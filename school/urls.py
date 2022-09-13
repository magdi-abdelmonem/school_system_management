from django.urls import path,include
from .views import *
from django.db import router
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router=DefaultRouter()
router.register('subject',viewsets_subject)
router.register('teacher',viewsets_teacher)
router.register('student',viewsets_student)



urlpatterns = [
    path('CBV_List',CBV_List.as_view(),name='CBV_List'),
    path('CBV_List1/<int:pk>',CBV_List1.as_view(),name='CBV_List1'),

    path('mixin',mixin_list.as_view(),name='mixin'),
    path('mixin_pk/<int:pk>',mixin_pk.as_view(),name='mixin_pk'),

    path('generic',generic_list.as_view(),name='generic'),
    path('generic_pk/<int:pk>',generic_pk.as_view(),name='generic_pk'),


    path('viewsets_subject',include(router.urls)),
    path('viewsets_teacher',include(router.urls)),
    path('viewsets_student',include(router.urls)),


    #rest auth url give you choise log out from view

    path('api_auth',include('rest_framework.urls')),


    #token authentication
    path('api-token-auth', obtain_auth_token)
]
