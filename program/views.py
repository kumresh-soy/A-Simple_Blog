from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView,TemplateView,CreateView
from .forms import LoginForm, PostForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .models import Post,Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout

# @method_decorator(staff_member_required,name='dispatch')
class PostView(ListView):
    model = Post
    paginate_by = 1
    # context_object_name = 'post'  # Default: object_list
    template_name = 'program/blog.html'
    
    def get_context_data(self, **kwargs):
      slug = self.kwargs.get('slug')
      context = super(PostView, self).get_context_data(**kwargs)
      context['post'] = Post.objects.filter(category__slug = slug)
      context['slug'] = slug
      return context

    def get_queryset(self):
        return Post.objects.filter(category__slug = self.kwargs.get('slug')).order_by('id')

class Home(ListView):
    modle = Category
    template_name = 'home.html'

    def get_queryset(self):
      query = self.request.GET.get('q', None)
      if not query :
        return Category.objects.all().order_by('?')[:6]
      else:
        return Category.objects.filter(tutorial_name__icontains=query)


@method_decorator(staff_member_required,name='dispatch')
class Programs(CreateView):
    template_name = 'program/program.html'
    form_class =  PostForm
    success_url ='/program/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = User.objects.get(username= self.request.user)
        kwargs.update({'initial':{'author': user}})
        return kwargs

    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)


class UserloginForm(LoginView):
  template_name = 'program/login.html'
  authentication_form = LoginForm

  def form_valid(self,form):
    uname = form.cleaned_data['username']
    upass = form.cleaned_data['password']
    user = authenticate(username=uname, password=upass)
    #checking user 
    if user.is_superuser == True:
      login(self.request, user)
      messages.success(self.request,'Logged in successfully !!')
      return HttpResponseRedirect('/admin/')

    if user.is_staff == True:
      login(self.request, user)
      messages.success(self.request,'Logged in successfully !! ')
      return HttpResponseRedirect('/program/')

    else:
      return HttpResponseRedirect('/login/')
    return super().form_valid(form)
