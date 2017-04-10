from django.conf.urls import include, url
from django.contrib import admin
from boletin import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact$',views.contact,name='contact'),
    url(r'^$',views.inicio,name='inicio')
]
