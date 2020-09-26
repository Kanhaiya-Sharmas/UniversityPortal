from rest_framework import serializers
from details.models import Details


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ('id',
                  'Mentor_Name',
                  'Student_Name',
                  'Status',
                  'Remark')
