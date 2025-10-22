"""pythondjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from myapp import views

urlpatterns = [
    path('registrationGet/',views.registrationGet),
    path('registration_post/',views.registration_post),
    path('loginGet/',views.loginGet),
    path('login_post/',views.login_post),
    path('adminHome/',views.adminHome),
    path('userHome/',views.userHome),
    path('companyHome/',views.companyHome),
    path('landingPage/',views.landingPage),

    path('adm_add_statistics/',views.adm_add_statistics),
    path('adm_manage_intern/',views.adm_manage_intern),
    path('adm_manage_company/',views.adm_manage_company),

    path('adm_view_approved_company/',views.adm_view_approved_company),
    path('adm_approve_internship/<id>',views.adm_approve_internship),
    path('adm_reject_internship/<id>',views.adm_reject_internship),
    path('adm_view_approved_internship/',views.adm_view_approved_internship),
    path('adm_view_company/',views.adm_view_company),
    path('approve_company/<id>',views.approve_company),
    path('reject_company/<id>',views.reject_company),
    path('adm_view_internship/',views.adm_view_internship),
    path('adm_view_rejected_company/',views.adm_view_rejected_company),
    path('adm_view_rejected_internship/',views.adm_view_rejected_internship),
    path('adm_change_password/',views.adm_change_password),

    path('c_add_certificate/',views.c_add_certificate),
    path('c_add_internship/',views.c_add_internship),
    path('c_add_internship_post/',views.c_add_internship_post),
    path('c_view_internship/',views.c_view_internship),
    path('c_add_task/<id>',views.c_add_task),

    path('c_add_task_post/',views.c_add_task_post),
    # path('c_view_task/',views.c_view_task),
    path('c_delete_task/<id>',views.c_delete_task),
    path('c_datesearch/',views.c_datesearch),
    path('c_registration/',views.c_registration),
    path('c_registration_post/',views.c_registration_post),
    path('c_view_application/',views.c_view_application),
    path('c_view_daily_reports/',views.c_view_daily_reports),
    path('c_view_complaints/',views.c_view_complaints),
    path('c_sent_reply/<id>',views.c_sent_reply),
    path('c_sent_reply_post/',views.c_sent_reply_post),
    path('c_view_user/',views.c_view_user),
    path('c_change_password/',views.c_change_password),
    path('c_view_applicationGet/',views.c_view_applicationGet),
    path('c_approved_applicationGet/<app_id>',views.c_approved_applicationGet),
    path('c_rejected_applicationGet/<app_id>',views.c_rejected_applicationGet),






    path('u_edit_task/<id>',views.u_edit_task),
    path('u_edit_task_post/',views.u_edit_task_post),
    path('u_ratingandreview/',views.u_ratingandreview),
    path('u_registration/',views.u_registration),
    path('u_sentcomplaints/',views.u_sentcomplaints),
    path('u_sentcomplaints_post/',views.u_sentcomplaints_post),
    path('u_view_complaints/',views.u_view_complaints),
    path('u_view_application_status/',views.u_view_application_status),
    path('u_certificate/',views.u_certificate),
    path('u_view_internship/',views.u_view_internship),
    path('u_apply/<internship_id>',views.u_apply),
    path('u_view_task/<id>',views.u_view_task),
    path('u_change_password/',views.u_change_password)
]