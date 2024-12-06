from django.urls import path, re_path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.home, name='home'),  # Asosiy sahifa
    path('user-home', views.user_home, name='user_home'),  # Foydalanuvchi sahifasi
    path('play/', views.play, name='play'),  # O'yin
    path('leaderboard/', views.leaderboard, name='leaderboard'),  # Natijalar ro'yxati
    re_path(r'^submission-result/(?P<attempted_question_pk>\d+)/$', views.submission_result, name='submission_result'),  # Regex bilan sahifa
    path('login/', views.login_view, name='login'),  # Login sahifasi
    path('logout/', views.logout_view, name='logout'),  # Logout
    path('register/', views.register, name='register'),  # Ro'yxatdan o'tish
]
