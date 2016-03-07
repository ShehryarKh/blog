from django.shortcuts import render, redirect
from django.views.generic import View

from posts.models import Post
from .forms import PostForm,UserForm,UserProfileForm
from django.shortcuts import get_object_or_404

#user registration
class register(View):
	template = "register.html"
	def get(self,request):
		register = False
		if request.user.is_authenticated():
			return render(request,"index.html", {})

		userform = UserForm()
		profileform = UserProfileForm()

		context={
		'userform':userform,
		'profileform':profileform
		}

		return render(request,self.template, context)

	def post(self,request):

		userform = UserForm(data=request.POST)
		profileform = UserProfileForm(data=request.POST)

		if userform.is_valid and profileform.is_valid:
			user = userform.save()

			profile = profileform.save(commit=False)
			profile.user = user

			profile.save()
			return redirect('/')
		else:
			context={
			'userform':userform,
			'profileform':profileform
			}

			return render(request,self.template,context)

# class login(self,request):

# 	if request.method =="GET":
# 		return render(request,'login.html',{})
# 	if request.method =="POST":
# 		username = request.POST['username']
# 		password = request.POST['password']



class index(View):
	def get(self,request):
		template = "index.html"
		#rose for commenting 
		blog_list = Post.objects.all().order_by('-updated_at')

		context = {
			"posts" : blog_list
		}
		return render(request, 'index.html', context)

class create(View):
	template = "create.html"

	def get(self,request):
		context = {
		"form":PostForm()
		}
		return render(request, self.template, context)

	def post(self,request):
		form = PostForm(request.POST)
		#rose for commenting
		
		if form.is_valid():
			form.save()
			return redirect('posts:index')
		else:
			context = {
				"form":form
			}
			return render(request,self.template,context)

class details(View):
	def post(self,request,slug):

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

	def get(self,request,slug):
		task = get_object_or_404(Post,slug=slug)
		form = PostForm(instance = task)
		context ={
		#rose for commenting
		"post": task,
		"form":form
		}
		return render(request, 'details.html', context)
		#rose for commenting
class delete(View):
	def post(self,request,slug):
		task = get_object_or_404(Post,slug=slug)
		task.delete()
		return redirect("posts:index")





