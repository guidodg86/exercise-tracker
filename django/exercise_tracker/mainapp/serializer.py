from dataclasses import field
from rest_framework import serializers
from mainapp.models import User, Exercise

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id_user', 'description', 'duration', 'date_exercise']


class ExerciseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['description', 'duration', 'date_exercise']

class UserLogSerializer(serializers.ModelSerializer):
    log = ExerciseLogSerializer(many = True, read_only=True)

    class Meta:
        model = User
        fields = ['_id', 'username', 'log']

class FilteredUserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'count', '_id', 'log']

    log = serializers.SerializerMethodField('get_log')
    count = serializers.SerializerMethodField('get_count')

    def get_log(self, _id):
        if not hasattr(self, '_two_values'):
            self.log_data = FilteredUserLogSerializer.obtain_logs(self, _id)
        return self.log_data['logs']

    def get_count(self, _id):
        if not hasattr(self, '_two_values'):
            self.log_data = FilteredUserLogSerializer.obtain_logs(self, _id)
        return self.log_data['count']

    def obtain_logs(self, _id):
        try:
            exercises_from = Exercise.objects.filter(id_user=_id, date_exercise__gt=self.context.get("from_date"))
        except:
            exercises_from = Exercise.objects.filter(id_user=_id,)
        try:
            exercises_from_to = exercises_from.filter(date_exercise__lt=self.context.get("to_date"))
        except:
            exercises_from_to = exercises_from
        try:
            exercises = exercises_from_to[:self.context.get("limit")]   
        except:
            exercises = exercises_from_to
        exercise_subset = ExerciseLogSerializer(instance=exercises, many=True)
        log_count = len(exercise_subset.data)
        return {"logs": exercise_subset.data, "count":log_count}