# This file contains all the serializers for the models in the database
# Serializers convert complex data such as querysets and model instances into native Python datatypes
# that can then be easily rendered into JSON or XML
# To use a serializer, you need to create an instance of the serializer and call is_valid() to validate the data,
# then call save() to save the validated data to the database
# The fields argument is a dictionary mapping field names to serializer fields
# The Meta class is used to associate the serializer with the model and list the fields that should be included in the serializer
from rest_framework import serializers
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

class UserSerializer(serializers.ModelSerializer):
    # This serializer is for the User model
    class Meta:
        model = User
        fields = '__all__'  # Automatically includes all fields in the User model

class SchoolSerializer(serializers.ModelSerializer):
    # This serializer is for the School model
    class Meta:
        model = School
        fields = '__all__'  # Automatically includes all fields in the School model

class ParentStudentLinkSerializer(serializers.ModelSerializer):
    # This serializer is for the ParentStudentLink model
    # It includes the parent and student fields
    parent = serializers.PrimaryKeyRelatedField(queryset=Parent.objects.all())  # Parent reference
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())  # Student reference

    class Meta:
        model = ParentStudentLink
        fields = '__all__'

    def create(self, validated_data):
        return ParentStudentLink.objects.create(**validated_data)

class StudentSerializer(serializers.ModelSerializer):
    # This serializer is for the Student model
    # It includes the user field and the parents field
    user = UserSerializer()  # Embedding the User serializer
    parents = ParentStudentLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'  # Automatically includes all fields in the Student model

    def create(self, validated_data):
        user_data = validated_data.pop('user')  # Extract the user data
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)  # Create the user instance
        student = Student.objects.create(user=user, **validated_data)  # Create the student instance and associate with user
        return student

class ParentSerializer(serializers.ModelSerializer):
    # This serializer is for the Parent model
    # It includes the user field and the students field
    user = UserSerializer()  # Embedding the User serializer for Parent
    students = ParentStudentLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Parent
        fields = '__all__'  # Automatically includes all fields in the Parent model

    def create(self, validated_data):
        user_data = validated_data.pop('user')  # Extract the user data
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)  # Create the user instance
        parent = Parent.objects.create(user=user, **validated_data)  # Create the parent instance
        return parent

class TeacherSerializer(serializers.ModelSerializer):
    # This serializer is for the Teacher model
    # It includes the user field
    user = UserSerializer()  # Embedding the User serializer for Teacher

    class Meta:
        model = Teacher
        fields = '__all__'  # Automatically includes all fields in the Teacher model

    def create(self, validated_data):
        user_data = validated_data.pop('user')  # Extract the user data
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)  # Create the user instance
        teacher = Teacher.objects.create(user=user, **validated_data)  # Create the teacher instance
        return teacher

class ClassSerializer(serializers.ModelSerializer):
    # This serializer is for the Class model
    class Meta:
        model = Class
        fields = '__all__'  # Automatically includes all fields in the Class model

class SubjectSerializer(serializers.ModelSerializer):
    # This serializer is for the Subject model
    class Meta:
        model = Subject
        fields = '__all__'  # Automatically includes all fields in the Subject model

class PaymentSerializer(serializers.ModelSerializer):
    # This serializer is for the FeePayment model
    class Meta:
        model = FeePayment
        fields = '__all__'  # Automatically includes all fields in the FeePayment model

class AnnouncementSerializer(serializers.ModelSerializer):
    # This serializer is for the Announcement model
    class Meta:
        model = Announcement
        fields = '__all__'  # Automatically includes all fields in the Announcement model

# AdminUser Serializer (For Admin User)
class AdminUserSerializer(serializers.ModelSerializer):
    # This serializer is for the User model for Admin Users
    class Meta:
        model = User
        fields = '__all__'  # Automatically includes all fields in the User model
        extra_kwargs = {
            'password': {'write_only': True},  # Ensures password is write-only
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)  # Hash the password before saving
        user.save()
        return user

