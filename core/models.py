from django.db import models


class SudokuModel(models.Model):

    input_string = models.CharField(max_length=81, null=False, unique=True)
    solution_str = models.CharField(max_length=81, null=True)
    difficulty = models.PositiveSmallIntegerField(null=False)
    dataset = models.CharField(max_length=30, null=True)
    dataset_id = models.IntegerField(null=True)
    clues = models.IntegerField(null=True)


