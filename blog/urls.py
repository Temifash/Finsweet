from django.urls import path
from . import views

# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path("", views.blogHome, name="blogHome"),
    path("business/", views.business, name="business"),
    path("post/", views.post, name="post"),
    path("font/", views.font, name="font"),
    path("new/", views.blogNew, name="blogNew"),
    path("<int:pk>/", views.blogDetails, name="blogDetails"),
    # path("addBlog/", views.addBlog, name="addBlog"),

    # path("", views.blogHome, name="blogHome"),
    # path("new/", views.blogNew, name="blogNew"),
    # path("<int:pk>/", views.blogDetails, name="blogDetails"),
    # path("delete/<int:id>/", views.deleteBlog, name="deleteBlog"),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)