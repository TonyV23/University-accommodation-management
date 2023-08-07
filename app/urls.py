from django.urls import path
from app.views import home, student, attribution, application, bedroom, location, department, faculty, campus, accommodation, auth

urlpatterns = [
    path('', home.index, name ='dashboard'),

    path('student', student.index, name ='view_student'),
    path('student/add', student.add_student, name ='add_student'),
    path('student/store', student.store_student, name ='store_student'),
    path('student/edit/<int:id>', student.edit_student, name ='edit_student'),
    path('student/update/<int:id>', student.update_student, name ='update_student'),
    path('student/delete/<int:id>', student.delete_student, name ='delete_student'),

    path('attribution', attribution.index, name ='view_attribution'),
    path('attribution/add', attribution.add_attribution, name ='add_attribution'),
    path('attribution/store', attribution.store_attribution, name ='store_attribution'),
    path('attribution/edit/<int:id>', attribution.edit_attribution, name ='edit_attribution'),
    path('attribution/update/<int:id>', attribution.update_attribution, name ='update_attribution'),
    path('attribution/delete/<int:id>', attribution.delete_attribution, name ='delete_attribution'),

    path('application', application.index, name ='view_application'),
    path('application/add', application.add_application, name ='add_application'),
    path('application/store', application.store_application, name ='store_application'),
    path('application/edit/<int:id>', application.edit_application, name ='edit_application'),
    path('application/update/<int:id>', application.update_application, name ='update_application'),
    path('application/delete/<int:id>', application.delete_application, name ='delete_application'),

    path('bedroom', bedroom.index, name ='view_bedroom'),
    path('bedroom/add', bedroom.add_bedroom, name ='add_bedroom'),
    path('bedroom/store', bedroom.store_bedroom, name ='store_bedroom'),
    path('bedroom/edit/<int:id>', bedroom.edit_bedroom, name ='edit_bedroom'),
    path('bedroom/update/<int:id>', bedroom.update_bedroom, name ='update_bedroom'),
    path('bedroom/delete/<int:id>', bedroom.delete_bedroom, name ='delete_bedroom'),

    path('location', location.index, name ='view_location'),
    path('location/add', location.add_location, name ='add_location'),
    path('location/store', location.store_location, name ='store_location'),
    path('location/edit/<int:id>', location.edit_location, name ='edit_location'),
    path('location/update/<int:id>', location.update_location, name ='update_location'),
    path('location/delete/<int:id>', location.delete_location, name ='delete_location'),

    path('department', department.index, name ='view_department'),
    path('department/add', department.add_department, name ='add_department'),
    path('department/store', department.store_department, name ='store_department'),
    path('department/edit/<int:id>', department.edit_department, name ='edit_department'),
    path('department/update/<int:id>', department.update_department, name ='update_department'),
    path('department/delete/<int:id>', department.delete_department, name ='delete_department'),

    path('faculty', faculty.index, name ='view_faculty'),
    path('faculty/add', faculty.add_faculty, name ='add_faculty'),
    path('faculty/store', faculty.store_faculty, name ='store_faculty'),
    path('faculty/edit/<int:id>', faculty.edit_faculty, name ='edit_faculty'),
    path('faculty/update/<int:id>', faculty.update_faculty, name ='update_faculty'),
    path('faculty/delete/<int:id>', faculty.delete_faculty, name ='delete_faculty'),

    path('campus', campus.index, name ='view_campus'),
    path('campus/add', campus.add_campus, name ='add_campus'),
    path('campus/store', campus.store_campus, name ='store_campus'),
    path('campus/edit/<int:id>', campus.edit_campus, name ='edit_campus'),
    path('campus/update/<int:id>', campus.update_campus, name ='update_campus'),
    path('campus/delete/<int:id>', campus.delete_campus, name ='delete_campus'),

    path('accommodation', accommodation.index, name ='view_accommodation'),
    path('accommodation/add', accommodation.add_accommodation, name ='add_accommodation'),
    path('accommodation/store', accommodation.store_accommodation, name ='store_accommodation'),
    path('accommodation/edit/<int:id>', accommodation.edit_accommodation, name ='edit_accommodation'),
    path('accommodation/update/<int:id>', accommodation.update_accommodation, name ='update_accommodation'),
    path('accommodation/delete/<int:id>', accommodation.delete_accommodation, name ='delete_accommodation'),

    path ('login/', auth.login_user, name = 'login'),
    path ('logout/', auth.logout_user, name = 'logout'),

    path ('accounts/', auth.index, name = 'view_users'),
    path ('accounts/add', auth.add_user, name = 'add_user'),
    path ('accounts/store', auth.store_user, name = 'store_user'),
    path ('accounts/edit/<int:id>', auth.edit_user, name = 'edit_user'),
    path ('accounts/update/<int:id>', auth.update_user, name = 'update_user'),
    path ('accounts/delete/<int:id>', auth.delete_user, name = 'delete_user'),
        
]