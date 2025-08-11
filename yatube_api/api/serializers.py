from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Group, Follow, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'text', 'created', 'post')
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(read_only=True, slug_field='username')
    following = SlugRelatedField(
        queryset=User.objects.all(), slug_field='username')

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate(self, data):
        request = self.context['request']
        following_user = data['following']

        if request.user == following_user:
            raise serializers.ValidationError("Нельзя подписаться на себя")

        if Follow.objects.filter(
            user=request.user, following=following_user
        ).exists():
            raise serializers.ValidationError(
                "Вы уже подписаны на этого пользователя")

        return data
