from graphene import ObjectType, Schema

from apps.action.schemas.schema import Mutation as ActionMutation
from apps.blog.schemas.schema import Query as BlogQuery
from apps.contact.schemas.schema import Mutation as ContactMutation
from apps.conversions.schemas.schema import Mutation as ConversionMutation
from apps.cookies.schemas.schema import Query as CookieQuery
from apps.initial_files.schemas.schema import Mutation as InitialFileMutation
from apps.pages.schemas.schema import Query as PageQuery
from apps.users.schemas.schema import Mutation as UserMutation
from apps.users.schemas.schema import Query as UserQuery


class Query(
    PageQuery,
    BlogQuery,
    CookieQuery,
    UserQuery,
    ObjectType,
):
    pass


class Mutation(
    ConversionMutation,
    InitialFileMutation,
    ActionMutation,
    ContactMutation,
    UserMutation,
    ObjectType,
):
    pass


schema = Schema(query=Query, mutation=Mutation)
