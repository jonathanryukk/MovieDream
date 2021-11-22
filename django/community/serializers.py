from rest_framework import serializers
from .models import Board, BoardComment




class BoardListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Board
        fields = ('id','title',)

class BoardSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Board
        fields = ('id','title', 'content', 'user', 'created_at', 'updated_at')
        read_only_fields = ('user', 'created_at', 'updated_at',)

class BoardCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardComment
        fields = ('id','user', 'board', 'content', 'created_at', 'updated_at')
        read_only_fields = ('user', 'board', 'created_at', 'updated_at')

