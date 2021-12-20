import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from project.models import Project, TODO
from users.models import CustomUser


class UserType(DjangoObjectType):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class ProjectType(DjangoObjectType):

    class Meta:
        model = Project
        fields = '__all__'


class TodoType(DjangoObjectType):

    class Meta:
        model = TODO
        fields = '__all__'


class Query(ObjectType):

    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)
    all_todo = graphene.List(TodoType)

    def resolve_all_users(root, info):
        return CustomUser.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todo(root, info):
        return TODO.objects.all()

    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))
    project_by_id = graphene.Field(ProjectType, id=graphene.Int(required=False))
    todo_by_id = graphene.Field(TodoType, id=graphene.Int(required=False))

    def resolve_user_by_id(root, info, id=None):
        user = CustomUser.objects.all()
        if id:
            return user.get(id=id)
        return None

    def resolve_project_by_id(root, info, id=None):
        project = Project.objects.all()
        if id:
            return project.get(id=id)
        return None

    def resolve_todo_by_id(root, info, id=None):
        project = TODO.objects.all()
        if id:
            return project.get(id=id)
        return None

    project_by_user = graphene.List(ProjectType, username=graphene.String(required=False))

    def resolve_project_by_user(root, info, username=None):
        projects = Project.objects.all()
        if username:
            return projects.filter(users__username=username)
        return projects


class ProjectUpdateMutation(graphene.Mutation):

    class Arguments:
        id = graphene.Int(required=True)
        name_project = graphene.String(required=True)
        url_project = graphene.String(required=True)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(self, oot, info, name_project, url_project, id):
        project = Project.objects.get(id=id)
        project.name_project = name_project
        project.url_project = url_project
        project.save()
        return ProjectUpdateMutation(project=project)


class Mutation(graphene.ObjectType):
    update_project = ProjectUpdateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
