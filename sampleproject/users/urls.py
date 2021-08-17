from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('', views.profiles, name="profiles" ),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('account/', views.userAccount, name="user-account"),

    path('edit-account/', views.editAccount, name="edit-account"),
    path('add-skills/', views.addSkills, name="add-skills"),
    path('update-skill/<str:pk>', views.updateSkills, name='update-skill'),
    path('delete-skill/<str:pk>', views.deleteSkill, name='delete-skill'),
]