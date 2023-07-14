import profile
from multiprocessing import AuthenticationError

from django.db.models import Q
# import username as username
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
<<<<<<< HEAD
from accounts.forms import CustomUserCreationForm, CommentForm
from django.contrib.auth.models import User
=======

import accounts
from accounts.forms import CustomUserCreationForm
from django.contrib.auth.models import User as username, User
>>>>>>> development
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from accounts.models import Profile, Post, Connection, Skill, SavedPost, get_post_suggestion, Comment
from .models import get_suggested_connections
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from .models import Profile
from django.conf import settings
from django.urls import reverse_lazy
# from autocomplete_light import shortcuts as autocomplete_light


# Function for checking user First login
def first_login(request):
    try:
        # print("in try")
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # print("1st login")
        return redirect('profile_fill')


#Function is not currently inuse
#function is for sending a mail to user when they sign up
def send_registration_email(email):
    subject = 'Registration successful'
    message = 'Thai Gayu Register'
    from_email = 'moviesnucleus@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


# Function to check user is already authenciated and all the profile are set or not, if not then redirect them to profill fill page
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to the dashboard if the user is already logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            try:
                # print("in try")
                profile = Profile.objects.get(user=request.user)
                if not profile.gscholar or not profile.department or not profile.university:
                    # Redirect to profile fill page if any required fields are missing
                    return redirect('profile_fill')
                else:
                    return redirect('dashboard')
            except Profile.DoesNotExist:
                # print("1st login")
                return redirect('profile_fill')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        # invalid credentials
        return render(request, 'login.html')


# Function for registering a person
def registration_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to the dashboard if the user is already logged in
    if request.method == 'POST':
        # Extract data from the POST request
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        name = request.POST['name']

        # Do some basic validation
        if not name or not email or not password:
            # Return an error message
            return render(request, 'registration/register.html', {'error_message': 'Please fill out all fields.'})
        if password != password1:
            # Return an error message
            return render(request, 'registration/register.html', {'error_message': 'Passwords do not match.'})

        # Create a new user account
        user = User.objects.create_user(name, email, password)
        # user.dept = dept
        # user.gScholar = gScholar
        user.save()

        # Redirect to a success page or login page
        return redirect('login')
    else:
        return render(request, 'registration.html')


#Function to just start the index page
def index(request):
    # if request.user.is_authenticated:
    #     return redirect('dashboard')  # Redirect to the dashboard if the user is already logged in
    return render(request, 'index.html')


# Function to get details of user and all the suggestion values and pass it to the template
@login_required(login_url='login')
def dashboard_view(request):
    following = Connection.objects.filter(follower=request.user).values_list('following', flat=True)
    # get the posts published by those users
    posts = Post.objects.filter(uploaded_by__in=following).order_by('-published_on')
    suggestions = get_suggested_connections(request.user)
    savedlist = SavedPost.objects.filter(user=request.user)
    postsuggestion = get_post_suggestion(request.user)
    # print("post suggestion",postsuggestion)
    if posts is not None:
        return render(request, 'dashboard.html', {'posts': posts, 'suggestions' : suggestions, 'savedlist': savedlist, 'suggestedpost':postsuggestion})
    else:
        return render(request, 'dashboard.html')


# Function to logout and redirecting to login page
def logout_view(request):
    logout(request)
    if not request.user.is_authenticated:
        # User has been logged out successfully
        # print("Successful")
        return redirect('login')
    else:
        # Logout was unsuccessful
        # print("Unsuccessful")
        return redirect('home')


def posts_view(request,post_id):
    # print(post_id)
    try:
<<<<<<< HEAD
        post = Post.objects.get(id=post_id)
        post.views += 1
        post.save()

=======
        posts = Post.objects.get(id=post_id)
        posts.views += 1 # Increment the views count
        posts.save()
>>>>>>> development
        if request.user.is_authenticated:
            is_saved=SavedPost.objects.filter(user=request.user,post=post_id).exists()
            postsuggestion = get_post_suggestion(request.user)
<<<<<<< HEAD

        form = CommentForm()

=======
            # print(is_saved)
        # if request.user.is_authenticated:
        #     save_post = request.
>>>>>>> development
    except Post.DoesNotExist:
        return render(request, '404.html', status=404)

    context = {
<<<<<<< HEAD
        'post': post,
        'pdf_url': post.paper.url,
        'is_saved': is_saved,
        'suggestedpost': postsuggestion,
        'comment_form': form
=======
        'posts': posts,
        'pdf_url': posts.paper.url,
        'is_saved':is_saved,
        'suggestedpost': postsuggestion
>>>>>>> development
    }
    return render(request, 'posts.html', context)


def save_paper(request, paper_id):
    return render(request, 'posts.html')


