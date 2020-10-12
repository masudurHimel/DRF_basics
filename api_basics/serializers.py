from rest_framework import serializers
from api_basics.models import article


class articleSerializers(serializers.ModelSerializer):
    class Meta:
        model = article
        fields = "__all__"

        

        
         