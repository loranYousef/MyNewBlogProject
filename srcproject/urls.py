"""srcproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django .conf import settings
from django.conf.urls.static import static
from django.urls import path, include
#from posts.views import post_list ,post_create ,post_detail, edit_post , delete_post
from postcbv.views import PostList , PostDetail , PostCreate ,PostEdit , PostDelete





urlpatterns = [
    path('admin/', admin.site.urls),
    #path('blog/' , post_list ),
    #path('blog/create' , post_create ),
   # path('blog/<int:id>/' , post_detail),
   # path('blog/<int:id>/edit' , edit_post),
   # path('blog/<int:id>/delete' , delete_post),

   path('blog/' , PostList.as_view()),
   path('blog/<int:pk>/' , PostDetail.as_view()),
   path('blog/create' , PostCreate.as_view() ),
   path('blog/<int:pk>/edit' , PostEdit.as_view()),
   path('blog/<int:pk>/delete' , PostDelete.as_view()),
   




]

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
