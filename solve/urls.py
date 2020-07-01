from django.urls import path
from .views import solve
urlpatterns = [
    path('', solve, name="Solve Sudoku"),
    ]
