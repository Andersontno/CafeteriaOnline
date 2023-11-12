from django.urls import path
from cafeteria.views import index

urlpatterns = [
    path('', index)

]
