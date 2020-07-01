from rest_framework import serializers
from core.models import SudokuModel


class SudokuSerializer(serializers.ModelSerializer):

    class Meta:
        model = SudokuModel
        fields = ('input_string', 'solution_string', 'no_of_solutions', 'difficulty', 'nums')

    def validate(self, data):
        if 'input_sting' in data:
            if len(data['input_string']) != 81:
                raise serializers.ValidationError("Input string should be 81 characters long")
        else:
            raise serializers.ValidationError("No input string found.")
        return data
