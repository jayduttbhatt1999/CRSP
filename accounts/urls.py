from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.login_view, name='login_'),  # With /
    path('login', views.login_view, name='login'),  # Without /

    path('registration/', views.registration_view, name='registration_'),
    path('registration', views.registration_view, name='registration'),

    path('dashboard/', views.dashboard_view, name='dashboard_'),
    path('dashboard', views.dashboard_view, name='dashboard'),

    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('posts/<int:post_id>/', views.posts_view, name='posts_'),
    path('posts/<int:post_id>', views.posts_view, name='posts'),

    path('create_posts/', views.create_posts_view, name='create_posts_'),
    path('create_posts', views.create_posts_view, name='create_posts'),

    path('profile_fill/', views.profile_fill_view, name='profile_fill_'),
    path('profile_fill', views.profile_fill_view, name='profile_fill'),

    # path('save_paper/<int:paper_id>/',views.save_paper, name='save_paper_'),
    # path('save_paper/<int:paper_id>',views.save_paper, name='save_paper'),

    path('', views.index, name='index'),

    path('logout/', views.logout_view, name='logout_'),
    path('logout', views.logout_view, name='logout'),

    path('profile/<str:username>', views.profile_view, name='profile'),  # without/
    path('profile/<str:username>/', views.profile_view, name='profile_'),  # with/

    path('follow_user/<str:username>', views.follow_user, name='follow_user'),  # without/
    path('follow_user/<str:username>/', views.follow_user, name='follow_user_'),  # with/

    path('save_post/<int:post_id>/', views.save_post, name='save_post_'),
    path('unsave_post/<int:post_id>/', views.unsave_post, name='unsave_post_'),
    path('save_post/<int:post_id>', views.save_post, name='save_post'),
    path('unsave_post/<int:post_id>', views.unsave_post, name='unsave_post'),

    path('pdf_download/<int:post_id>/', views.pdf_download, name='pdf_download_'),
    path('pdf_download/<int:post_id>', views.pdf_download, name='pdf_download'),
    path('search_publishers/', views.search_publishers, name='search_publishers_'),  # without/
    path('search_publishers/', views.searched_publishers, name='searched_publishers_'),
    path('profile/', views.user_profile_list, name='profile_'),

    path('autosuggest', views.autosuggest, name="autosuggest"),
    path('search/', views.post_search, name='post_search'),
    path('search/', views.search, name='search'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    # path('add_reply/<int:comment_id>/', views.reply, name='add_reply'),
    path('add_reply/<int:comment_id>/', views.add_reply, name='add_reply'),
    # path('profile/<str:username>/personal_comment/', views.personal_comment, name='personal_comment'),
    # path('profile/<str:username>/personal_reply/', views.personal_reply, name='personal_reply'),
    path('profile/<str:username>/chat', views.chat, name='chat_page'),
    # path('profile/message/<str:username>_')
]
