from django.urls import path
from .views import solve, serve
urlpatterns = [
    path('api/solve', solve, name="Solve Sudoku"),
    path('api/serve', serve, name="Serve Sudoku"),
    ]
