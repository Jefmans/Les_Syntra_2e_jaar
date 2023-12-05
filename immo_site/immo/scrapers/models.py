from django.db import models

# Create your models here.

class ImmoWebData(models.Model):
    original_url = models.URLField()
    # original_id = models.CharField(max_length=15, unique=True)
    original_id = models.CharField(max_length=15)
    postal_code = models.IntegerField()
    price = models.CharField(max_length=20)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['original_id', 'postal_code'],
                name = "unique_id"
            )
        ]

    def __str__(self) -> str:
        return self.original_url