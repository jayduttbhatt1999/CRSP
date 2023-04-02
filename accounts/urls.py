from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.login_view, name='login_'), # With /
    path('login', views.login_view, name='login'), # Without /


    path('registration/', views.registration_view, name='registration_'),
    path('registration', views.registration_view, name='registration'),

    path('dashboard/',views.dashboard_view, name='dashboard_'),
    path('dashboard',views.dashboard_view, name='dashboard'),

    path ('aboutUs/',views.aboutUs, name='aboutUs'),
    path('posts/<int:post_id>/',views.posts_view, name='posts_'),
    path('posts/<int:post_id>',views.posts_view, name='posts'),

    path('create_posts/',views.create_posts_view, name='create_posts_'),
    path('create_posts',views.create_posts_view, name='create_posts'),


    path('profile_fill/',views.profile_fill_view, name='profile_fill_'),
    path('profile_fill',views.profile_fill_view, name='profile_fill'),

    # path('save_paper/<int:paper_id>/',views.save_paper, name='save_paper_'),
    # path('save_paper/<int:paper_id>',views.save_paper, name='save_paper'),

    path('', views.index, name='index'),

    path('logout/', views.logout_view, name='logout_'),
    path('logout', views.logout_view, name='logout'),

    
    path('profile/<str:username>',views.profile_view, name='profile'), #without/
    path('profile/<str:username>/',views.profile_view, name='profile_'), #with/

    path('follow_user/<str:username>',views.follow_user, name='follow_user'), #without/
    path('follow_user/<str:username>/',views.follow_user, name='follow_user_'), #with/

    path('save_post/<int:post_id>/', views.save_post, name='save_post_'),
    path('unsave_post/<int:post_id>/', views.unsave_post, name='unsave_post_'),
    path('save_post/<int:post_id>', views.save_post, name='save_post'),
    path('unsave_post/<int:post_id>', views.unsave_post, name='unsave_post'),

    path('pdf_download/<int:post_id>/', views.pdf_download, name='pdf_download_'),
    path('pdf_download/<int:post_id>', views.pdf_download, name='pdf_download'),
]
