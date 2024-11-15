from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from student_management_system import views,Staff_views,Student_views

urlpatterns = [

   #  Staff Url  
   path('Home',Staff_views.HOME, name="staff_home"),
   path('Notification',Staff_views.Notification, name="notificaion"),
   path('Mark-As-Done/<str:status>',Staff_views.Staff_Notification_Mark_As_Done, name="staff_notifcaion_mark_as_done"),

   
   path('Apply-Leave',Staff_views.Staff_Apply_Leave, name="staff_apply_leave"),
   path('Apply-Leave/Save',Staff_views.Staff_Apply_Leave_Save, name="staff_apply_leave_save"),
   path('Feedback',Staff_views.Staff_feedback, name="staff_feedback"),
   path('Feedback/Save',Staff_views.Staff_Feedback_Save, name="staff_feedback_save"),




   path('Take/Attendance',Staff_views.Staff_Take_Attendance, name="staff_take_attendance"),
   path('Save/Attendance',Staff_views.Staff_Save_Attendance, name="staff_save_attendance"),
   path('View/Attendance',Staff_views.Staff_View_Attendance, name="staff_view_attendance"),
   path('Add/Result',Staff_views.Staff_Add_Result, name="staff_add_result"),
   path('Save/Result',Staff_views.Staff_Save_Result, name="staff_save_result"),




] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

