from django.shortcuts import render
from datetime import datetime
from django.http.response import JsonResponse
import smtplib as smtp
# Create your views here.
from main.models import *


def indexHandler(request):
    contact = Contact.objects.all()
    online_courses = OnlineCourses.objects.all()
    abouts = AboutUs.objects.all()
    category = Category.objects.all()
    courses = Courses.objects.all()
    # teachers = Teachers.objects.order_by('-level')
    feed_backs = FeedBack.objects.all()
    popular = Category.objects.filter(popular=True)
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    cat = int(request.POST.get('category', 0))
    action = request.POST.get('action', '')
    ema1l = request.POST.get('ema1l', '')
    blogs_subjects = Blog.objects.filter(is_main=True).order_by('data')

    errors = []

    blogs_count = Blog.objects.filter(is_main=True).order_by('data').count()
    f = blogs_count % 3
    if f == 0:
        blogs = Blog.objects.filter(is_main=True).order_by('data')
    else:
        blogs = Blog.objects.filter(is_main=True).order_by('data')[:blogs_count - f]

    teachers_count = Teachers.objects.all().order_by('-level').count()
    f = teachers_count % 4
    if f == 0:
        teachers = Teachers.objects.all().order_by('-level')
    else:
        teachers = Teachers.objects.all().order_by('-level')[:teachers_count - f]

    if request.POST:
        if action == 'sighUpNow':
            sign = SignUpForCourse()
            if name:
                sign.name = name
            else:
                errors.append("NAME_NOT_FOUND")
            if email:
                # re_email = SignUpForCourse.objects.filter(email=email)
                # if re_email:
                #     errors.append("THIS_EMAIL_IS_ALREADY_REGISTERED!!!")
                # else:
                sign.email = email
            else:
                errors.append("EMAIL_NOT_FOUND")
            if cat:
                sign.course_id = cat
            else:
                errors.append("CATEGORY_NOT_FOUND")
            if not errors:
                sign.save()

                email = 'u5ad44in@yandex.ru'
                password = '010100Aa#'
                dest_email = ['m_mirzafar@mail.ru']

                subject = '****'
                email_text = f'description: {sign.name}\n email: {sign.email} '

                message = 'From: {}\nSubject: {}\n\n{}'.format(email, subject, email_text)

                server = smtp.SMTP_SSL('smtp.yandex.com')
                server.set_debuglevel(1)
                server.ehlo(email)
                server.login(email, password)
                server.sendmail(email, dest_email, message)
                server.quit()

                subject = 'ECOURSES'
                email_text = f'Vasha zayavka na etot kurs prinito!!!'

                message = 'From: {}\nSubject: {}\n\n{}'.format(email, subject, email_text)

                server = smtp.SMTP_SSL('smtp.yandex.com')
                server.set_debuglevel(1)
                server.ehlo(email)
                server.login(email, password)
                server.sendmail(email, [sign.email], message)
                server.quit()

                response = JsonResponse({'status': True}, status=200)
            else:
                response = JsonResponse({'status': False, 'errors': errors}, status=200)
            return response
        elif action == 'emailRegister':
            email_address = EmailAddress()
            if ema1l:
                re_email = EmailAddress.objects.filter(email=ema1l)
                if re_email:
                    errors.append("THIS_EMAIL_IS_ALREADY_REGISTERED!!!")
                else:
                    email_address.email = ema1l
            else:
                errors.append("EMAIL_NOT_FOUND")
            if not errors:
                email_address.save()
                response = JsonResponse({'status': True}, status=200)
            else:
                response = JsonResponse({'status': False, 'errors': errors}, status=200)
            return response
    return render(request, 'index.html',
                  {'contact': contact,
                   'online_courses': online_courses,
                   'abouts': abouts,
                   'category': category,
                   'courses': courses,
                   'teachers': teachers,
                   'feed_backs': feed_backs,
                   'blogs_count': blogs_count,
                   'popular': popular,
                   'errors': errors,
                   'blogs': blogs,
                   'blogs_subjects': blogs_subjects,
                   })


