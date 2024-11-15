from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from student_management_system import views,Staff_views,Student_views

urlpatterns = [

   #  Student Url  

   path('Home',Student_views.Student_Home, name="student_home"),
   path('Notification',Student_views.STUDENT_NOTIFICAION, name="student__notificaion"),
   path('Mark-As-Done/<str:status>',Student_views.STUDENT_Notification_Mark_As_Done, name="student_notifcaion_mark_as_done"),
   path('Feedback', Student_views.STUDENT_FEEDBACK, name="student__feedback"),
   path('Feedback/Save', Student_views.Student_Feedback_Save, name="student_feedback_save"),




   path('Apply-Leave',Student_views.Student_Apply_Leave, name="student_apply_leave"),
   path('Apply-Leave/Save',Student_views.Student_Apply_Leave_Save, name="student_apply_leave_save"),


   path('View/Attendance',Student_views.Student_View_Attendance, name="student_view_attendance"),
   path('View/Result',Student_views.Student_View_Result, name="student_view_result"),

  
   
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

