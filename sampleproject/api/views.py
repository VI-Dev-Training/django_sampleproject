
import project1
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import ProjectSerializer
from project1.models import Project, Review
from api import serializers


@api_view(['GET'])
def getRoutes(request):

    routes = [

        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},

    ]

    return Response(routes)



@api_view(['GET'])
def getProjects(request):

    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProject(request, pk):
    project = Project.objects.get(id = pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def projectVote(request, pk):
    
    project = Project.objects.get(id=pk)
    
    # getting the current user and data given in the post
    user = request.user.profile
    data = request.data
    
    # getting Review from models checking to get or create by owner of the review
    # and project that user is giving review for
    review , created = Review.objects.get_or_create(
        owner = user,
        project = project
    )
    
    # retreving the value from post and assigning it to the review database 
    review.value = data['value']
    review.save()
    project.getVoteCount # triggering  getVoteCount to update the votes
    
    serializer = ProjectSerializer(project, many = False)
    return Response(serializer.data)












