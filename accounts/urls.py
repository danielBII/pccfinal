from django.contrib import admin
from django.urls import path
from accounts.views import (
    create_accont, 
    account_profile, 
    login_view, 
    logout_view, 
    recovery_password, 
    redefine_view,
    account_profile_edit
    )


urlpatterns = [
    path('create/', create_accont, name="createaccount"),
    path('edit/', account_profile_edit, name="editaccount"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    
    path('', account_profile, name="profile"),

    path('recovery-password/', recovery_password, name="recoverypass"),
    path('retype-password/', logout_view, name="redefine"),
    path('click-password/<str:email>/', redefine_view, name="clickpass"),
]
