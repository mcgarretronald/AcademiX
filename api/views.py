from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions  # Import for permission handling
from users.models import User
from school.models import School
from student.models import Student
from parent.models import Parent
from teacher.models import Teacher
from classes.models import Class
from subjects.models import Subject
from feepayments.models import FeePayment
from announcements.models import Announcement
from parentstudentlink.models import ParentStudentLink
from .serializers import (
    UserSerializer, SchoolSerializer, StudentSerializer, ParentSerializer, 
    TeacherSerializer, ClassSerializer, SubjectSerializer, PaymentSerializer, 
    AnnouncementSerializer, AdminUserSerializer, ParentStudentLinkSerializer
)

class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(role='admin')
    serializer_class = AdminUserSerializer

    # Uncomment to restrict admin creation
    # def get_permissions(self):
    #     if self.action == 'create':
    #         self.permission_classes = [permissions.IsAdminUser]
    #     return super().get_permissions()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a user along with their specific role (student, teacher, etc.)
        """
        role = request.data.get('role')
        if role not in ['student', 'teacher', 'parent']:
            return Response({"detail": "Invalid role."}, status=400)

        # Check if password is provided
        password = request.data.get('password')
        if not password:
            return Response({"detail": "Password is required."}, status=400)

        # Call super().create() to create the user
        response = super().create(request, *args, **kwargs)

        # Depending on the role, create the respective model instance (Student, Teacher, Parent, etc.)
        if role == 'student':
            Student.objects.create(user=response.data, school=request.data.get('school'), admission_number=request.data.get('admission_number'), class_name=request.data.get('class_name'))
        elif role == 'teacher':
            Teacher.objects.create(user=response.data, school=request.data.get('school'))
        elif role == 'parent':
            Parent.objects.create(user=response.data)

        return response

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=['get'])
    def parents(self, request, student_id=None):
        student = Student.objects.get(id=student_id)
        parents = student.parents.all()
        serializer = ParentSerializer(parents, many=True)
        return Response(serializer.data)

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    # Custom action to fetch students for a given parent
    @action(detail=True, methods=['get'], url_path='students')
    def get_students(self, request, pk=None):
        parent = self.get_object()  # Get the parent instance using the pk from the URL
        # Query for all students associated with the parent through ParentStudentLink
        students = Student.objects.filter(parentstudentlink__parent=parent)
        student_serializer = StudentSerializer(students, many=True)
        return Response(student_serializer.data)
    
    
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = FeePayment.objects.all()
    serializer_class = PaymentSerializer

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    
    
class ParentStudentLinkViewSet(viewsets.ModelViewSet):
    queryset = ParentStudentLink.objects.all()
    serializer_class = ParentStudentLinkSerializer

    @action(detail=True, methods=['get'])
    def parents(self, request, student_id=None):
        student = Student.objects.get(id=student_id)
        links = ParentStudentLink.objects.filter(student=student)
        parents = [link.parent for link in links]
        serializer = ParentSerializer(parents, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def students(self, request, parent_id=None):
        parent = Parent.objects.get(id=parent_id)
        links = ParentStudentLink.objects.filter(parent=parent)
        students = [link.student for link in links]
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)