from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_pk>/<int:lesson_pk>/', views.lesson_detail),
    path('<int:pk>', views.course_detail, name='course_detail'),
]

#tener cuidado con el orden de las url, django revisa en orden descendente

