import graphene
from graphene_django import DjangoListField

from .models import Post
from .types import PostType


class Query(graphene.ObjectType):
    all_posts = DjangoListField(PostType)

    def resolve_all_posts(root, info):
        return Post.objects.all()