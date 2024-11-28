from django.shortcuts import render,redirect,get_object_or_404
from . models import Student
from django.contrib import messages
from . forms import TeacherSignup,TeacherLogin,StudentDetails
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def Home(request):
    return render(request,'home.html')
def TeachersignupView(request):
    if request.method == 'POST':
        form = TeacherSignup(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('Teacher-Login')  # Redirect to login page or wherever you want
        else:
            # If the form is not valid, re-render the form with error messages
            return render(request, 'register.html', {'form': form})
    else:
        # If the request is GET, show the empty form
        form = TeacherSignup()
        return render(request, 'register.html', {'form': form})
@login_required
def TeacherLoginView(request):
    if request.method == 'POST':
        form = TeacherLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']  
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('Teacher-Dashboard')
            else:
                return render(request, 'login.html', {'form': form})  
    else:
        form = TeacherLogin()
    return render(request, 'login.html', {'form': form})  # Always return a response  # Return the empty form initially
       
@login_required
def TeacherDashboard(request):
    students = Student.objects.filter(teacher=request.user)  # Only show students for the logged-in teacher
    return render(request, 'dashboard.html', {'students': students})

@login_required
def Addstudent(request):
    if request.method == 'POST':
        form = StudentDetails(request.POST,request.FILES)
        if form.is_valid():
            student = form.save()
            student.teacher = request.user
            student.save()
            return redirect('Teacher-Dashboard')
    else:
        form = StudentDetails()
        return render(request,'addstudent.html',{'form':form})
@login_required
def Viewstudent(request,id):
    student = get_object_or_404(Student,id=id)
    return render(request,'view-student.html',{'student':student})

@login_required
def Updatestudent(request,student_id):
    student = get_object_or_404(Student,id=student_id)
    if request.method == 'POST':
        form = StudentDetails(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('Teacher-Dashboard')
    else:
        form = StudentDetails(instance=student)
    return render(request,'updatestudent.html',{'form':form,'student':student})

@login_required
def Deletestudent(request,id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('Teacher-Dashboard')
    return render (request,'confirmation.html',{'student':student})

def logout_view(request):
    logout(request)
    return redirect('Home-page')

def Studentloginview(request):
    if request.method == 'POST':
        register_number = request.POST.get('register_number')
        try:
            # Fetch the student with the provided register number
            student = Student.objects.get(register_number=register_number)
            return redirect('Student-Profile', student_id=student.id)  # Redirect to the profile page
        except Student.DoesNotExist:
            messages.error(request, 'Invalid Register Number.')
    return render(request, 'studentlogin.html')

def StudentProfileView(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'studentprofileview.html', {'student': student})

def studentupdateview(request,student_id):
    student = get_object_or_404(Student,id=student_id)
    if request.method == 'POST':
        form = StudentDetails(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('Student-Profile', student_id=student.id)
    else:
        form = StudentDetails(instance=student)
    return render(request,'studentupdateprofile.html',{'form':form,'student':student})