def aboutHandler(request):
    abouts = AboutUs.objects.all()
    contact = Contact.objects.all()
    feed_backs = FeedBack.objects.all()
    popular = Category.objects.filter(popular=True)
    courses = Courses.objects.all()
    blogs_subjects = Blog.objects.filter(is_main=True).order_by('data')

    name_about = request.POST.get('name', '')
    email_about = request.POST.get('email', '')
    cat_about = int(request.POST.get('category', 0))

    errors = []
    if request.POST:
        sign = SignUpForCourse()
        if name_about:
            sign.name = name_about
        else:
            errors.append("NAME_NOT_FOUND")
        if email_about:
            re_email = SignUpForCourse.objects.filter(email=email_about)
            if re_email:
                errors.append("THIS_EMAIL_IS_ALREADY_REGISTERED!!!")
            else:
                sign.email = email_about
        else:
            errors.append("EMAIL_NOT_FOUND")

        if cat_about:
            sign.course_id = cat_about
        else:
            errors.append("CATEGORY_NOT_FOUND")
        if not errors:
            sign.save()
            response = JsonResponse({'status': True}, status=200)
        else:
            response = JsonResponse({'status': False, 'errors': errors}, status=200)
        return response
    return render(request, 'about.html',
                  {'abouts': abouts,
                   'contact': contact,
                   'feed_backs': feed_backs,
                   'popular': popular,
                   'courses': courses,
                   'errors': errors,
                   'blogs_subjects': blogs_subjects,
                   })


def coursesHandler(request):
    contact = Contact.objects.all()
    category = Category.objects.all()
    courses = Courses.objects.all()
    popular = Category.objects.filter(popular=True)
    blogs_subjects = Blog.objects.filter(is_main=True).order_by('data')
    return render(request, 'courses.html',
                  {'contact': contact,
                   'category': category,
                   'courses': courses,
                   'popular': popular,
                   'blogs_subjects': blogs_subjects,
                   })


def teacherHandler(request):
    contact = Contact.objects.all()
    # teachers = Teachers.objects.all().order_by('is_main')[::-1]
    popular = Category.objects.filter(popular=True)
    blogs_subjects = Blog.objects.filter(is_main=True).order_by('data')

    teachers_count = Teachers.objects.all().order_by('-level').count()
    f = teachers_count % 4
    if f == 0:
        teachers = Teachers.objects.all().order_by('-level')
    else:
        teachers = Teachers.objects.all().order_by('-level')[:teachers_count - f]

    return render(request, 'teachers.html',
                  {'contact': contact,
                   'teachers': teachers,
                   'popular': popular,
                   'blogs_subjects': blogs_subjects,
                   })


def blogHandler(request):
    search_value = request.GET.get('q', '')
    category_id = int(request.GET.get('category_id', 0))
    contact = Contact.objects.all()
    author = Author.objects.all()
    category = Category.objects.all()
    popular = Category.objects.filter(popular=True)
    recent_post = Blog.objects.all().order_by('data')[:3]
    blogs_subjects = Blog.objects.filter(is_main=True).order_by('data')

    new_categories = []
    for pc in category:
        new_pc = {
            'id': pc.id,
            'title': pc.title,
            'count': Blog.objects.filter(category__id=int(pc.id)).count()
        }
        new_categories.append(new_pc)

    limit = int(request.GET.get('limit', 6))
    current_page = int(request.GET.get('page', 1))
    stop = current_page * limit
    start = stop - limit

    if category_id:
        if search_value:
            blogs = Blog.objects.filter(category__id=category_id).filter(post_name__contains=search_value).order_by(
                'data')[start:stop]
            total = Blog.objects.filter(category__id=category_id).filter(post_name__contains=search_value).count()
        else:
            blogs = Blog.objects.filter(category__id=category_id)[start:stop]
            total = Blog.objects.filter(category__id=category_id).count()
    else:
        if search_value:
            blogs = Blog.objects.filter(post_name__contains=search_value).order_by('data')[start:stop]
            total = Blog.objects.filter(post_name__contains=search_value).count()
        else:
            blogs = Blog.objects.all().order_by('data')[start:stop]
            total = Blog.objects.all().count()

    pages_count = int(total / limit)
    if total % limit > 0:
        pages_count += 1
    pages = range(1, pages_count + 1)

    prev_page = current_page - 1
    next_page = 0
    if total > stop:
        next_page = current_page + 1

    return render(request, 'blog.html',
                  {'contact': contact,
                   'blogs': blogs,
                   'author': author,
                   'category': category,
                   'popular': popular,
                   'recent_post': recent_post,
                   'prev_page': prev_page,
                   'next_page': next_page,
                   'limit': limit,
                   'current_page': current_page,
                   'pages': pages,
                   'search_value': search_value,
                   'category_id': category_id,
                   'products': blogs,
                   'total': total,
                   'blogs_subjects': blogs_subjects,
                   'new_categories': new_categories,
                   })


