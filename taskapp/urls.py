from django.urls import path

from taskapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signin',views.signin_fun,name='signin'),
    path('login',views.login_fun,name='login'),
    path('display/',views.display_fun,name='display'),
    path('addtask/',views.add_fun,name='addtask'),
    path('update_task/<int:id>/',views.update_fun,name='update_task'),
    path('delete_task/<int:id>/',views.delete_fun,name='delete_task'),
    path('logout/',views.log_fun),

]


