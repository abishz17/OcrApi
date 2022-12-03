from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FeedBack
from .serializers import FeedBackSerializer


class FeedbackView(APIView):
    def get(self, request):
        feedbacks = FeedBack.objects.all()
        serializer = FeedBackSerializer(feedbacks, many=True)
        return Response(serializer.data)

    def post(self, request):
        feedback_serializer = FeedBackSerializer(data=request.data)
        if feedback_serializer.is_valid():
            feedback_serializer.save()
            return Response(feedback_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('errors', feedback_serializer.errors)
            return Response(feedback_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
