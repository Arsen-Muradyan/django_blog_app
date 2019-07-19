from django.urls import path
from . import views
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:id>', views.show, name='show'),
  path('new', views.create, name='new'),
  path('destroy/<int:id>', views.destroy, name='delete'),
  path('<int:id>/edit', views.edit, name='edit')
]