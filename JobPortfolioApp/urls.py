from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from JobPortfolioApp.views import home, education, work_experience, achievements, contact
app_name = 'JobPortfolioApp'

urlpatterns = [
    path('',home, name='home'),
    path('education', education, name="education"),
    path('experience', work_experience, name="experience"),
    path('achievements', achievements, name="achievements"),
    path('contact', contact, name="contact"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)     #setup for media server