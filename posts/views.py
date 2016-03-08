from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from posts.models import Post
from .forms import PostForm,UserForm,UserProfileForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin


#user registration
class register(View):
	template = "register.html"

	def get(self,request):
		register = False
		if request.user.is_authenticated():
			return render(request,"index.html")

		userform = UserForm()
		profileform = UserProfileForm()

		context = {
			'userform': userform,
			'profileform': profileform
		}

		return render(request,self.template, context)

	def post(self,request):
		userform = UserForm(data=request.POST)
		profileform = UserProfileForm(data=request.POST)

		if userform.is_valid() and profileform.is_valid():
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


class create(LoginRequiredMixin,TemplateView):
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


class details(LoginRequiredMixin, TemplateView):
	template = "details.html"

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

class login(View):
	template = "login.html"
	

	def post(self,request):
		if request.user.is_authenticated():
			messages.warning(request, "You are already logged in.")
			return render(request, 'login.html')

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:

			if user.is_active:
				#create a session

				login(request,user)

				return redirect('/')
			else:
				return HttpResponse("your rango account is disabled.")

		else:
			print("Invalid login details")
			return HttpResponse("Invalid details")

	def get(self,request):
		return render(request,'login.html', {})


@login_required
def logout(request):
	logout(request)

	return redirect('/')













