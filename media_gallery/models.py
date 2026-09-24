from django.db import models

from cloudinary_storage.storage import (
    RawMediaCloudinaryStorage,
    VideoMediaCloudinaryStorage,
)


class MediaItem(models.Model):

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="images/",
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to="videos/",
        storage=VideoMediaCloudinaryStorage(),
        blank=True,
        null=True
    )

    audio = models.FileField(
        upload_to="audio/",
        storage=RawMediaCloudinaryStorage(),
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title