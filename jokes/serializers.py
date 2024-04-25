# serializers.py
from rest_framework import serializers
from .models import Joke

class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = ['id', 'text', 'language']


# # serializers.py
# from rest_framework import serializers
# from .models import Joke

# class JokeSerializer(serializers.ModelSerializer):
#     text = serializers.CharField(max_length=255)
#     language = serializers.CharField(max_length=50)

#     class Meta:
#         model = Joke
#         fields = ['id', 'text', 'language']

#     def create(self, validated_data):
#         return Joke.objects.create(**validated_data)
