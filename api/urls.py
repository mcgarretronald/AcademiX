from django.urls import path
from .views import (
    AdminUserViewSet, UserViewSet, SchoolViewSet, StudentViewSet, ParentViewSet,
    TeacherViewSet, ClassViewSet, SubjectViewSet, PaymentViewSet, AnnouncementViewSet,
    ParentStudentLinkViewSet  # Make sure to import your new viewset
)

urlpatterns = [
    # Admin Users
    path('admin-users/', AdminUserViewSet.as_view({'get': 'list'}), name='admin-user-list'),
    path('admin-users/<int:pk>/', AdminUserViewSet.as_view({'get': 'retrieve'}), name='admin-user-detail'),
    path('admin-users/create/', AdminUserViewSet.as_view({'post': 'create'}), name='admin-user-create'),
    path('admin-users/<int:pk>/update/', AdminUserViewSet.as_view({'put': 'update'}), name='admin-user-update'),
    path('admin-users/<int:pk>/delete/', AdminUserViewSet.as_view({'delete': 'destroy'}), name='admin-user-delete'),

    # Users
    path('users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve'}), name='user-detail'),
    path('users/create/', UserViewSet.as_view({'post': 'create'}), name='user-create'),
    path('users/<int:pk>/update/', UserViewSet.as_view({'put': 'update'}), name='user-update'),
    path('users/<int:pk>/delete/', UserViewSet.as_view({'delete': 'destroy'}), name='user-delete'),

    ## Schools
    path('schools/', SchoolViewSet.as_view({'get': 'list'}), name='school-list'),
    path('schools/<int:pk>/', SchoolViewSet.as_view({'get': 'retrieve'}), name='school-detail'),
    path('schools/create/', SchoolViewSet.as_view({'post': 'create'}), name='school-create'),
    path('schools/<int:pk>/update/', SchoolViewSet.as_view({'put': 'update'}), name='school-update'),
    path('schools/<int:pk>/delete/', SchoolViewSet.as_view({'delete': 'destroy'}), name='school-delete'),

    # Students
    path('students/', StudentViewSet.as_view({'get': 'list'}), name='student-list'),
    path('students/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve'}), name='student-detail'),
    path('students/create/', StudentViewSet.as_view({'post': 'create'}), name='student-create'),
    path('students/<int:pk>/update/', StudentViewSet.as_view({'put': 'update'}), name='student-update'),
    path('students/<int:pk>/delete/', StudentViewSet.as_view({'delete': 'destroy'}), name='student-delete'),

    # Parents
    path('parents/', ParentViewSet.as_view({'get': 'list'}), name='parent-list'),
    path('parents/<int:pk>/', ParentViewSet.as_view({'get': 'retrieve'}), name='parent-detail'),
    path('parents/create/', ParentViewSet.as_view({'post': 'create'}), name='parent-create'),
    path('parents/<int:pk>/update/', ParentViewSet.as_view({'put': 'update'}), name='parent-update'),
    path('parents/<int:pk>/delete/', ParentViewSet.as_view({'delete': 'destroy'}), name='parent-delete'),
    path('parents/<int:pk>/students/', ParentViewSet.as_view({'get': 'get_students'}), name='parent-students'),

    # Parent-Student Link (NEW)
    path('parentstudentlink/', ParentStudentLinkViewSet.as_view({'get': 'list', 'post': 'create'}), name='parentstudentlink-list'),
    path('parentstudentlink/<int:pk>/', ParentStudentLinkViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='parentstudentlink-detail'),
    path('parentstudentlink/<int:parent_id>/students/', ParentStudentLinkViewSet.as_view({'get': 'students'}), name='parentstudentlink-students'),
    path('parentstudentlink/<int:student_id>/parents/', ParentStudentLinkViewSet.as_view({'get': 'parents'}), name='parentstudentlink-parents'),

    # Teachers
    path('teachers/', TeacherViewSet.as_view({'get': 'list'}), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherViewSet.as_view({'get': 'retrieve'}), name='teacher-detail'),
    path('teachers/create/', TeacherViewSet.as_view({'post': 'create'}), name='teacher-create'),
    path('teachers/<int:pk>/update/', TeacherViewSet.as_view({'put': 'update'}), name='teacher-update'),
    path('teachers/<int:pk>/delete/', TeacherViewSet.as_view({'delete': 'destroy'}), name='teacher-delete'),

    # Classes
    path('classes/', ClassViewSet.as_view({'get': 'list'}), name='class-list'),
    path('classes/<int:pk>/', ClassViewSet.as_view({'get': 'retrieve'}), name='class-detail'),
    path('classes/create/', ClassViewSet.as_view({'post': 'create'}), name='class-create'),
    path('classes/<int:pk>/update/', ClassViewSet.as_view({'put': 'update'}), name='class-update'),
    path('classes/<int:pk>/delete/', ClassViewSet.as_view({'delete': 'destroy'}), name='class-delete'),

    # Subjects
    path('subjects/', SubjectViewSet.as_view({'get': 'list'}), name='subject-list'),
    path('subjects/<int:pk>/', SubjectViewSet.as_view({'get': 'retrieve'}), name='subject-detail'),
    path('subjects/create/', SubjectViewSet.as_view({'post': 'create'}), name='subject-create'),
    path('subjects/<int:pk>/update/', SubjectViewSet.as_view({'put': 'update'}), name='subject-update'),
    path('subjects/<int:pk>/delete/', SubjectViewSet.as_view({'delete': 'destroy'}), name='subject-delete'),

    # Fee Payments
    path('payments/', PaymentViewSet.as_view({'get': 'list'}), name='payment-list'),
    path('payments/<int:pk>/', PaymentViewSet.as_view({'get': 'retrieve'}), name='payment-detail'),
    path('payments/create/', PaymentViewSet.as_view({'post': 'create'}), name='payment-create'),
    path('payments/<int:pk>/update/', PaymentViewSet.as_view({'put': 'update'}), name='payment-update'),
    path('payments/<int:pk>/delete/', PaymentViewSet.as_view({'delete': 'destroy'}), name='payment-delete'),

    # Announcements
    path('announcements/', AnnouncementViewSet.as_view({'get': 'list'}), name='announcement-list'),
    path('announcements/<int:pk>/', AnnouncementViewSet.as_view({'get': 'retrieve'}), name='announcement-detail'),
    path('announcements/create/', AnnouncementViewSet.as_view({'post': 'create'}), name='announcement-create'),
    path('announcements/<int:pk>/update/', AnnouncementViewSet.as_view({'put': 'update'}), name='announcement-update'),
    path('announcements/<int:pk>/delete/', AnnouncementViewSet.as_view({'delete': 'destroy'}), name='announcement-delete'),
]
