from django.shortcuts import get_object_or_404, render

from .models import MediaItem


def home(request):

    media_items = MediaItem.objects.all().order_by("-created_at")

    context = {
        "media_items": media_items
    }

    return render(
        request,
        "media_gallery/home.html",
        context
    )


def media_detail(request, pk):

    media_item = get_object_or_404(
        MediaItem,
        pk=pk
    )

    context = {
        "media_item": media_item
    }

    return render(
        request,
        "media_gallery/media_detail.html",
        context
    )