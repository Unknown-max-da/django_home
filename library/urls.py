from django.urls import path
from .views import BookListApiView,BookDetailApiView,BookDeleteApiView

urlpatterns=[
    path('kitoblar/', BookListApiView.as_view()),
    path('kitob/<int:pk>/', BookDetailApiView.as_view() ),
    path('kitob/delete/<int:pk>', BookDeleteApiView.as_view()),
]