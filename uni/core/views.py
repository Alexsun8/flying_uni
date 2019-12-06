from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from account.models import Profile
from core.forms import NewsForm, CourseForm, LocationForm
from core.models import Course, News, Categories


def index_view(request):
    count = Course.objects.filter(status='done').count()
    user = request.user
    active = user.is_active
    index = True
    courses = Course.objects.all()
    title = "Список всех курсов"
    return render(request, 'index.html', locals())


def add_location(request):
    count = Course.objects.filter(status='done').count()
    user = request.user
    active = user.is_active
    add = True
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.save()
            return redirect('/uni/index')
    else:
        form = LocationForm()
    return render(request, 'add_location.html', locals())


def course_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    count = Course.objects.filter(status='done').count()
    news = News.objects.all().order_by('-date')
    user = request.user
    active = user.is_active
    is_pres = False
    is_vol = False
    if active:
        is_vol = user.profile.is_volunteer()
        if is_vol:
            is_pres = True
        if user.pk == course.group_president.pk or user.pk == course.teacher.pk:
            is_pres = True
        stu_list = []
        for prof in Profile.objects.all():
            if course in prof.studying.all():
                stu_list.append(prof.user)
        wish_list = []
        for prof in Profile.objects.all():
            if course in prof.wishes.all():
                wish_list.append(prof.user)
        know_list = []
        for prof in Profile.objects.all():
            if course in prof.knowledge.all():
                know_list.append(prof.user)
    return render(request, 'course.html', locals())


def add_course_to_wish(request, pk):
    course = get_object_or_404(Course, pk=pk)
    count = Course.objects.filter(status='done').count()
    user = request.user
    user.profile.wishes.add(course)
    active = user.is_active
    is_pres = False
    is_vol = False
    if active:
        is_vol = user.profile.is_volunteer()
        if is_vol:
            is_pres = True
        if user.pk == course.group_president.pk or user.pk == course.teacher.pk:
            is_pres = True
        stu_list = []
        for prof in Profile.objects.all():
            if course in prof.studying.all():
                stu_list.append(prof.user)
        wish_list = []
        for prof in Profile.objects.all():
            if course in prof.wishes.all():
                wish_list.append(prof.user)
        know_list = []
        for prof in Profile.objects.all():
            if course in prof.knowledge.all():
                know_list.append(prof.user)

    return render(request, 'course.html', locals())


def delete_course_from_wish(request, pk):
    course = get_object_or_404(Course, pk=pk)
    count = Course.objects.filter(status='done').count()
    user = request.user
    user.profile.wishes.remove(course)
    active = user.is_active
    is_pres = False
    is_vol = False
    if active:
        is_vol = user.profile.is_volunteer()
        if is_vol:
            is_pres = True
        if user.pk == course.group_president.pk or user.pk == course.teacher.pk:
            is_pres = True
        stu_list = []
        for prof in Profile.objects.all():
            if course in prof.studying.all():
                stu_list.append(prof.user)
        wish_list = []
        for prof in Profile.objects.all():
            if course in prof.wishes.all():
                wish_list.append(prof.user)
        know_list = []
        for prof in Profile.objects.all():
            if course in prof.knowledge.all():
                know_list.append(prof.user)

    return render(request, 'course.html', locals())


def add_course_to_stud(request, pk):
    course = get_object_or_404(Course, pk=pk)
    count = Course.objects.filter(status='done').count()
    user = request.user
    user.profile.studying.add(course)
    active = user.is_active
    is_pres = False
    is_vol = False
    if active:
        is_vol = user.profile.is_volunteer()
        if is_vol:
            is_pres = True
        if user.pk == course.group_president.pk or user.pk == course.teacher.pk:
            is_pres = True
        stu_list = []
        for prof in Profile.objects.all():
            if course in prof.studying.all():
                stu_list.append(prof.user)
        wish_list = []
        for prof in Profile.objects.all():
            if course in prof.wishes.all():
                wish_list.append(prof.user)
        know_list = []
        for prof in Profile.objects.all():
            if course in prof.knowledge.all():
                know_list.append(prof.user)

    return render(request, 'course.html', locals())


def delete_course_from_stud(request, pk):
    course = get_object_or_404(Course, pk=pk)
    count = Course.objects.filter(status='done').count()
    user = request.user
    user.profile.studying.remove(course)
    active = user.is_active
    is_pres = False
    is_vol = False
    if active:
        is_vol = user.profile.is_volunteer()
        if is_vol:
            is_pres = True
        if user.pk == course.group_president.pk or user.pk == course.teacher.pk:
            is_pres = True
        stu_list = []
        for prof in Profile.objects.all():
            if course in prof.studying.all():
                stu_list.append(prof.user)
        wish_list = []
        for prof in Profile.objects.all():
            if course in prof.wishes.all():
                wish_list.append(prof.user)
        know_list = []
        for prof in Profile.objects.all():
            if course in prof.knowledge.all():
                know_list.append(prof.user)

    return render(request, 'course.html', locals())


