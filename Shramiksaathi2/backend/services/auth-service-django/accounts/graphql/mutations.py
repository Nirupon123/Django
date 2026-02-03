import graphene
import graphql_jwt
from .types import UserType
from django.contrib.auth import get_user_model



class AuthMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()





User = get_user_model()

class RegisterUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(lambda: UserType)

    def mutate(self, info, email, password):
        user = User.objects.create_user(
            email=email,
            password=password
        )
        return RegisterUser(user=user)
    


class Mutation(AuthMutation, graphene.ObjectType):
    register_user = RegisterUser.Field()


