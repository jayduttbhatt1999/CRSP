from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
#
# User.add_to_class('dept', models.CharField(max_length=50))
# User.add_to_class('gScholar', models.URLField())


# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     dept = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     scholar = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

# class profiles(models.Model):
#     username = models.OneToOneField(User, on_delete=models.CASCADE)
#     dept = models.CharField(max_length=50)
#     # password = models.CharField(max_length=50)
#     scholar = models.CharField(max_length=50)

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gscholar = models.URLField(max_length=200, blank=True)
    department = models.CharField(max_length=100, blank=True)
    university = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    skills = models.ManyToManyField('Skill')

    def __str__(self):
        return self.user.username

    def get_skills(self):
        return [skill.name for skill in self.skills.all()]

    def get_skills_id(self):
        return [skill.id for skill in self.skills.all()]


class Post(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    # keywords = models.CharField(max_length=200)
    skills = models.ManyToManyField('Skill')
    abstract = models.CharField(max_length=2000)
    paper = models.FileField(upload_to='papers/')
    allow_downloading = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_on = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_skills(self):
            return [skill.name for skill in self.skills.all()]

    def is_saved_by(self,user):
        return self.savedpost_set.filter(uploaded_by=user).exists()

class Connection(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.following

    class Meta:
        unique_together = ('follower', 'following')

def get_suggested_connections(user):
    profile = Profile.objects.get(user =user.id)
    skills = profile.get_skills()
    following = [c.following_id for c in user.following.all()]
    users = User.objects.exclude(id=user.id).exclude(id__in=following)
    suggestions = []
    for u in users:
        u_profile = Profile.objects.get(user=u.id)
        if u_profile.skills.filter(name__in=skills).exists():
            suggestions.append(u)

    print(suggestions)
    return suggestions

def get_post_suggestion(user):
    profile = Profile.objects.get(user =user)
    # print(profile)
    skills = profile.get_skills_id()
    suggested_posts = Post.objects.filter(skills__in=skills).exclude(uploaded_by=user).distinct()

    return suggested_posts


class SavedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    saved_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post

    class Meta:
        unique_together = ('user', 'post')