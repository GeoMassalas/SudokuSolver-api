from rest_framework import serializers
from core.models import SudokuModel
from resources.sudoku import Sudoku


class SudokuSerializer(serializers.ModelSerializer):

    class Meta:
        model = SudokuModel
        fields = ('id', 'input_string', 'solution_str', 'difficulty', 'clues', 'dataset', 'dataset_id')

    def validate(self, data):
        if ('input_string' in data) & ('difficulty' in data):
            if (len(data['input_string']) != 81) & (data['input_string'].isdigit()):
                raise serializers.ValidationError("Input string should be 81 arithmetic characters long")
        else:
            raise serializers.ValidationError("No input string found.")
        sdk = Sudoku()
        sdk.str_to_grid(data['input_string'])
        if sdk.is_valid():
            if 'solution_str' not in data:
                sdk.solve()
                if len(sdk.get_solutions()) > 1:
                    raise serializers.ValidationError("More than one possible Solutions.")
                data['solution_str'] = sdk.solution_to_str()
        else:
            raise serializers.ValidationError("Provided Sudoku is not valid.")

        # Count Clues
        count = 0
        for i in data['input_string']:
            if i != '0':
                count = count + 1
        data['clues'] = count

        return data
