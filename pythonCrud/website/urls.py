from django.urls import path
from website.apis import *


urlpatterns = [
    path('createRecord/', RecordDataAPI.as_view(), name='create-record-api'),
]


