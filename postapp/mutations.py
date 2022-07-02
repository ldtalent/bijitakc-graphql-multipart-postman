import graphene
from graphene_file_upload.scalars import Upload

from .models import Post
from .types import PostType


class CreatePostMutation(graphene.Mutation):
    post = graphene.Field(PostType)

    class Arguments:
        title = graphene.String(required=True)
        photo = Upload(required=True)
        caption = graphene.String(required=True)
        
    @classmethod
    def mutate(cls, root, info, title, photo, caption):
        post_ins = Post.objects.create(title=title, photo=photo, caption=caption)
        return CreatePostMutation(post=post_ins)


class Mutation(graphene.ObjectType):
    create_post = CreatePostMutation.Field()
