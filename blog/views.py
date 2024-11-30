from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Artwork
from .forms import ArtworkUploadForm
from django.conf import settings
from PIL import Image
import os

# 首页视图，展示所有文章列表
def home(request):
    return render(request, 'blog/home.html')

def call_me(request):
    return render(request, 'blog/call_me.html')

def art_share(request):
    artworks = Artwork.objects.all()
    form = ArtworkUploadForm()

    if request.method == 'POST' and request.FILES:
        form = ArtworkUploadForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)  # 不保存图片，先处理
            uploaded_image = artwork.image

            # 使用 Pillow 调整图片大小
            img = Image.open(uploaded_image)
            img = img.resize((300, 300))  # 将图片统一缩放为 300x300 像素
            img.save(uploaded_image.path)  # 保存修改后的图片

            artwork.save()  # 保存艺术作品
            return redirect('art_share')

    return render(request, 'blog/art_share.html', {'form': form, 'artworks': artworks})


def upload_artwork(request):
    if request.method == 'POST' and request.FILES.get('art_image'):
        art_image = request.FILES['art_image']
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)  # 确保保存到 MEDIA_ROOT
        filename = fs.save(art_image.name, art_image)  # 保存文件
        uploaded_file_url = fs.url(filename)  # 获取文件的 URL

        # 保存上传的艺术作品
        artwork = Artwork(image=uploaded_file_url)
        artwork.save()

        return redirect('art_share')  # 上传成功后跳转
    return redirect('art_share')  # 如果请求方式错误，跳转回艺术分享页面

from .models import Article
from .forms import ArticleForm

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'blog/article_create.html', {'form': form})


from django.shortcuts import get_object_or_404
def article_detail(request, pk):
    # 获取指定文章
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article_detail.html', {'article': article})