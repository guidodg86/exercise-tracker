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

