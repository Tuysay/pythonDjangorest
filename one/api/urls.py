from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import *

routerA = routers.SimpleRouter()
routerA.register(r'author', AuthorDetailAPI)

routerB = routers.SimpleRouter()
routerB.register(r'books', BookDetailAPI)

urlpatterns = [
    path('api/v1/', include(routerA.urls)),
    path('api/v1/', include(routerB.urls)),
    path('api/v1/add_book', CreateBookAPI.as_view()),

]
