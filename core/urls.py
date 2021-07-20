from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from blog.views import home
from django.conf.urls.static import static
from django.conf import settings
from blog.views import view_desenv



urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(('blog.urls', 'blogs'), namespace="blog")),
    path('account/', include(('accounts.urls', 'accounts'), namespace="accounts")),
    path('courses/', include(('courses.urls', 'courses'), namespace="courses")),
    path('galery/', include(('galery.urls', 'galery'), namespace="galery")),
    path('desenvolvedores/', view_desenv, name="desenvolvedores"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', home),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)