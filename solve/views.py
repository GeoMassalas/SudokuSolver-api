import random
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from resources.sudoku import Sudoku
from core.models import SudokuModel
from sudokus.serializers import SudokuSerializer


@api_view(['POST'])
def solve(request, pk=None):
    sdk = Sudoku()
    if len(request.data['input_string']) == 81:
        sdk.str_to_grid(request.data['input_string'])
        if sdk.is_valid():
            sdk.solve()
            if len(sdk.get_solutions()) > 1:
                s = 'False'
            else:
                s = 'True'
            msg = {'input_string': request.data['input_string'], 'solution': sdk.solution_to_str(), 'Unique Solution': s}
            sts = status.HTTP_200_OK
        else:
            msg = {'message': 'Sudoku is not valid.'}
            sts = status.HTTP_400_BAD_REQUEST
    else:
        msg = {'message': 'input_string should be 81 chars long.'}
        sts = status.HTTP_400_BAD_REQUEST
    return Response(msg, status=sts)


@api_view(['GET'])
def serve(request, pk=None):
    if 'difficulty' in request.data:
        dif = int(request.data['difficulty'])
        if (dif > 0) & (dif < 10):
            sudokus = SudokuModel.objects.filter(difficulty=dif)
            if len(sudokus) > 0:
                sdk = random.choice(sudokus)
                serializer = SudokuSerializer(sdk, many=False)
                msg = {'data': serializer.data}
                sts = status.HTTP_200_OK
            else:
                msg = {'data': 'There is no sudoku with that difficulty left.'}
                sts = status.HTTP_400_BAD_REQUEST
        else:
            msg = {'message': 'You should provide a difficulty of 1 to 9.'}
            sts = status.HTTP_400_BAD_REQUEST
    return Response(msg, status=sts)




