from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from details.models import Mentor
from details.models import Student
from details.serializers import MentorSerializer
from details.serializers import StudentSerializer
from rest_framework.decorators import api_view


# Create your views here

# START function mentor_list
@api_view(['GET', 'POST', 'DELETE'])
def mentor_full(request):
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
def mentor_byid(request, pk):
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


@api_view(['GET', 'POST', 'DELETE'])
def student_full(request):
    # Get all student list
    if request.method == 'GET':
        details = Student.objects.all()

        student = request.GET.get('student', None)
        if student is not None:
            details = details.filter(student__icontains=student)

        details_serializer = StudentSerializer(details, many=True)
        return JsonResponse(details_serializer.data, safe=False)
    # Add a new student
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Delete all student
    elif request.method == 'DELETE':
        count = Student.objects.all().delete()
        return JsonResponse({'message': '{} details were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        count = Student.objects.all().delete()
        return JsonResponse({'message': '{} details were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def mentor_byid(request, pk):
    try:
        student = Student.objects.get(pk=pk)

        if request.method == 'GET':
            detail_serializer = StudentSerializer(student)
            return JsonResponse(detail_serializer.data)
        elif request.method == 'PUT':
            detail_data = JSONParser().parse(request)
            detail_serializer = StudentSerializer(student, data=detail_data)
            if detail_serializer.is_valid():
                detail_serializer.save()
                return JsonResponse(detail_serializer.data)
            return JsonResponse(detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            student.delete()
            return JsonResponse({'message': 'student was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Student.DoesNotExist:
        return JsonResponse({'message': 'The student does not exist'}, status=status.HTTP_404_NOT_FOUND)