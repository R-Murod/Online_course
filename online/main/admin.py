from django.contrib import admin
from main.models import *


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)


class CoursesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Courses, CoursesAdmin)


class TeachersAdmin(admin.ModelAdmin):
    pass


admin.site.register(Teachers, TeachersAdmin)


class BlogAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, CommentAdmin)


class FeedBackAdmin(admin.ModelAdmin):
    pass


admin.site.register(FeedBack, FeedBackAdmin)


class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contact, ContactAdmin)


class OnlineCoursesAdmin(admin.ModelAdmin):
    pass


admin.site.register(OnlineCourses, OnlineCoursesAdmin)


class AboutUsAdmin(admin.ModelAdmin):
    pass


admin.site.register(AboutUs, AboutUsAdmin)


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)


class AddNewInfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(AddNewInfo, AddNewInfoAdmin)


class SignUpForCourseAdmin(admin.ModelAdmin):
    pass


admin.site.register(SignUpForCourse, SignUpForCourseAdmin)


class EmailAddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(EmailAddress, EmailAddressAdmin)


class FeedBackMessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(FeedBackMessage, FeedBackMessageAdmin)
