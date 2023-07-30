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
    # path('follow_user/<str:username>/', views.follow_user, name='follow_user'),

    path('save_post/<int:post_id>/', views.save_post, name='save_post_'),
    path('unsave_post/<int:post_id>/', views.unsave_post, name='unsave_post_'),
    path('save_post/<int:post_id>/', views.save_post, name='save_post'),
    # path('save_post/<int:post_id>', views.save_post, name='save_post'),
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
    path('on_project/', views.on_project, name='on_project'),
    path('express-interest/<int:post_id>/', views.express_interest, name='express_interest'),
    # path('update_notification_count/', views.update_notification_count, name='update_notification_count'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('collab/', views.collab, name='collab'),
    path('research_collaboration_board/', views.research_collaboration_board, name='research_collaboration_board'),
    path('post_collaboration/', views.post_collaboration, name='post_collaboration'),
    # Use the same view function for both URLs
]
