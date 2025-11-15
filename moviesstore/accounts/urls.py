from django.urls import path
from . import views
urlpatterns = [
path('signup', views.signup, name='accounts.signup'),
path('login', views.login, name='accounts.login'),
path('logout', views.logout, name='accounts.logout'),
path('', views.login, name='accounts.index'),
#path('<int:id>/', views.show, name='movies.show'),
#path('<int:id>/review/create/', views.create_review,name='movies.create_review'),
]
