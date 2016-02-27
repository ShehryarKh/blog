from django.shortcuts import render, redirect
from posts.models import Post
from .forms import PostForm,UpdatePostForm
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
	blog_list = Post.objects.all()

	context = {
		"posts" : blog_list
	}
	return render(request, 'index.html', context)


def create(request):
	if request.method == "GET":
		context = {
		"form":PostForm()
		}
		return render(request, 'create.html', context)
	elif request.method =="POST":
		form = PostForm(request.POST)
		
		if form.is_valid():
			form.save()
		return redirect('posts:index')

def details(request,id):
	if request.method=="POST":
		task = get_object_or_404(Post,pk=id)
		post = UpdatePostForm(request.POST,instance = task)
		if post.is_valid():
			post.save()
			return redirect('posts:index')
	if request.method == "GET":
		task = get_object_or_404(Post,pk=id)
		form = UpdatePostForm(instance = task)
		context ={
		"post": task,
		"form":form
		}
		return render(request, 'details.html', context)

def delete(request,id):
	if request.method=="POST":
		task = get_object_or_404(Post,pk=id)
		task.delete()
		return redirect("posts:index")





