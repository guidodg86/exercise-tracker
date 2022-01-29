from dataclasses import field
from rest_framework import serializers
from mainapp.models import User, Exercise


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
        fields = ['_id', 'username', 'log']

    log = serializers.SerializerMethodField('get_log')

    def get_log(self, _id):
        exercises = Exercise.objects.filter(id_user=_id)[:self.context.get("limit")]
        exercise_subset = ExerciseLogSerializer(instance=exercises, many=True)
        return exercise_subset.data