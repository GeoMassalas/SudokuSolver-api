from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.sudoku import Sudoku
from core.models import SudokuModel
from .serializers import SudokuSerializer


@api_view(['POST'])
def solve(request, pk=None):
    msg = ''
    sdk = Sudoku()
    if len(request.data['input_string']) == 81:
        sdk.str_to_grid(request.data['input_string'])
        sdk.solve()
        print('--------------')
        print(sdk.grid_to_str())
        print('--------------')
        if len(sdk.get_solutions()) > 1:
            s = 'MULT'
        else:
            s = 'UNIQUE'
        if len(sdk.solution_to_str()) == 81:
            sudoku = SudokuModel.objects.create(
                input_string=request.data['input_string'],
                solution_string=sdk.solution_to_str,
                no_of_solutions=s)
            serializer = SudokuSerializer(sudoku, many=False)
            msg = {'message': 'New Data Added', 'result': serializer.data}
            sts = status.HTTP_200_OK
        else:
            msg = {'message': 'input_string should be 81 chars long'}
            sts = status.HTTP_400_BAD_REQUEST
    else:
        msg = {'message': 'input_string should be 81 chars long.'}
        sts = status.HTTP_400_BAD_REQUEST
    return Response(msg, status=sts)
