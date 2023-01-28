from django.urls import path
from backend import views

urlpatterns= [ 

    path('indexfn/',views.indexfn,name='indexfn'),
    path('bookinput/',views.bookinput,name='bookinput'),

    path('loginpage/',views.loginpage,name="loginpage"),
    path('loginsave/',views.loginsave,name="loginsave"),
    path('logoutpage/',views.logoutpage,name="logoutpage"),
    path('booksave/',views.booksave,name='booksave'),
    path('bookoutput/',views.bookoutput,name="bookoutput"),
    path('editpage/<int:dataid>/',views.editpage,name="editpage"),
    path('updatefn/<int:dataid>/',views.updatefn,name="updatefn"),
    path('deletefn/<int:dataid>/',views.deletefn,name="deletefn"),
    path('categoryip/',views.categoryip,name="categoryip"),
    path('savecategory/',views.savecategory,name="savecategory"),
    path('categoryop/',views.categoryop,name="categoryop"),
    path('categoryedit/<int:dataid>/',views.categoryedit,name="categoryedit"),
    path('categoryupdate/<int:dataid>/',views.categoryupdate,name="categoryupdate"),
    path('categorydel/<int:dataid>/',views.categorydel,name="categorydel"),
    path('contact/',views.contact,name="contact"),
    path('productinput/',views.productinput,name="productinput"),
    path('saveproducts/',views.saveproducts,name="saveproducts"),
    path('productoutput/',views.productoutput,name="productoutput"),
    path('editproduct/<int:dataid>/',views.editproduct,name="editproduct"),
    path('updateproduct/<int:dataid>/',views.updateproduct,name="updateproduct"),
    path('productdel/<int:dataid>/',views.productdel,name="productdel")
 ]