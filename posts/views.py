from django.shortcuts import render, redirect
from posts.models import Post
from .forms import PostForm
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
	#rose for commenting 
	blog_list = Post.objects.all().order_by('-updated_at')

	context = {
		"posts" : blog_list
	}
	return render(request, 'index.html', context)

#rose for commenting
def create(request):
	if request.method == "GET":
		context = {
		"form":PostForm()
		}
		return render(request, 'create.html', context)
	elif request.method =="POST":
		form = PostForm(request.POST)
		#rose for commenting
		
		if form.is_valid():
			form.save()
			return redirect('posts:index')
		else:
			context = {
				"form":form
			}
			return render(request,'create.html',context)

def details(request,slug):
	if request.method=="POST":
		#rose for commenting
		task = get_object_or_404(Post,slug=slug)
		post = PostForm(request.POST,instance = task)
		if post.is_valid():
			post.save()
			return redirect('posts:index')
		else:
			#rose for commenting
			context = {
				"post": task,
				"form":post,
			}
			return render(request,'details.html',context)

	if request.method == "GET":
		task = get_object_or_404(Post,slug=slug)
		form = PostForm(instance = task)
		context ={
		#rose for commenting
		"post": task,
		"form":form
		}
		return render(request, 'details.html', context)
		#rose for commenting

def delete(request,slug):
	if request.method=="POST":
		task = get_object_or_404(Post,slug=slug)
		task.delete()
		return redirect("posts:index")





