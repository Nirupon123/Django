import graphene
from accounts.graphql.queries import Query
from accounts.graphql.mutations import Mutation


schema = graphene.Schema(query=Query, mutation=Mutation)

