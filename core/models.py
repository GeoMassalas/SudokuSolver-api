from django.db import models


class SudokuModel(models.Model):
    SOLUTION = {
        ('MULT', 'Multiple Solutions'),
        ('UNIQUE', 'Unique Solution'),
    }

    DIFFICULTY = {
        ('EASY', 'Easy'),
        ('MEDIUM', 'Medium'),
        ('HARD', 'Hard'),
        ('VERY_HARD', 'Very Hard'),
        ('IMPOSSIBLE', 'Impossible'),
    }

    input_string = models.CharField(max_length=81, null=False)
    solution_string = models.CharField(max_length=81)
    no_of_solutions = models.CharField(max_length=10, choices=SOLUTION)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY)

    def nums(self):
        count = 0
        for i in self.input_string:
            if i == '0':
                count = count + 1
        return 81-count

