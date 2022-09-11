from django.urls import path

from . import aboutMeViews

urlpatterns = [
    path('', aboutMeViews.self_introduction, name='selfIntroduction'),
    path('test/<int:id>', aboutMeViews.test, name='test'),
    path('healthcheck', aboutMeViews.health_check, name='healthcheck'),
]