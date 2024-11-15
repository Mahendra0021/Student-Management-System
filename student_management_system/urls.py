"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views,Hod_views,Staff_views,Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('base/', views.BASE, name='base'), 

   # Login Path
    path('', views.Login, name='login'), 
    path('doLogin', views.doLogin, name='doLogin'),  
    path('doLogout', views.doLogout, name='logout'),  

  # Profile Update Path
    path('profile', views.Profile, name="profile"),
    path('profile/update', views.Profile_update, name="profile_update"),

   # HOD Panel Url
    path('HOD/Home', Hod_views.Home, name='hod_home'),
    path('HOD/Student/Add', Hod_views.Student_Add, name='student_add'),
    path('HOD/Student/View', Hod_views.View_Student, name='view_student'),
    path('HOD/Student/Edit/<str:id>', Hod_views.Edit_Student, name='edit_student'),
    path('HOD/Student/Update', Hod_views.Update_Student, name='update_student'),
    path('HOD/Student/Delete/<str:admin>', Hod_views.Delete_Student, name='delete_student'),


    # Staff Url

    path('HOD/Staff/Add', Hod_views.Staff_Add, name='add_staff'),
    path('HOD/Staff/View', Hod_views.View_Staff, name='view_staff'),  
    path('HOD/Staff/Edit/<str:id>', Hod_views.Edit_Staff, name='edit_staff'),
    path('HOD/Staff/Update', Hod_views.Update_Staff, name='update_staff'),
    path('HOD/Staff/Delete/<str:admin>', Hod_views.Delete_Staff, name='delete_staff'),






    # Course Url

    path('HOD/Course/Add', Hod_views.Add_Course, name='add_course'),
    path('HOD/Course/View', Hod_views.View_Course, name='view_course'),
    path('HOD/Course/Edit/<str:id>', Hod_views.Edit_Course, name='edit_course'),
    path('HOD/Course/Update', Hod_views.Update_Course, name='update_course'),
    path('HOD/Course/Delete/<str:id>', Hod_views.Delete_Course, name='delete_course'),



   # Subjects Url
    path('HOD/Subject/Add', Hod_views.Add_Subject, name='add_subject'),
    path('HOD/Subject/View', Hod_views.View_Subject, name='view_subject'),
    path('HOD/Subject/Edit/<str:id>', Hod_views.Edit_Subject, name='edit_subject'),
    path('HOD/Subject/Update', Hod_views.Update_Subject, name='update_subject'),
    path('HOD/Subject/Delete/<str:id>', Hod_views.Delete_Subject, name='delete_subject'),



  # Session Url
    path('HOD/Session/Add', Hod_views.Add_Session, name='add_session'),
    path('HOD/Session/View', Hod_views.View_Session, name='view_session'),
    path('HOD/Session/Edit/<str:id>', Hod_views.Edit_Session, name='edit_session'),
    path('HOD/Session/Update', Hod_views.Update_Session, name='update_session'),
    path('HOD/Session/Delete/<str:id>', Hod_views.Delete_Session, name='delete_session'),



    # Staff Send Notification

    path('HOD/Staff/Send-Notificaion', Hod_views.Send_Notificaion, name='send_notificaion'),
    path('HOD/Staff/Save-Notificaion', Hod_views.Save_Staff_Notificaion, name='save_staff_notificaion'),


    # Student Send Notification
    path('HOD/Student/Send-Notificaion', Hod_views.Student_Notificaion, name='student_notificaion'),
    path('HOD/Student/Save-Notificaion', Hod_views.Save_Student_Notificaion, name='save_student_notificaion'),



  # Staff Leave Urls
    path('HOD/Staff/Leave-View', Hod_views.Staff_Leave_View, name='staff_leave_view'),
    path('HOD/Staff/Approve-Leave/<str:id>', Hod_views.Staff_Approve_Leave, name='staff_approve_leave'),
    path('HOD/Staff/DisApprove-Leave/<str:id>', Hod_views.Staff_DisApprove_Leave, name='staff_disapprove_leave'),


  # Student Leave Urls
    
    path('HOD/Student/Leave-View', Hod_views.Student_Leave_View, name='student_leave_view'),
    path('HOD/Student/Approve-Leave/<str:id>', Hod_views.Student_Approve_Leave, name='student_approve_leave'),
    path('HOD/Student/DisApprove-Leave/<str:id>', Hod_views.Student_DisApprove_Leave, name='student_disapprove_leave'),
 
 




  # Staff Feedback

    path('HOD/Staff/Feedback', Hod_views.Hodi_Staff_Feedback, name='hod_staff_feedback'),
    path('HOD/Staff/Feedback/Save', Hod_views.Hodi_Staff_Feedback_Save, name='hod_staff_feedback_save'),



    # Student Feedback

    path('HOD/Student/Feedback', Hod_views.Hodi_Student_Feedback, name='hod_student_feedback'),
    path('HOD/Student/Feedback/Save', Hod_views.Hodi_Student_Feedback_Save,name='hod_student_feedback_save'),

    path('HOD/View/Attendance',Hod_views.View_Attendance, name="view_attendance"),

    
 




  # this is Staff urls
    path('Staff/',include('APP.urls')),

    # this is Student urls
    path('Student/',include('APP.student_urls')),



] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

