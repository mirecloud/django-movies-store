from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
path('', views.index, name='movies.index'),
path('<int:id>/', views.show, name='movies.show'),
path('<int:id>/review/create/', views.create_review,name='movies.create_review'),

]
urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
