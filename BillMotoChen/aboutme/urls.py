from django.urls import path, re_path

from . import aboutMeViews

urlpatterns = [
    # home
    path('', aboutMeViews.self_introduction, name='selfIntroduction'),

    # hobbies
    path('hobbies', aboutMeViews.hobbies, name='hobbies'),
    path('hobbies/pieces/search/', aboutMeViews.pieces_search, name='piecesSearch'),

    # others
    path('test/<int:id>', aboutMeViews.test, name='test'),
    path('healthcheck', aboutMeViews.health_check, name='healthcheck'),
]