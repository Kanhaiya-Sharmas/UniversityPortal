from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from details.models import Details
from details.serializers import DetailsSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def details_list(request):
    if request.method == 'GET':
        details = Details.objects.all()

        Mentor_Name = request.GET.get('Mentor_Name', None)
        if Mentor_Name is not None:
            details = details.filter(Mentor_Name__icontains=Mentor_Name)

        details_serializer = DetailsSerializer(details, many=True)
        return JsonResponse(details_serializer.data, safe=False)

    elif request.method == 'POST':
        details_data = JSONParser().parse(request)
        details_serializer = DetailsSerializer(data=details_data)
        if details_serializer.is_valid():
            details_serializer.save()
            return JsonResponse(details_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(details_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Details.objects.all().delete()
        return JsonResponse({'message': '{} Details were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        count = Details.objects.all().delete()
        return JsonResponse({'message': '{} Details were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)