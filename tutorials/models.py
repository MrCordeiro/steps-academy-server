from django.db import models


class Tutorial(models.Model):
    """A Tutorial is a lesson for individual self-study"""

    # Relations

    # Attributes - Mandatory
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    # Attributes - Optional

    # Methods

    # Managers
    objects = models.Manager()

    # Meta and String
    def __str__(self):
        return self.title


class Step(models.Model):
    """The most granular unit of a tutorial"""
    # Relations
    tutorial = models.ForeignKey(
        Tutorial, on_delete=models.CASCADE, related_name="steps"
    )

    # Attributes - Mandatory
    title = models.CharField(max_length=200)
    body = models.TextField()
    order = models.IntegerField(default=0)

    # Meta and String
    class Meta:
        ordering = ['order',]
    
    def __str__(self):
        return self.title
