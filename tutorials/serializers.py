from rest_framework import serializers
from . import models


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Step
        fields = ('order', 'title', 'body')

class TutorialSerializer(serializers.HyperlinkedModelSerializer):
    steps = StepSerializer(many=True)

    class Meta:
        model = models.Tutorial
        fields = ('url', 'id', 'title', 'steps')
