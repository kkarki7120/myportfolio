from django.urls import path
from user.views.contact import contact
from user.views.home import home
from user.views.about import about
from user.views.project import project

urlpatterns = [
    path('', home , name='home'),
    path('about/', about, name="about"),
    path('contact/', contact.as_view(), name='contact'),
    path('project/', project.as_view(), name='project'),
]