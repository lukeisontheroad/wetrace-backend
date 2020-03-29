
from rest_framework import routers, serializers, viewsets
from fcm_django.api.rest_framework import FCMDeviceViewSet
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['signature', 'severity',]


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    http_method_names = ["post",]

class FCMDevicePostViewSet(FCMDeviceViewSet):
    http_method_names = ["post",]
