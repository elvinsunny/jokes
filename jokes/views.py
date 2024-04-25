from django.shortcuts import render

# Create your views here.


# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Joke
from .serializers import JokeSerializer







from rest_framework import generics
from .models import Joke
from .serializers import JokeSerializer

class JokeListCreate(generics.ListCreateAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class JokeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer






# views.py

from rest_framework import generics
from .models import Joke
from .serializers import JokeSerializer

class JokeListCreate(generics.ListCreateAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

    def get_queryset(self):
        language = self.kwargs.get('language')
        if language:
            return Joke.objects.filter(language=language)
        return Joke.objects.all()

class JokeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer




# class JokesByLanguageAPIView(APIView):
#     def get(self, request, language, format=None):
#         jokes = Joke.objects.filter(language=language)
#         serializer = JokeSerializer(jokes, many=True)
#         return Response(serializer.data)

# class AddJokeAPIView(APIView):
#     def post(self, request, format=None):
#         serializer = JokeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)








from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Joke

class LanguagesAPIView(APIView):
    def get(self, request, format=None):
        languages = Joke.objects.values_list('language', flat=True).distinct()
        return Response(languages)









# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Joke
from .serializers import JokeSerializer

class AllJokesAPIView(APIView):
    def get(self, request, format=None):
        jokes = Joke.objects.all()
        serializer = JokeSerializer(jokes, many=True)
        return Response(serializer.data)


# # views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Joke
# from .serializers import JokeSerializer

# class DeleteJokeAPIView(APIView):
#     def delete(self, request, joke_id, format=None):
#         try:
#             joke = Joke.objects.get(id=joke_id)
#         except Joke.DoesNotExist:
#             return Response({"error": "Joke not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         joke.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# # views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Joke
# from .serializers import JokeSerializer

# class UpdateJokeAPIView(APIView):
#     def put(self, request, joke_id, format=None):
#         try:
#             joke = Joke.objects.get(id=joke_id)
#         except Joke.DoesNotExist:
#             return Response({"error": "Joke not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = JokeSerializer(joke, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, joke_id, format=None):
#         try:
#             joke = Joke.objects.get(id=joke_id)
#         except Joke.DoesNotExist:
#             return Response({"error": "Joke not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = JokeSerializer(joke, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



