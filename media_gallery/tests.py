from django.test import TestCase
from django.urls import reverse

from .models import MediaItem


class MediaItemTests(TestCase):

    def test_media_item_creation(self):

        item = MediaItem.objects.create(
            title="Test Multimedia Item",
            description="Test description"
        )

        self.assertEqual(
            item.title,
            "Test Multimedia Item"
        )


class GalleryViewTests(TestCase):

    def test_home_page_loads(self):

        response = self.client.get(
            reverse("home")
        )

        self.assertEqual(
            response.status_code,
            200
        )


    def test_media_detail_page_loads(self):

        item = MediaItem.objects.create(
            title="Test Multimedia Item"
        )

        response = self.client.get(
            reverse(
                "media_detail",
                args=[item.pk]
            )
        )

        self.assertEqual(
            response.status_code,
            200
        )