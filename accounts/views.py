
from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from accounts.forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from accounts.models import Profile, Post, Connection, Skill, SavedPost, get_post_suggestion
from .models import get_suggested_connections
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse_lazy
# from autocomplete_light import shortcuts as autocomplete_light

def first_login(request):
    try:
        # print("in try")
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # print("1st login")
        return redirect('profile_fill')

def send_registration_email(email):
    subject = 'Registration successful'
    message = 'Thai Gayu Register'
    from_email = 'moviesnucleus@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

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

def registration_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to the dashboard if the user is already logged in
    if request.method == 'POST':
        # Extract data from the POST request
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        name = request.POST['name']
        # gScholar = request.POST['gScholar']
        # dept = request.POST['dept']
        # print(request)
        # print('123')
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

# def registration_view(request):
#     if request.method == 'POST':
#         #extracting details
#         email = request.POST['email']
#         password = request.POST['password']
#         password1 = request.POST['password1']
#         name = request.POST['name']
#         gScholar = request.POST['gScholar']
#         dept = request.POST['dept']

#         if form.is_valid()==True:
#             print(3)
#             user = form.save()
#             print('saved')
#             login(request, user)
#             return redirect('home')
#     else:
#         print(4)
#         form = CustomUserCreationForm()
#  
    # return render(request, 'registration.html', {'form': form})

def index(request):
    # if request.user.is_authenticated:
    #     return redirect('dashboard')  # Redirect to the dashboard if the user is already logged in
    return render(request, 'index.html')

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
    # return render(request, 'dashboard.html', {'posts': posts})
    else:
        return render(request, 'dashboard.html')

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
        posts = Post.objects.get(id=post_id)
        posts.views += 1 # Increment the views count
        posts.save()
        if request.user.is_authenticated:
            is_saved=SavedPost.objects.filter(user=request.user,post=post_id).exists()
            postsuggestion = get_post_suggestion(request.user)
            # print(is_saved)
        # if request.user.is_authenticated:
        #     save_post = request.
    except Post.DoesNotExist:
        return render(request, '404.html', status=404)
    
    context = {
        'posts': posts,
        'pdf_url': posts.paper.url,
        'is_saved':is_saved,
        'suggestedpost': postsuggestion
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


# def user_profile(request,username):
#     print(username)
#     try:
#         userObj=User.objects.get(username=username)
#         profile = Profile.objects.get(user=userObj)
#         posts = Post.objects.filter(uploaded_by=userObj)
#         context = {'user': request.user, 'profile': profile, 'posts': posts}
#     except Profile.DoesNotExist:
#         return render(request, '404.html', status=404)
#     return render(request, 'profile.html', context)
 
    # try:
    #     profile = Profile.objects.get(user=username)
    #     posts = Post.objects.filter(uploaded_by=username).order_by('-published_on')
    #     context = {'user': request.user, 'profile': profile, 'posts': posts}
    # except Profile.DoesNotExist:
    #     return render(request, '404.html', status=404)

    # return render(request, 'profile_view.html', context)

# def profile_fill_view(request):
#     profile = Profile.objects.get(user=request.user)

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')

#     else:
#         form = ProfileForm(instance=profile)

#     return render(request, 'profile.html', {'form': form})

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

# def create_posts_view(request):
#     return render(request,'create_posts.html')
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
        # print (skills_input)
        skills_input=skills_input.lower()
        skills_list = skills_input.split(',')
        # print (skills_list)
        skills = []
        for skill_name in skills_list:
            skill, created = Skill.objects.get_or_create(name=skill_name.strip())
            skills.append(skill)
        # print(skills)


        
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


# number1
# @login_required(login_url='login')
# def create_post_view(request):
#     if request.method == 'POST':
#         # Get the form data from the request object
#         title = request.POST['title']
#         authors = request.POST['authors']
#         keywords = request.POST['keywords']
#         allow_download = 'allow_download' in request.POST
#         abstract = request.POST['abstract']
#         published_on=request.POST.get('published_on')
#         # Get the uploaded PDF file
#         pdf_file = request.FILES.get('pdf', None)
#         if pdf_file:
#             # Create a new Post object with the form data and user
#             post = Post(
#                 title=title,
#                 authors=authors,
#                 keywords=keywords,
#                 allow_download=allow_download,
#                 abstract=abstract,
#                 pdf_file=pdf_file,
#                 user=request.user
#                 published_on=published_on
#             )
#             post.save()
#             # Redirect to the detail view of the new post
#             return redirect(reverse('posts', args=[post.id]))
#     # Render the form template if the request method is GET
#     return render(request, 'create_post.html')

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

def profile_view(request,username):
    try:
        userObj=User.objects.get(username=username)
        profile = Profile.objects.get(user=userObj)
        posts = Post.objects.filter(uploaded_by=userObj).order_by('-published_on')
        is_following = Connection.objects.filter(follower=request.user,following=userObj).exists()
        context = {'user': request.user, 'profile': profile, 'posts': posts, 'is_following' : is_following}
    except Profile.DoesNotExist:
        return redirect(request,'profile_fill')

    return render(request, 'profile.html', context)
    
def follow_user(request, username):
    userObj=User.objects.get(username=username)
    try:
        following_user = Profile.objects.get(user=userObj)
    except Profile.DoesNotExist:
        following_user = Profile.objects.create(user=userObj)
    try:
        connection = Connection.objects.get(follower=request.user, following=userObj)
        connection.delete()
    except Connection.DoesNotExist:
        Connection.objects.create(follower=request.user, following=userObj)
    return redirect('profile', username=username)

def aboutUs(request):
    return render(request, 'aboutUs.html')


@login_required
def save_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    saved_post, created = SavedPost.objects.get_or_create(user=request.user, post=post)
    # if not created:
    #     # messages.warning(request, 'You have already saved this post.')
    # else:
    #     messages.success(request, 'Post saved successfully.')
    return redirect('posts', post_id=post_id)

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

def pdf_download(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post_path="C:/Users/Owner/PycharmProjects/CRSP/media"+post.paper.url
    print(post_path)
    # pdf_path = os.path.join('/path/to/pdf/files', str(pdf_file.pdf_file))
    with open(post_path,'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{post.paper.name}"'
        return response