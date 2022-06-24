from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    count_courses = models.IntegerField(default=0)
    popular = models.BooleanField()

    def __str__(self):
        return self.title


class Courses(models.Model):
    title = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    count_students = models.IntegerField(default=0, blank=True)
    duration = models.TimeField(blank=True, null=True)
    rating = models.IntegerField(default=0, blank=True)
    reviews = models.IntegerField(default=0, blank=True)
    price = models.IntegerField(default=0, blank=True)
    comments_count = models.IntegerField(default=0, blank=True)
    description = models.TextField(max_length=300, blank=True)
    short_title = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload', default='')
    hours = models.TimeField(blank=True, null=True)
    minutes = models.TimeField(blank=True, null=True)
    hours_int = models.IntegerField(default=0, blank=True)
    minutes_int = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


class Teachers(models.Model):
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    profession = models.CharField(max_length=300)
    level = models.IntegerField(default=0)
    is_main = models.BooleanField()
    profession_foreign = models.ForeignKey(Category, on_delete=models.CASCADE, default=True)
    twitter = models.CharField(max_length=300, blank=True)
    facebook = models.CharField(max_length=300, blank=True)
    linkedIn = models.CharField(max_length=300, blank=True)
    instagram = models.CharField(max_length=300, default='', blank=True)
    whatsapp = models.CharField(max_length=300, default='', blank=True)
    telegram = models.CharField(max_length=300, default='', blank=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    author_name = models.CharField(max_length=300, blank=True)
    author_text = models.TextField(blank=True)
    data = models.DateField()
    post_name = models.CharField(max_length=300)
    logo1 = models.ImageField(upload_to='upload', blank=True)
    logo2 = models.ImageField(upload_to='upload', blank=True)
    info1 = models.TextField(blank=True)
    info2 = models.TextField(blank=True)
    info3 = models.TextField(blank=True)
    info4 = models.TextField(blank=True)
    plus_post_name = models.CharField(max_length=300, blank=True)
    logo_author = models.ImageField(upload_to='upload', default='', blank=True)
    logo_recent = models.ImageField(upload_to='upload', default='', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, blank=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.post_name


class Comment(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=200, default='', blank=True)
    website = models.CharField(max_length=200, default='', blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)
    text = models.TextField()
    data = models.DateField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class FeedBack(models.Model):
    name = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    text = models.TextField()
    profession = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Contact(models.Model):
    address = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    phone = models.IntegerField()
    twitter = models.CharField(max_length=300, default='', blank=True)
    facebook = models.CharField(max_length=300, default='', blank=True)
    linkedIn = models.CharField(max_length=300, default='', blank=True)
    instagram = models.CharField(max_length=300, default='', blank=True)

    def __str__(self):
        return self.address


class OnlineCourses(models.Model):
    min_title = models.CharField(max_length=300, blank=True)
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    logo = models.ImageField(upload_to='upload')
    percent = models.IntegerField(default=0)
    short_description = models.TextField()
    info1 = models.CharField(max_length=300)
    info2 = models.CharField(max_length=300)
    info3 = models.CharField(max_length=300)
    info4 = models.CharField(max_length=300, default='')
    info5 = models.CharField(max_length=300, default='')
    info6 = models.CharField(max_length=300, default='')
    logo2 = models.ImageField(upload_to='upload', default='')
    logo3_header = models.ImageField(upload_to='upload', default='')

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    logo = models.ImageField(upload_to='upload')

    def __str__(self):
        return self.name


class AddNewInfo(models.Model):
    about = models.CharField(max_length=300)
    subjects = models.CharField(max_length=300)
    subjects_title = models.CharField(max_length=300)
    course = models.CharField(max_length=300)
    course_title = models.CharField(max_length=300)
    teachers = models.CharField(max_length=300)
    teachers_title = models.CharField(max_length=300)
    testimonial = models.CharField(max_length=300)
    testimonial_title = models.CharField(max_length=300)
    our_blog = models.CharField(max_length=300)
    our_blog_title = models.CharField(max_length=300)
    domain_name = models.CharField(max_length=300)
    my_site = models.CharField(max_length=300)
    newsletter_title = models.CharField(max_length=300, default='')
    newsletter_description = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.about


class SignUpForCourse(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class EmailAddress(models.Model):
    email = models.CharField(max_length=300)

    def __str__(self):
        return self.email


class FeedBackMessage(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.name


class PostComment(models.Model):
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload', blank=True, default='')
    description = models.CharField(max_length=300)
    date = models.DateTimeField()
    comment_id = models.IntegerField(default=0)
    email = models.CharField(default='', blank=True, max_length=300)
    subject = models.CharField(max_length=300, blank=True, default='')

    def __str__(self):
        return self.title
