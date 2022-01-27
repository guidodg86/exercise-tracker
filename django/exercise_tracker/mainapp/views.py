from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from mainapp.models import User, Exercise
from mainapp.serializer import ExerciseSerializer, UserLogSerializer, FilteredUserLogSerializer

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
        try:  
            description = request.data['description']
            duration = request.data['duration']
            if 'date' in request.data:
                received_date = datetime.strptime(request.data['date'], "%Y-%m-%d")
            else:
                received_date = datetime.now()
            user_selected = User.objects.get(pk=id_user)
            new_exercise_record = Exercise(id_user=user_selected, description=description, duration=duration, date_exercise=received_date)
            new_exercise_record.save()
            response_exercise = ExerciseSerializer(new_exercise_record)
            return Response(response_exercise.data)
        except:
            return Response({"error": "bad request"})


class UserExerciseLogView(APIView):
    def get(self, request, id_user):
        #try:
        user_selected = User.objects.get(pk=id_user)
        if len(request.query_params) == 0:
            response_exercise_log = UserLogSerializer(user_selected)
            return Response(response_exercise_log.data)

        for param in request.query_params:
            if param != 'limit' and param != 'from' and param != 'to':
                return Response({"error": "bad request"})
            if param == 'limit':
                limit_of_logs = int(request.query_params[param])
            if param == 'from':
                initial_date_logs = datetime.strptime(request.query_params[param], "%Y-%m-%d")
            if param == 'to':
                last_date_logs = datetime.strptime(request.query_params[param], "%Y-%m-%d")

        response_exercise_log= FilteredUserLogSerializer(user_selected, context={"limit": limit_of_logs})
        return Response(response_exercise_log.data)
"""        except:
            return Response({"error": "bad request"})"""
            