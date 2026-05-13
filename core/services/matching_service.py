# core/services/matching_service.py

def calculate_match_score(lost, found):
    score = 0

    if lost.category == found.category:
        score += 40

    if lost.location.lower() == found.location.lower():
        score += 30

    if lost.description:
        words = lost.description.lower().split()
        if any(word in found.description.lower() for word in words):
            score += 30

    return score