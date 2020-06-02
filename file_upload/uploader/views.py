from django.shortcuts import render, redirect
from .models import Post
from .utils import upload_and_create

# Create your views here.
def home(request):
  if (request.method == 'POST'):
    file_to_upload = request.FILES.get('img')
    upload_and_create(request, file_to_upload)

    return redirect('home')

  posts = Post.objects.all()
  return render(request, 'home.html', { 'posts': posts })