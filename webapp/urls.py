from django.urls import path

from webapp.views import index, detail, delete, create

urlpatterns = [
    path('', index),
    path('task/', detail),
    path('delete/', delete),
    path('create_task/', create)
]
