from celery import shared_task
from .models.item import LostItem, FoundItem
from .models.match_history import MatchHistory
from .utils import send_match_notification
from core.services.matching_service import calculate_match_score


@shared_task
def process_matches(found_item_id):
    found_item = FoundItem.objects.get(id=found_item_id)

    lost_items = LostItem.objects.filter(status="open")

    for lost in lost_items:
        score = calculate_match_score(lost, found_item)

        if score >= 60:
            MatchHistory.objects.get_or_create(
                lost_item=lost,
                found_item=found_item,
                defaults={"confidence_score": score}
            )

            if lost.user and lost.user.email:
                send_match_notification(
                    lost.user.email,
                    lost.title,
                    found_item.title
                )

    return "done"