from rest_framework import serializers

from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (

            'id',
            'autor',
            'titulo',
            'contenido',
            'publicado',
        )

        model = models.Post

