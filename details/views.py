from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from details.models import Mentor
from details.serializers import MentorSerializer
from rest_framework.decorators import api_view


# Create your views here.
# START function mentor_list
@api_view(['GET', 'POST', 'DELETE'])
def mentor_list(request):
    # Get all mentor list
    if request.method == 'GET':
        details = Mentor.objects.all()

        mentor = request.GET.get('mentor', None)
        if mentor is not None:
            details = details.filter(mentor__icontains=mentor)

        details_serializer = MentorSerializer(details, many=True)
        return JsonResponse(details_serializer.data, safe=False)
    # Add a new mentor
    elif request.method == 'POST':
        mentor_data = JSONParser().parse(request)
        mentor_serializer = MentorSerializer(data=mentor_data)
        if mentor_serializer.is_valid():
            mentor_serializer.save()
            return JsonResponse(mentor_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(mentor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Delete all mentor
    elif request.method == 'DELETE':
        count = Mentor.objects.all().delete()
        return JsonResponse({'message': '{} details were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        count = Mentor.objects.all().delete()
        return JsonResponse({'message': '{} details were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
# END function mentor_lis


# START function mentor_details by id
@api_view(['GET', 'PUT', 'DELETE'])
def mentor_detail(request, pk):
    try:
        mentor = Mentor.objects.get(pk=pk)

        if request.method == 'GET':
            detail_serializer = MentorSerializer(mentor)
            return JsonResponse(detail_serializer.data)
        elif request.method == 'PUT':
            detail_data = JSONParser().parse(request)
            detail_serializer = MentorSerializer(mentor, data=detail_data)
            if detail_serializer.is_valid():
                detail_serializer.save()
                return JsonResponse(detail_serializer.data)
            return JsonResponse(detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            mentor.delete()
            return JsonResponse({'message': 'mentor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Mentor.DoesNotExist:
        return JsonResponse({'message': 'The mentor does not exist'}, status=status.HTTP_404_NOT_FOUND)

def student_list(request, pk):
    pass