def profile_view_test(request,username):
    try:
        userObj=User.objects.get(username=username)
        profile = Profile.objects.get(user=userObj)
        posts = Post.objects.filter(uploaded_by=userObj).order_by('-published_on')
        context = {'user': userObj, 'profile': profile, 'posts': posts}
    except Profile.DoesNotExist:
        return redirect(request,'profile_fill')

    return render(request, 'profile.html', context)


def user_profile_list(request):
    profile_list = Profile.objects.all()
    return render(request, 'users.html', {'profile_list':profile_list})


def search_publishers(request):
    if request.method=="POST":
        searched = request.POST['searched']
        publishers = User.objects.filter(username__startswith=searched)
        # profile = User.objects.get(pro)
        # profile_list = Profile.objects.filter(profile_pic__in=publishers)
        return render(request, 'search_publishers.html', {
            'searched': searched,
            'publishers': publishers,
            # 'profile': profile,
            # 'user': userObj,
            # 'profile': profile
                                                          })
    else:
        return render(request, 'search_publishers.html', {})


def searched_publishers(request):
    try:
        userObj=User.objects.get(username=username)
        profile = Profile.objects.get(user=userObj)
        posts = Post.objects.filter(uploaded_by=userObj).order_by('-published_on')
        context = {'user': userObj, 'profile': profile, 'posts': posts}
    except Profile.DoesNotExist:
        return redirect(request,'profile_fill')

    return render(request, 'search_publishers.html', context)
    # if request.method=="POST":
    #     searched = request.POST['searched']
    #     profiles = Profile.objects.filter(profile=searched)
    #     return render(request, 'search_publishers.html', {'searched': searched, 'profiles': profiles})
    # else:
    #     return render(request, 'search_publishers.html', {})

def post_search(request):
    query = request.GET.get('query', '')
    if query:
        multiple_query = Q(Q(title__icontains=query) | Q(authors__icontains=query) | Q(paper__icontains=query) | Q(abstract__icontains=query))
        posts = Post.objects.filter(multiple_query)
    else:
        posts = Post.objects.all()
    return render(request, 'search_post_list.html', {'search_result': posts, 'query': query})


def autosuggest(request):
    print(request.GET)
    term = request.GET.get('term')
    if term:
        queryset = Post.objects.filter(
            Q(title_icontains=term) | Q(authorsicontains=term) | Q(paper_icontains=term)
        )
        suggestions = [post.title for post in queryset]
        return JsonResponse(suggestions, safe=False)
    return JsonResponse([], safe=False)


def search(request):
    query = request.GET.get('query')
    if query:
        posts = Post.objects.filter(Q(keywords_icontains=query) | Q(title_icontains=query))
    else:
        posts = Post.objects.all()
    return render(request, 'search_post_list.html', {'search_result': posts})

@login_required(login_url='login')
def profile_fill_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        profile.gscholar = request.POST.get('gScholar')
        profile.department = request.POST.get('dept')
        profile.university = request.POST.get('university')

        # handle profile_pic field
        if request.FILES.get('profile_pic'):
            print("IN IF")
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            uploaded_file_url = fs.url(filename)
            profile.profile_pic = uploaded_file_url
            print(uploaded_file_url)

        skills_input = request.POST.get('skills')
        skills_input = skills_input.lower()
        skills_list = skills_input.split(',')
        skills = []
        for skill_name in skills_list:
            skill, created = Skill.objects.get_or_create (name= skill_name.strip())
            skills.append(skill)
        profile.skills.set(skills)

        print(profile)

        profile.save()
        return redirect('profile',request.user)

    return render(request, 'profile_fill.html', {'profile': profile})


@login_required(login_url='login')
def create_posts_view(request):
    if request.method == 'POST':
        # Get the form data from the request object
        title = request.POST['title']
        authors = request.POST['authors']
        # keywords = request.POST['keywords']
        allow_download = 'allow_download' in request.POST
        abstract = request.POST['abstract']
        published_on=request.POST.get('published_on')
        # Get the uploaded PDF file
        skills_input = request.POST.get('keywords')
        skills_input=skills_input.lower()
        skills_list = skills_input.split(',')

        skills = []
        for skill_name in skills_list:
            skill, created = Skill.objects.get_or_create(name=skill_name.strip())
            skills.append(skill)

        if request.FILES.get('pdf'):
            print("IN IF")
            pdf = request.FILES['pdf']
            fs = FileSystemStorage()
            filename = fs.save(pdf.name, pdf)
            uploaded_file_url = fs.url(filename)
            pdf = uploaded_file_url
            # print(uploaded_file_url)
        if pdf:
            # Create a new Post object with the form data and user
            post = Post(
                title=title,
                authors=authors,
                allow_downloading=allow_download,
                abstract=abstract,
                paper=pdf,
                uploaded_by=request.user,
                published_on=published_on
            )
            post.save()

            post.skills.set(skills)
            # Redirect to the detail view of the new post
            return redirect('posts', post.id)
    # Render the form template if the request method is GET
    return render(request, 'create_posts.html')

