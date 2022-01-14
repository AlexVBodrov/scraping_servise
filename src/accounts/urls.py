from django.urls import path, include
from .views import view_account

urlpatterns = [
    path('account/', view_account, name='view_account'),
]