def add_course_to_know(request, pk):
    course = get_object_or_404(Course, pk=pk)
    count = Course.objects.filter(status='done').count()
    user = request.user
    user.profile.knowledge.add(course)
    active = user.is_active
    is_pres = False
    is_vol = False
    if active:
        is_vol = user.profile.is_volunteer()
        if is_vol:
            is_pres = True
        if user.pk == course.group_president.pk or user.pk == course.teacher.pk:
            is_pres = True
        stu_list = []
        for prof in Profile.objects.all():
            if course in prof.studying.all():
                stu_list.append(prof.user)
        wish_list = []
        for prof in Profile.objects.all():
            if course in prof.wishes.all():
                wish_list.append(prof.user)
        know_list = []
        for prof in Profile.objects.all():
            if course in prof.knowledge.all():
                know_list.append(prof.user)

    return render(request, 'course.html', locals())


def delete_course_from_know(request, pk):
    course = get_object_or_404(Course, pk=pk)
    count = Course.objects.filter(status='done').count()
    user = request.user
    user.profile.knowledge.remove(course)
    active = user.is_active
    is_pres = False
    is_vol = False
    if active:
        is_vol = user.profile.is_volunteer()
        if is_vol:
            is_pres = True
        if user.pk == course.group_president.pk or user.pk == course.teacher.pk:
            is_pres = True
        stu_list = []
        for prof in Profile.objects.all():
            if course in prof.studying.all():
                stu_list.append(prof.user)
        wish_list = []
        for prof in Profile.objects.all():
            if course in prof.wishes.all():
                wish_list.append(prof.user)
        know_list = []
        for prof in Profile.objects.all():
            if course in prof.knowledge.all():
                know_list.append(prof.user)

    return render(request, 'course.html', locals())


@login_required
def edit_course_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    count = Course.objects.filter(status='done').count()
    user = request.user
    active = user.is_active
    edit = True
    is_vol = user.profile.is_volunteer()
    is_pres = False
    if user.pk == course.group_president.pk or user.pk == course.teacher.pk:
        is_pres = True
    if is_vol == False and is_pres == False:
        raise Http404("Вне уровня доступа!")
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            stu_list = []
            for prof in Profile.objects.all():
                if course in prof.studying.all():
                    stu_list.append(prof.user)
            wish_list = []
            for prof in Profile.objects.all():
                if course in prof.wishes.all():
                    wish_list.append(prof.user)
            know_list = []
            for prof in Profile.objects.all():
                if course in prof.knowledge.all():
                    know_list.append(prof.user)
            return render(request, 'course.html', locals())
    else:
        form = CourseForm(instance=course)
    return render(request, 'add_course.html', locals())


@login_required
def add_course_view(request):
    count = Course.objects.filter(status='done').count()
    user = request.user
    active = user.is_active
    add = True
    if user.is_authenticated:
        wish = user.profile.wishes

    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect('/uni/index')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', locals())


def idea_view(request):
    count = Course.objects.filter(status='done').count()
    user = request.user
    active = user.is_active
    return render(request, 'idea.html', locals())


def home_view(request):
    count = Course.objects.filter(status='done').count()
    user = request.user
    active = user.is_active
    if user.is_authenticated:
        is_vol = user.profile.is_volunteer()
    news = News.objects.all().order_by('-date')
    return render(request, 'home.html', locals())


@login_required
def edit_news_view(request, pk):
    news = get_object_or_404(News, pk=pk)
    count = Course.objects.filter(status='done').count()
    user = request.user
    edit = True
    active = user.is_active
    is_vol = user.profile.is_volunteer()
    if is_vol == False:
        raise Http404("Вне уровня доступа!")
    if request.method == "POST":
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.date = timezone.now()
            news.save()
            return redirect('/uni/home')
    else:
        form = NewsForm(instance=news)
    return render(request, 'add_news.html', locals())


@login_required
def add_news_view(request):
    count = Course.objects.filter(status='done').count()
    user = request.user
    active = user.is_active
    add = True
    is_vol = user.profile.is_volunteer()
    if is_vol == False:
        raise Http404("Вне уровня доступа!")
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.date = timezone.now()
            news.save()
            return redirect('/uni/home')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', locals())


def index_with_domain_view(request, num):
    count = Course.objects.filter(status='done').count()
    user = request.user
    active = user.is_active
    index = True
    domains = Categories.DOMAIN_CHOIСES
    n = int(num)
    domain = domains[n]
    print(domain)
    courses = []
    dom = domain[1]
    types = []
    for ty in Categories.objects.all():
        if ty.domain == domain[0]:
            types.append(ty)
    print(types)
    for cou in Course.objects.all():
        if cou.type.domain == domain[0]:
            courses.append(cou)
    title = "Список курсов"
    return render(request, 'index.html', locals())


def index_with_types_view(request, pk):
    count = Course.objects.filter(status='done').count()
    user = request.user
    active = user.is_active
    index = True
    type = get_object_or_404(Categories, pk=pk)
    domain = type.domain
    courses = []
    types = []

    for d in Categories.DOMAIN_CHOIСES:
        if domain == d[0]:
            dom = d[1]

    for ty in Categories.objects.all():
        if ty.domain == domain:
            types.append(ty)
    courses = Course.objects.filter(type=type)
    title = "Список курсов"
    return render(request, 'index.html', locals())
