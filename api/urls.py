from django.urls import path, include

urlpatterns = [
    path('', include('solve.urls')),
    path('api/sudokus', include('sudokus.urls')),
    path('', include('accounts.urls'))
]
