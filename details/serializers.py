from rest_framework import serializers
from details.models import Mentor
from details.models import Student


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ('id',
                  'mentor',
                  'lecture',
                  'status',
                  'Remark')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id',
                  'student',
                  'math',
                  'physics',
                  'english',
                  'status',
                  'Remark')
