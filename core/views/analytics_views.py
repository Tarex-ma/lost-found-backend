from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from core.services.analytics_service import get_dashboard_stats

class AdminDashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        data = get_dashboard_stats()
        return Response(data)