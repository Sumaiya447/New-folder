from django.urls import path
from . import views


urlpatterns = [
    path('',views.homePage,name='home'),
    path('addEmp',views.addEmp,name='addEmp'),
    path('editEmp',views.editEmp,name='editEmp'),
    path('updateEmp/<str:id>',views.updateEmp,name='updateEmp'),
    path('deleteEmp/<str:id>',views.deleteEmp,name='deleteEmp'),
   
]
