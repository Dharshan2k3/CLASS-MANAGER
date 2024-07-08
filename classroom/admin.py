from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Student, StudentMarks, Teacher, StudentsInClass

# Customizing admin display for Student model
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'email', 'phone')
    list_filter = ('name', 'roll_no')
    search_fields = ('name', 'roll_no', 'email')

# Registering other models as before
admin.site.register(User, UserAdmin)
admin.site.register(StudentMarks)
admin.site.register(Teacher)
admin.site.register(StudentsInClass)
