from rest_framework import serializers
from webapp.models import employees


class employeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = "__all__"