from django.urls import path
from . import views
urlpatterns=[

    # path('',views.index_home),
    path('',views.todos_json)
]