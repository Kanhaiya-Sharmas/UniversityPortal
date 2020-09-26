from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from details.models import Mentor
from details.serializers import MentorSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def mentor_list(request):
    if request.method == 'GET':
        details = Mentor.objects.all()

        mentor = request.GET.get('mentor', None)
        if mentor is not None:
            details = details.filter(mentor__icontains=mentor)

        details_serializer = MentorSerializer(details, many=True)
        return JsonResponse(details_serializer.data, safe=False)

    elif request.method == 'POST':
        mentor_data = JSONParser().parse(request)
        mentor_serializer = MentorSerializer(data=mentor_data)
        if mentor_serializer.is_valid():
            mentor_serializer.save()
            return JsonResponse(mentor_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(mentor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Mentor.objects.all().delete()
        return JsonResponse({'message': '{} details were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        count = Mentor.objects.all().delete()
        return JsonResponse({'message': '{} details were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)