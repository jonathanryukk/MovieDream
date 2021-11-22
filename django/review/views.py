from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Review, ReviewComment

from .serializers import ReviewSerializer, ReviewListSerializer, CommentSerializer



@api_view(['GET', 'POST'])
def review_list_or_create(request):
    
    def artist_list():
        artists = Review.objects.all()
        serializer = ReviewSerializer(artists, many=True)
        return Response(serializer.data)

    def create_artist():
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    if request.method == 'GET':
        return artist_list()
    elif request.method == 'POST':
        return create_artist()


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_or_update_or_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    def artist_detail():
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def update_artist():
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete_artist():
        review.delete()
        return Response(data='delete successfully', status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return artist_detail()
    elif request.method == 'PUT':
        return update_artist()
    elif request.method == 'DELETE':
        return delete_artist()


