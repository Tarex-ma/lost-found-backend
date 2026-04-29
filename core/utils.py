from .models import LostItem
from django.core.mail import send_mail

def find_matches(found_item):
    print("=== DEBUG START ===")
    print("Found Item:", found_item.title)
    print("Category:", found_item.category)
    print("Location:", found_item.location)

    matches = LostItem.objects.filter(status='open')
    print("All Lost Items Count:", matches.count())

    for item in matches:
        print("LostItem:", item.title, item.category, item.location)

    category_matches = matches.filter(category=found_item.category)
    print("Category Matches:", category_matches.count())

    location_matches = matches.filter(location__icontains=found_item.location)
    print("Location Matches:", location_matches.count())

    final_matches = (category_matches | location_matches).distinct()
    print("Final Matches:", final_matches.count())

    print("=== DEBUG END ===")

    return final_matches[:5]


def send_match_notification(user_email, lost_item, found_item):
    subject = "Possible Match Found!"

    message = f"""
    Good news!

    Your lost item "{lost_item.title}" may match a found item.

    Found Item: {found_item.title}
    Location: {found_item.location}

    Please log in to review and claim.
    """

    send_mail(
        subject,
        message,
        'noreply@lostfound.com',
        [user_email],
        fail_silently=True,
    )
