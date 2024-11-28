from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path
from collegemng import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='Home-page'),
    path('register/',views.TeachersignupView,name='Register-page'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('Teacher-Dashboard/',views.TeacherDashboard,name='Teacher-Dashboard'),
    path('logout/',views.logout_view,name='Logout'),
    path('addstudent/',views.Addstudent,name='Student-Details'),
    path('viewstudent<int:id>/',views.Viewstudent,name='ViewStudent'),
    path('updatestudent<int:student_id>/',views.Updatestudent,name='UpdateStudent'),
    path('deletestudent<int:id>/',views.Deletestudent,name='DeleteStudent'),
    path('studentlogin/',views.Studentloginview,name='Studentlogin'),
    path('student-profile/<int:student_id>/', views.StudentProfileView, name='Student-Profile'),
    path('updateprofile/<int:student_id>',views.studentupdateview,name='Update-profile'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)