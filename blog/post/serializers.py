from rest_framework.serializers import ModelSerializer
from .models import Post 
from review.serializers import CommentSerializer


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance:Post):
        rep = super().to_representation(instance)
        print(rep)
        rep['likes'] = instance.likes.all().count()
        comments = instance.comments.all() # все комменты данного поста 
        rep['comments'] = CommentSerializer(comments, many=True).data
        return rep 