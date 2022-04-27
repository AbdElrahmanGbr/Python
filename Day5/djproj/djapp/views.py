from django.shortcuts import redirect, render
from .models import Student,Track
from .forms import StudentForm,TrackForm

#rest_framework imports.
from .serializers import StudentSerializer,TrackSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

#rest_framework views.
@api_view(['GET'])
def api_all_student(request):
    all_students = Student.objects.all()
    student_serializer = StudentSerializer(all_students, many = True) 
    return Response(student_serializer.data)

@api_view(['GET'])
def api_one_student(request,st_id):
    student = Student.objects.get(id=st_id)
    student_serializer = StudentSerializer(student, many = False) 
    return Response(student_serializer.data)

@api_view(['POST'])
def api_add_student(request):
    student_serializer = StudentSerializer(data = request.data)
    if student_serializer.is_valid():
        student_serializer.save()
        return redirect('api-all')

@api_view(['POST'])
def api_edit_student(request,st_id):
    student = Student.objects.get(id = st_id)
    student_serializer = StudentSerializer(data=request.data , instance=student)
    if student_serializer.is_valid():
        student_serializer.save()
        return redirect('api-all')

@api_view(['DELETE'])
def api_delete_student(request,st_id):
    student = Student.objects.get(id = st_id)
    student.delete()
    return Response('Student is deleted!!')









# Create your views here.

def home(request):
    all_students = Student.objects.all()
    context = {'student_list':all_students}
    return render(request,'djapp/home.html',context)

def show(request,st_id):
    student = Student.objects.get(id=st_id)
    context = {'student':student}
    return render(request,'djapp/show.html',context)

def delete(request,st_id):
    student = Student.objects.get(id=st_id)
    student.delete()
    return redirect('home')

def addStudent(request):
    st_form = StudentForm()
    if request.method == 'POST':
        st_form = StudentForm(request.POST)
        if st_form.is_valid:
            st_form.save()
            return redirect('home')
    context = {'st_form': st_form}
    return render(request,'djapp/add.html',context)

def editStudent(request,st_id):
    st = Student.objects.get(id=st_id)
    st_form = StudentForm(instance=st)
    if request.method == 'POST':
        st_form = StudentForm(request.POST,instance=st )
        if st_form.is_valid:
            st_form.save()
            return redirect('home')
    context = {'st_form': st_form}
    return render(request,'djapp/add.html',context)



   