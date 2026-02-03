import graphene
from .types import UserType


class Query(graphene.ObjectType):

    me = graphene.Field(UserType)

    def resolve_me(self, info):
        user = info.context.user

        if user.is_anonymous:
            return None

        return user
