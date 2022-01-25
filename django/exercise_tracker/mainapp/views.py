from rest_framework.views import APIView
from rest_framework.response import Response
import json
from mainapp.models import User
import secrets

class CreateUserView(APIView):
    def post(self, request):
        try:          
            new_username = request.data['username']
            already_exists = User.objects.filter(username=new_username).exists()
            if already_exists:
                return Response({"error": "user already exists"})           
            new_user_record = User(username=new_username)
            new_user_record.save()
            return Response({"username": new_username, "_id":new_user_record._id})               
                
        except:
            return Response({"error": "bad request"})


