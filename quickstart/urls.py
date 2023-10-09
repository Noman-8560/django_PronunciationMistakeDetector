from django.urls import path
from . import views

urlpatterns = [
    # Define a URL pattern for the recording view
    path('recording/', views.recording_view, name='recording_view'),

    # Define a URL pattern for the audio recording endpoint
    path('record_audio/', views.record_audio, name='record_audio'),

    # Add other URL patterns as needed
]
