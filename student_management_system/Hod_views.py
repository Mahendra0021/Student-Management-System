from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from APP.models import Course,Session_Year,Student,CustomUser,Staff,Subject,Staff_Notification,Staff_leave,Staff_Feedback,Student_Notification,Student_Feedback,Student_leave,Attendance,Attendance_Report
from django.contrib import messages
@login_required(login_url='/')
def Home(request):
  student_count = Student.objects.all().count()
  staff_count = Staff.objects.all().count()
  course_count = Course.objects.all().count()
  subject_count = Subject.objects.all().count()
  student_gender_male = Student.objects.filter(gender = 'Male').count()
  student_gender_female = Student.objects.filter(gender = 'Female').count()
  print(student_gender_male,student_gender_female)
  context = {
     'student_count':student_count,
     'staff_count':staff_count,
     'course_count':course_count,
     'subject_count':subject_count,
     'student_gender_male':student_gender_male,
     'student_gender_female':student_gender_female
  }
  return render(request,'Hodii/Home.html', context)

@login_required(login_url='/')
def Student_Add(request):
  course = Course.objects.all()
  session_year = Session_Year.objects.all()
  # print(course)
  # print(session_year)
  if request.method == "POST":
    profile_pic = request.FILES.get('profile_pic')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    address = request.POST.get('address')
    gender = request.POST.get('gender')
    course_id = request.POST.get('course_id')
    session_year_id = request.POST.get('session_year_id')
    print(profile_pic, first_name, last_name, email,username,password, address, gender, course_id, session_year_id)

    if CustomUser.objects.filter(email=email).exists():
      messages.warning(request, 'Email is already Add')
      return redirect('student_add')
    if CustomUser.objects.filter(username=username).exists():
      messages.warning(request, 'Username is already Add')
      return redirect('student_add')
    else:
      user = CustomUser(
        first_name = first_name, last_name = last_name, username = username, email = email, profile_pic =   profile_pic, user_type = 3  
      )
      user.set_password(password)
      user.save()
      course = Course.objects.get(id = course_id)
      session_year = Session_Year.objects.get(id = session_year_id)

      student = Student(
        admin = user,
        address = address,
        session_year_id = session_year,
        course_id = course,
        gender = gender,
      )
      student.save()
      messages.success(request, user.first_name + "  " + user.last_name + ' Are SuccessFull Add !')
      return redirect('student_add')

      
  context = {
    'course':course,
    'session_year':session_year
  }
  return render(request, "Hodii/add_student.html", context)



@login_required(login_url='/')
def View_Student(request):
  student = Student.objects.all()
  print(student)
  context = {
    'student':student
  }
  return render(request, 'Hodii/view_student.html',context)

@login_required(login_url='/')
def Edit_Student(request,id):
  student = Student.objects.filter(id=id)
  course = Course.objects.all()
  session_year = Session_Year.objects.all()
  context = {
    'student':student,
    'course':course,
    'session_year':session_year
  }
  return render(request, 'Hodii/edit_student.html',context)


