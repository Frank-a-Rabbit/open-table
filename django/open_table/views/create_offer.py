from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Offer, Member
from datetime import datetime


def create_offer(request):
    if request.method == "POST":
        # Get the logged-in member
        member = get_object_or_404(Member, id=request.user.id)

        # Extract offer details from the request
        title = request.POST.get("title")
        description = request.POST.get("description")
        condition = request.POST.get("condition")
        reward = request.POST.get("reward")
        expires = datetime.strptime(request.POST.get("expires"), "%Y-%m-%d %H:%M:%S")

        # Create the offer with a unique ID for this member
        offer = Offer.objects.create(
            member=member,
            title=title,
            description=description,
            condition=condition,
            reward=reward,
            expires=expires,
        )

        return JsonResponse({"message": "Offer created successfully", "offer_id": offer.id})
