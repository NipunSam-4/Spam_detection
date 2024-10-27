from django.urls import path
from .views import spam_detection

urlpatterns = [
   path('', spam_detection, name='spam_detection')

]