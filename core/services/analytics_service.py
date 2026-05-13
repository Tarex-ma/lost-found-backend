from ..models.match_history import MatchHistory
from ..models.claim import ClaimRequest
from ..models.item import LostItem, FoundItem
from django.db.models import Count


def get_dashboard_stats():
    total_matches = MatchHistory.objects.count()

    approved_claims = ClaimRequest.objects.filter(status="approved").count()
    rejected_claims = ClaimRequest.objects.filter(status="rejected").count()

    total_claims = ClaimRequest.objects.count()

    success_rate = (
        (approved_claims / total_claims) * 100
        if total_claims > 0 else 0
    )

    # Top categories
    top_lost_categories = (
        LostItem.objects.values("category")
        .annotate(count=Count("id"))
        .order_by("-count")[:5]
    )

    top_found_categories = (
        FoundItem.objects.values("category")
        .annotate(count=Count("id"))
        .order_by("-count")[:5]
    )

    return {
        "total_matches": total_matches,
        "approved_claims": approved_claims,
        "rejected_claims": rejected_claims,
        "success_rate": round(success_rate, 2),
        "top_lost_categories": list(top_lost_categories),
        "top_found_categories": list(top_found_categories),
    }