@login_required(login_url='/')
def Update_Student(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        # Fetch the CustomUser instance
        user = CustomUser.objects.get(id=student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        # Check if password needs to be updated
        if password and password != "":
            user.set_password(password)

        # Check if profile picture needs to be updated
        if profile_pic:
            user.profile_pic = profile_pic

        user.save() 

        # Fetch the Student instance
        student = Student.objects.get(admin=student_id)
        student.address = address
        student.gender = gender

        # Fetch the course and session year based on provided IDs
        course = Course.objects.get(id=course_id)
        student.course_id = course

        session_year = Session_Year.objects.get(id=session_year_id)
        student.session_year_id = session_year

        student.save() 
        messages.success(request, "Record Successfully Updated!")
        return redirect('view_student')

    return render(request, 'Hodii/edit_student.html')


@login_required(login_url='/')
def Delete_Student(request, admin):
    try:
        student = CustomUser.objects.get(id=admin)
        
        # Delete related Student record(s) first
        Student.objects.filter(admin=student).delete()
        
        # Now delete the CustomUser
        student.delete()
        messages.success(request, "Record Successfully Deleted!")
    except CustomUser.DoesNotExist:
        messages.error(request, "Student does not exist.")
    except Exception as e:
        messages.error(request, f"Error: {e}")
    
    return redirect('view_student')




############ Staff Query set ###########
@login_required(login_url='/')
def Staff_Add(request):
   if request.method == "POST":
    profile_pic = request.FILES.get('profile_pic')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    address = request.POST.get('address')
    gender = request.POST.get('gender')
    # print(profile_pic, first_name, last_name, email,username,password, address, gender)

    if CustomUser.objects.filter(email=email).exists():
      messages.warning(request, 'Email is already Add !')
      return redirect('add_staff')
    
    else:
      user = CustomUser(
        first_name = first_name, last_name = last_name, username = username, email = email, profile_pic =   profile_pic, user_type = 2
      )
      user.set_password(password)
      user.save()
      student = Staff(
        admin = user,
        address = address,
        gender = gender,
      )
      student.save()
      messages.success(request, user.first_name + "  " + user.last_name + ' Are Successfully Added !')
      return redirect('add_staff')

   return render(request, "Hodii/add_staff.html")


@login_required(login_url='/')
def View_Staff(request):
   staff = Staff.objects.all()
   print(staff)
   context = {
    'staff':staff
   }
   return render(request, 'Hodii/view_staff.html',context)


@login_required(login_url='/')
def Edit_Staff(request,id):
  staff = Staff.objects.filter(id=id)
  context = { 'staff':staff}
  return render(request, 'Hodii/edit_staff.html',context)

@login_required(login_url='/')
def Update_Staff(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        # Fetch the CustomUser instance
        user = CustomUser.objects.get(id=staff_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        # Check if password needs to be updated
        if password and password != "":
            user.set_password(password)

        # Check if profile picture needs to be updated
        if profile_pic:
            user.profile_pic = profile_pic

        user.save() 

        # Fetch the Student instance
        staff = Staff.objects.get(admin=staff_id)
        staff.address = address
        staff.gender = gender

       

        staff.save() 
        messages.success(request, "Record Successfully Updated!")
        return redirect('view_staff')

    return render(request, 'Hodii/edit_staff.html')


@login_required(login_url='/')
def Delete_Staff(request,admin):
   staff = Staff.objects.get(id=admin)
   staff.delete()
   messages.success(request, "Record Successfully Deleted!")
   return redirect('view_staff')



########## Course #############
@login_required(login_url='/')
def Add_Course(request):
   if request.method == "POST":
      course_name = request.POST.get('course_name')
      # print(course_name)
      course = Course(name=course_name)
      course.save()
      messages.success(request, "Course Are Successfully Created !")
      return redirect('add_course')
   return render(request, "Hodii/add_course.html")

@login_required(login_url='/')
def View_Course(request):
   course = Course.objects.all()
   context = {
      'course':course
   }
   return render(request, "Hodii/view_course.html",context)

@login_required(login_url='/')
def Edit_Course(request,id):
   course = Course.objects.get(id = id)
   context = {
      'course':course
   }
   return render(request, 'Hodii/edit_course.html',context)

@login_required(login_url='/')
def Update_Course(request):
    if request.method == "POST":
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')
        print(name,course_id)
        course = Course.objects.get(id = course_id)
        course.name = name
        course.save()
        messages.success(request, "Record Successfully Updated!")
        return redirect('view_course')

    return render(request, 'Hodii/edit_course.html')


@login_required(login_url='/')
def Delete_Course(request,id):
   course = Course.objects.get(id =id)
   course.delete()
   messages.success(request, "Record Successfully Deleted !")
   return redirect('view_course')





############# Subject Query set ############
@login_required(login_url='/')
def Add_Subject(request):
    course_list = Course.objects.all()  # To avoid overwriting the variable 'course'
    staff_list = Staff.objects.all()
    
    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')  # Get course ID from the form
        staff_id = request.POST.get('staff_id')    # Get staff ID from the form
        
        # Fetch the actual Course and Staff instances using their IDs
        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        # Now pass the actual Course and Staff instances when creating Subject
        subject = Subject(name=subject_name, course=course, staff=staff)
        subject.save()

        messages.success(request, "Subject successfully added!")
        return redirect('add_subject')

    context = {
        'course': course_list,
        'staff': staff_list
    }
    return render(request, "Hodii/add_subject.html", context)



@login_required(login_url='/')
def View_Subject(request):
    subject = Subject.objects.all()
    context = {
      'subject':subject
    }
    return render(request, "Hodii/view_subject.html",context)


@login_required(login_url='/')
def Edit_Subject(request,id):
   subject = Subject.objects.get(id = id)
   course = Course.objects.all()
   staff = Staff.objects.all()
   context = {
      'subject':subject,
      'course':course,
      'staff':staff
   }
   return render(request, 'Hodii/edit_subject.html',context)

@login_required(login_url='/')
def Update_Subject(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')
        # print(subject_id,subject_name,course_id,staff_id)
        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)
        subject = Subject(
           id = subject_id,name = subject_name,course= course, staff =staff
        )
        subject.save()
        messages.success(request, "Record Successfully Updated!")
        return redirect('view_subject')

    return render(request, 'Hodii/edit_subject.html')


def Delete_Subject(request,id):
   subject = Subject.objects.get(id = id)
   subject.delete()
   messages.success(request, "Record Successfully Deleted !")
   return redirect('view_subject')




################## Session Query Set #################

def Add_Session(request):
   if request.method == "POST":
      session_year_start = request.POST.get('session_year_start')
      session_year_end = request.POST.get('session_year_end')
      session = Session_Year(
         session_start = session_year_start,
         session_end = session_year_end
         )
      session.save()
      messages.success(request, "Session successfully added!")
      return redirect('add_session')
   return render(request, "Hodii/add_session.html")


def View_Session(request):
   session = Session_Year.objects.all()
   context = {
      'session':session
   }
   return render(request, "Hodii/view_session.html",context)




@login_required(login_url='/')
def Edit_Session(request, id):
    session_year = Session_Year.objects.get(id=id)  # Fetch single instance of Session_Year
    
    context = {
        'session_year': session_year,  # Pass the single session object
    }
    
    return render(request, 'Hodii/edit_session.html', context)

@login_required(login_url='/')
def Update_Session(request):
    if request.method == "POST":
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')
        
     
        session = Session_Year(
           id = session_id,session_start = session_year_start,session_end= session_year_end
        )
        session.save()
        messages.success(request, "Record Successfully Updated!")
        return redirect('view_session')

    return render(request, 'Hodii/edit_session.html')

def Delete_Session(request,id):
   session = Session_Year.objects.get(id=id)
   session.delete()
   
   messages.success(request, "Record Successfully Deleted !")
   return redirect('view_session')



def Send_Notificaion(request):
  staff_data = Staff.objects.all()
  seen_notificaion = Staff_Notification.objects.all().order_by('-id')
  context = {
     'staff_data':staff_data,
     'seen_notificaion': seen_notificaion
  }
   
  return render(request, 'Hodii/staff_notificaion.html',context)

def Save_Staff_Notificaion(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')  # get the staff_id from the form
        message = request.POST.get('message')    # get the message from the form

        # Retrieve the Staff instance
        staff = Staff.objects.get(admin=staff_id)

        # Now create the notification
        notification = Staff_Notification(
            staff_id=staff,  # Use 'staff_id' as it's the ForeignKey field in your model
            message=message
        )
        notification.save()
        messages.success(request,"Notificaion Successfully Send!")
        return redirect('send_notificaion')





def Staff_Leave_View(request):
   staff_leave = Staff_leave.objects.all()
   context = {
    'staff_leave':staff_leave
   }
   return render(request,'Hodii/staff_leave.html',context)


def Staff_Approve_Leave(request,id):
   leave = Staff_leave.objects.get(id=id)
   leave.status = 1
   leave.save()
   messages.success(request,"Approve Sent !")
   return redirect('staff_leave_view')


def Staff_DisApprove_Leave(request,id):
   leave = Staff_leave.objects.get(id=id)
   leave.status = 2
   leave.save()
   messages.success(request,"Dis-Approve Sent !")
   return redirect('staff_leave_view')





def Student_Leave_View(request):
   student_leave = Student_leave.objects.all()
   context = {
    'student_leave':student_leave
   }
   return render(request,'Hodii/student_leave.html',context)




def Student_Approve_Leave(request,id):
   leave = Student_leave.objects.get(id=id)
   leave.status = 1
   leave.save()
   messages.success(request,"Approve Sent !")
   return redirect('student_leave_view')


def Student_DisApprove_Leave(request,id):
   leave = Student_leave.objects.get(id=id)
   leave.status = 2
   leave.save()
   messages.success(request,"Dis-Approve Sent !")
   return redirect('student_leave_view')







def Hodi_Staff_Feedback(request):
   feedback = Staff_Feedback.objects.all()
   feedback_history = Student_Feedback.objects.all().order_by('id')
   context = {
      'feedback':feedback,
      'feedback_history':feedback_history
   }
   return render(request,'Hodii/hod_staff_feedback.html',context)



def Hodi_Staff_Feedback_Save(request):
   if request.method == "POST":
      feedback_id = request.POST.get('feedback_id')
      feedback_reply = request.POST.get('feedback_reply')
      feedback = Staff_Feedback.objects.get(id = feedback_id)
      feedback.feedback_reply = feedback_reply
      feedback.status = 1
      feedback.save()
      messages.success(request, "Feedback-Reply Sent!")
      return  redirect('hod_staff_feedback')


def Student_Notificaion(request):
    student = Student.objects.all()
    notificaion = Student_Notification.objects.all().order_by('-id')
    context = {
      'student':student,
      'notificaion': notificaion
    }
    
    return render(request, 'Hodii/student_notificaion.html',context)




def Save_Student_Notificaion(request):
    if request.method == "POST":
        message = request.POST.get('message')
        student_id = request.POST.get('student_id')  
         

        student = Student.objects.get(admin=student_id)

        Stud_notification = Student_Notification(
            student_id=student,  
            message=message
        )
        Stud_notification.save()
        messages.success(request,"Notificaion Successfully Send!")
        return redirect('student_notificaion')





def Hodi_Student_Feedback(request):
   feedback = Student_Feedback.objects.all()
   feedback_history = Student_Feedback.objects.all().order_by('id')
   context = {
      'feedback':feedback,
      'feedback_history':feedback_history
   }
   return render(request,'Hodii/hod_student_feedback.html',context)



def Hodi_Student_Feedback_Save(request):
   if request.method == "POST":
      feedback_id = request.POST.get('feedback_id')
      feedback_reply = request.POST.get('feedback_reply')
      feedback = Student_Feedback.objects.get(id = feedback_id)
      feedback.feedback_reply = feedback_reply
      feedback.status = 1
      feedback.save()
      messages.success(request, "Feedback-Reply Sent!")
      return  redirect('hod_staff_feedback')



def View_Attendance(request):
   
    subject = Subject.objects.all()
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')
    
    get_subject = None
    get_session_year = None
    attendance_date = None
    attendance_report = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')

            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)
            
         
            attendance = Attendance.objects.filter(
                subject_id=get_subject, attendance_date=attendance_date
            )
            for i in attendance:
               attendance_id = i.id
               attendance_report = Attendance_Report.objects.filter(
                  attendance_id = attendance_id,
                  student_id = request.user.id
                  )
                       
           

    context = {
        'subject': subject,
        'session_year': session_year,
        'action': action,
        'get_subject': get_subject,
        'get_session_year': get_session_year,
        'attendance_date': attendance_date,
        'attendance_report': attendance_report,
    }
    return render(request, "Hodii/view_attendance.html",context)