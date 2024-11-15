from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from APP.models import Student,Student_Notification,Student_Feedback,Student_leave,Subject,Attendance,Attendance_Report,StudentResult
from django.contrib import messages

def Student_Home(request):
  return render(request, "Student/home.html")


def STUDENT_NOTIFICAION(request):
   student = Student.objects.filter(admin = request.user.id)
   for i in student:
     student_id = i.id
     student_notification = Student_Notification.objects.filter(student_id=student_id)
     context = {
      'student_notification':student_notification
     }
     return render(request, "Student/student_notificaion.html",context)



def STUDENT_Notification_Mark_As_Done(request,status):
  student_notification = Student_Notification.objects.get(id = status )
  student_notification.status = 1
  student_notification.save()
  return redirect('student__notificaion')





def STUDENT_FEEDBACK(request):
   student_id = Student.objects.get(admin = request.user.id)
   feedback_history = Student_Feedback.objects.filter(student_id=student_id)
   context = {
      'feedback_history':feedback_history
   }

   return render(request, "Student/feedback.html",context)


def Student_Feedback_Save(request):
    if request.method == "POST":
        feedback_text = request.POST.get('feedback_text')  
        student = Student.objects.get(admin=request.user.id)

    
        feedback_instance = Student_Feedback(
            student_id=student,
            feedback=feedback_text,
            feedback_reply="",  
        )
        feedback_instance.save()
        messages.success(request,"Successfully Sent!")
        return redirect('student__feedback')





def Student_Apply_Leave(request):
  student = Student.objects.filter(admin = request.user.id)
  for i in student:
    student_id = i.id
    student_leave_history = Student_leave.objects.filter(student_id=student_id)
    context = {
      'student_leave_history':student_leave_history
    }
  return render(request, 'Student/student_apply_leave.html',context)



def Student_Apply_Leave_Save(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        student = Student.objects.get(admin=request.user.id)

        leave = Student_leave(
            student_id=student,
            data=leave_date, 
            message=leave_message
        )
        leave.save()

        messages.success(request, "Successfully sent leave")
        return redirect('student_apply_leave')



def Student_View_Attendance(request):
   student = Student.objects.get(admin = request.user.id)
   subjects = Subject.objects.filter(course = student.course_id)
   action = request.GET.get('action')
   get_subject = None
   if action is not None:
      if request.method == "POST":
         subject_id = request.POST.get('subject_id')
         get_subject = Subject.objects.get(id = subject_id)
         attendance = Attendance.objects.get(subject_id = get_subject)
        
         attendance_report = Attendance_Report.objects.filter(student_id = student,attendance_id__subject_id = subject_id)
                  
               

   context = {
      'subjects':subjects, 'action':action, 'get_subject':get_subject,'attendance_report':attendance_report
   }
   return render(request, "Student/view_attendance.html",context)



def Student_View_Result(request):
   mark = None
   student = Student.objects.get(admin = request.user.id)
   print(student)
   result = StudentResult.objects.filter(student_id = student)
   for i in result:
      assignment_mark = i.assignment_mark
      exam_mark = i.exam_mark
      mark = assignment_mark + exam_mark
   context = {
      'result':result, "mark":mark
   }
   return render(request, "Student/view_result.html",context)