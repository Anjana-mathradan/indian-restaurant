from django.urls import path
from frontend import views
urlpatterns=[ 
    path('',views.fnindex,name="fnindex"),
    path('fncontact/',views.fncontact,name="fncontact"),
    path('fnabout/',views.fnabout,name="fnabout"),
    path('displaycategorypage/<itemcategory>/',views.displaycategorypage,name="displaycategorypage"),
    path('singleproduct/<int:dataid>/',views.singleproduct,name="singleproduct"),
    path('registersave/',views.registersave,name="registersave"),
    path('frontreg/',views.frontreg,name="frontreg"),
    path('frontlogin/',views.frontlogin,name="frontlogin"),
    path('frontloginsave/',views.frontloginsave,name="frontloginsave"),
    path('frontlogout/',views.frontlogout,name="frontlogout"),
    ]