# Function to create a connection between users
def follow_user(request, username):
    try:
        following_user = Profile.objects.get(user=username)
    except Profile.DoesNotExist:
        following_user = Profile.objects.create(user=username)
    try:
        connection = Connection.objects.get(follower=request.user, following=following_user)
        connection.delete()
    except Connection.DoesNotExist:
        Connection.objects.create(follower=request.user, following=following_user)
    return redirect('profile', username=username)


#Function to gather all the details present in the profile model to show in profile page
def profile_view(request, username):
    try:
        userObj=User.objects.get(username=username)
        profile = Profile.objects.get(user=userObj)
        posts = Post.objects.filter(uploaded_by=userObj).order_by('-published_on')
        is_following = Connection.objects.filter(follower=request.user,following=userObj).exists()
        context = {'user': request.user, 'profile': profile, 'posts': posts, 'is_following' : is_following}
    except Profile.DoesNotExist:
        return redirect(request,'profile_fill')

    return render(request, 'profile.html', context)


#Function to just redirect to AboutUs page
def aboutUs(request):
    return render(request, 'aboutUs.html')

#Function to save post for a user and store in the mode
@login_required
def save_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    saved_post, created = SavedPost.objects.get_or_create(user=request.user, post=post)
    return redirect('posts', post_id=post_id)


#Function to unsave a post for a user
@login_required
def unsave_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    saved_post = SavedPost.objects.filter(user=request.user, post=post).first()
    if saved_post:
        saved_post.delete()
        # messages.success(request, 'Post unsaved successfully.')
    else:
        print('else')
        # messages.warning(request, 'You have not saved this post.')
    return redirect('posts', post_id=post_id)

#Function to force download a pdf if given the options
# need to change the path whoeve is using it in their system
def pdf_download(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post_path="C:/Users/Owner/PycharmProjects/CRSP/media"+post.paper.url
    print(post_path)
    # pdf_path = os.path.join('/path/to/pdf/files', str(pdf_file.pdf_file))
    with open(post_path,'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{post.paper.name}"'
<<<<<<< HEAD
        return response


# def search_view(request):
#     if 'search' in request.GET:
#         search_query = request.GET['search']
#         results = Post.objects.filter(
#             Q(authors__icontains=search_query) |
#             Q(paper__icontains=search_query) |
#             Q(abstract__icontains=search_query) |
#             Q(uploaded_by__icontains=search_query) |
#             Q(title__icontains=search_query)
#         )
#     else:
#         results = []
#
#     context = {
#         'results': results,
#         'search_query': search_query
#     }
#     return render(request, 'search_post_list.html', context)


def post_search(request):
    query = request.GET.get('query', '')
    if query:
        multiple_query = Q(Q(title__icontains=query) | Q(authors__icontains=query) | Q(paper__icontains=query) | Q(
            abstract__icontains=query))
        posts = Post.objects.filter(multiple_query)
    else:
        posts = Post.objects.all()
    return render(request, 'search_post_list.html', {'search_result': posts, 'query': query})


def autosuggest(request):
    print(request.GET)
    term = request.GET.get('term')
    if term:
        queryset = Post.objects.filter(
            Q(title__icontains=term) | Q(authors__icontains=term) | Q(paper__icontains=term)
        )
        suggestions = [post.title for post in queryset]
        return JsonResponse(suggestions, safe=False)
    return JsonResponse([], safe=False)


def search(request):
    query = request.GET.get('query')
    if query:
        posts = Post.objects.filter(Q(keywords__icontains=query) | Q(title__icontains=query))
    else:
        posts = Post.objects.all()
    return render(request, 'search_post_list.html', {'search_result': posts})


@login_required
# def add_comment(request, post_id):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post_id = post_id
#             comment.name = request.user.username
#             comment.save()
#             return redirect('posts', post_id=post_id)
#     else:
#         form = CommentForm()
#         post1 = Post.objects.get(id=post_id)
#         get_comment = post1.comments.all()
#         comment_form = CommentForm()
#         return render(request, 'posts.html', {'post': post1, 'get_comment': get_comment, 'comment_form': comment_form})
#     return redirect('posts', post_id=post_id)
#
def add_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post_id
            comment.name = request.user.username
            comment.save()
            return redirect('posts', post_id=post_id)
    else:
        form = CommentForm()
        post1 = get_object_or_404(Post, id=post_id)
        get_comment = post1.comments.all()
        comment_form = CommentForm()
        return render(request, 'posts.html', {'post': post1, 'get_comment': get_comment, 'comment_form': comment_form})
    return redirect('posts', post_id=post_id)


def add_reply(request, comment_id):
    if request.method == 'POST':
        reply_content = request.POST.get('reply_content')
        comment = get_object_or_404(Comment, id=comment_id)

        comment.reply_content = reply_content
        comment.save()

        return redirect('posts', post_id=comment.post_id)
    return redirect('home')
=======
        return response
>>>>>>> development
