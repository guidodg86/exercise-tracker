from rest_framework.views import APIView
from rest_framework.response import Response

class CreateUserView(APIView):
    def post(self, request):
        return Response({
            "test": request.data })
