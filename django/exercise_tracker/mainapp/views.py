from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from mainapp.models import User, Exercise
from mainapp.serializer import ExerciseSerializer, UserLogSerializer

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


class CreateExerciseView(APIView):
    def post(self, request, id_user):     
        description = request.data['description']
        duration = request.data['duration']
        if 'date' in request.data:
            received_date = request.data['date']
        else:
            received_date = datetime.now()
        user_selected = User.objects.get(pk=id_user)
        new_exercise_record = Exercise(id_user=user_selected, description=description, duration=duration, date_exercise=received_date)
        new_exercise_record.save()
        response_exercise = ExerciseSerializer(new_exercise_record)
        return Response(response_exercise.data)


class UserExerciseLogView(APIView):
    def get(self, request, id_user):
        user_selected = User.objects.get(pk=id_user)
        response_exercise_log = UserLogSerializer(user_selected)
        return Response(response_exercise_log.data)




