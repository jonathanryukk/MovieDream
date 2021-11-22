from rest_framework import serializers
from .models import Review, ReviewComment
from accounts.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()
    class Meta:
        model = ReviewComment
        fields = ('id', 'content','user','created_at','updated_at')
        
class ReviewListSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()

    class Meta:
        model = Review
        fields = ('id', 'title', 'user')
        

class ReviewSerializer(serializers.ModelSerializer):
    # user = UserSerializer(required=False)
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()
    comment_set = CommentSerializer(many=True)
    # movie_title = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('id', 'content', 'review', 'created_at', 'updated_at', 'user', 'commnet_set')
        # read_only_fields = ('id', 'user', 'created_at', 'updated_at','comment_set', 'movie_title','movie')
    # def get_movie_title(self, obj):  # "get_" + field name
    #     return obj.movie.title

    