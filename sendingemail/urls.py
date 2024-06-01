# myapp/urls.py

from django.urls import path
from .views import schedule_email_view, schedule_success_view, schedule_mail

app_name = 'sendingemail'

urlpatterns = [
    path('schedule-email/', schedule_email_view, name='schedule_email'),
    path('schedule-success/', schedule_success_view, name='schedule_success'),
    path('send/', schedule_mail, name='schedule_mail'),
]