def blogsingleHandler(request, blog_id):
    contact = Contact.objects.all()
    post = Blog.objects.get(id=int(blog_id))
    comments = Comment.objects.filter(blog__id=int(blog_id))
    comments_answers = Comment.objects.filter(blog__id=int(blog_id))
    comment_len = len(comments)
    category = Category.objects.all()
    recent_post = Blog.objects.all().order_by('data')[:3]
    popular = Category.objects.filter(popular=True)
    blogs_subjects = Blog.objects.filter(is_main=True).order_by('data')
    post_comments = Comment.objects.all()
    post_comments_answers = Comment.objects.all()

    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    website = request.POST.get('website', '')
    comment_id = request.POST.get('comment_id', 0)
    description = request.POST.get('description', '')

    new_categories = []
    for pc in category:
        new_pc = {
            'id': pc.id,
            'title': pc.title,
            'count': Blog.objects.filter(category__id=int(pc.id)).count()
        }
        new_categories.append(new_pc)

    errors = []
    if request.POST:
        com = Comment()
        if name:
            com.name = name
        else:
            errors.append("NAME_NOT_FOUND")
        if email:
            com.email = email
        else:
            errors.append("EMAIL_NOT_FOUND")
        if website:
            com.website = website
        else:
            errors.append("WEBSITE_NOT_FOUND")
        if description:
            com.text = description
        else:
            errors.append("TEXT_NOT_FOUND")
        com.comment_id = comment_id
        com.blog_id = blog_id
        com.data = datetime.now()
        if not errors:
            com.save()
            response = JsonResponse({'status': True}, status=200)
        else:
            response = JsonResponse({'status': False, 'errors': errors}, status=200)
        return response

    return render(request, 'blog_single.html',
                  {'contact': contact,
                   'post': post,
                   'comments': comments,
                   'comment_len': comment_len,
                   'category': category,
                   'recent_post': recent_post,
                   'errors': errors,
                   'popular': popular,
                   'blogs_subjects': blogs_subjects,
                   'new_categories': new_categories,
                   'post_comments': post_comments,
                   'post_comments_answers': post_comments_answers,
                   'comments_answers': comments_answers,
                   })


def contactHandler(request):
    contact = Contact.objects.all()
    popular = Category.objects.filter(popular=True)
    domain = AddNewInfo.objects.all()
    blogs_subjects = Blog.objects.filter(is_main=True).order_by('data')
    courses = Courses.objects.all()

    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    cat = int(request.POST.get('category', 0))
    message = request.POST.get('message', '')

    errors = []
    if request.POST:
        contact = FeedBackMessage()
        if name:
            contact.name = name
        else:
            errors.append("NAME_NOT_FOUND")
        if email:
            re_email = SignUpForCourse.objects.filter(email=email)
            if re_email:
                errors.append("THIS_EMAIL_IS_ALREADY_REGISTERED!!!")
            else:
                contact.email = email
        else:
            errors.append("EMAIL_NOT_FOUND")
        if cat:
            contact.course_id = cat
        else:
            errors.append("CATEGORY_NOT_FOUND")
        if message:
            contact.message = message
        else:
            errors.append("MESSAGE_NOT_FOUND")
        if not errors:
            contact.save()
            response = JsonResponse({'status': True}, status=200)
        else:
            response = JsonResponse({'status': False, 'errors': errors}, status=200)
        return response
    return render(request, 'contact.html',
                  {'contact': contact,
                   'popular': popular,
                   'domain': domain,
                   'blogs_subjects': blogs_subjects,
                   'courses': courses,
                   'errors': errors,
                   })
