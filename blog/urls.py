# urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),  # 首页，展示文章列表
    path('art_share/',views.art_share,name='art_share'),
    path('upload_artwork/',views.upload_artwork,name='upload_artwork'),
    path('call_me/',views.call_me,name='call_me'),
    path('article_list/',views.article_list,name='article_list'),
    path('articles/create/',views.article_create,name='article_create'),
path('article_list/<int:pk>/', views.article_detail, name='article_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
