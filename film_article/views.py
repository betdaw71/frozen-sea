from django.shortcuts import render
from film_article.models import Article,Genre,Category,Comment,Star_article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import FormView,View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import *
import random



# Create your views here.
def index(request):
	ganres = Genre.objects.all()
	films = Article.objects.all().filter(category=Category.objects.get(title='Films'))[:15]
	serials =Article.objects.all().filter(category=Category.objects.get(title='Serials'))[:15]
	stars = Star_article.objects.all()
	# films = Article.objects.all().filter(quolity=)[:15]
	return render(request,'film_article/index.html',{'films':films,'serials':serials,'stars':stars})

def films(request):
	ganres = Genre.objects.filter(category=Category.objects.get(title='Films'))
	random_film = random.choice(Article.objects.all().filter(category=Category.objects.get(title='Films')))
	random_serial = random.choice(Article.objects.all().filter(category=Category.objects.get(title='Serials')))

	articles1 = Article.objects.filter(category=Category.objects.get(title='Films'))
	paginator = Paginator(articles1, 15)
	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	return render(request,'film_article/films.html',{'genre':ganres,'articles':articles,'random_film':random_film,'random_serial':random_serial})

def serials(request):
	ganres = Genre.objects.filter(category=Category.objects.get(title='Serials'))
	random_film = random.choice(Article.objects.all().filter(category=Category.objects.get(title='Films')))
	random_serial = random.choice(Article.objects.all().filter(category=Category.objects.get(title='Serials')))

	print(random_film)
	articles1 = Article.objects.filter(category=Category.objects.get(title='Serials'))
	paginator = Paginator(articles1, 15)
	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	return render(request,'film_article/serials.html',{'genre':ganres,'articles':articles,'random_film':random_film,'random_serial':random_serial})


def article(request,genre,pk):
	random_film = random.choice(Article.objects.all().filter(category=Category.objects.get(title='Films')))
	random_serial = random.choice(Article.objects.all().filter(category=Category.objects.get(title='Serials')))

	article = Article.objects.get(id=pk)
	iframe = article.iframe
	a = iframe.split('width')
	a.insert(1,'allowfullscreen="True" width')
	ifr = ''
	for i in a:
		ifr += i
	comments = Comment.objects.filter(article=article)
	if request.method == 'POST':
		form = ComentForm(request.POST)
		if form.is_valid():
			Comment.objects.create(body = form.cleaned_data['comment'],article=article,author=request.user)
	else:
		form = ComentForm()
	ifra = ifr.split(' ')
	ifra = [i + ' ' for i in ifra]
	return render(request,'film_article/article.html',{'comments':comments,'article':article,'random_film':random_film,'iframe':ifr,'random_serial':random_serial,'form':form})

def film_genre(request,genre):
	random_film = random.choice(Article.objects.all().filter(category=Category.objects.get(title='Films')))
	random_serial = random.choice(Article.objects.all().filter(category=Category.objects.get(title='Serials')))

	articles1 = Article.objects.all().filter(ganre = Genre.objects.get(pk=genre))
	genre = Genre.objects.get(pk=genre)
	paginator = Paginator(articles1, 15)
	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	return render(request,'film_article/film_genre.html',{'articles':articles,'random_film':random_film,'genre':genre,'random_serial':random_serial})


class RegisterFormView(FormView):
	form_class = UserCreationForm
	success_url = "/login/"
	template_name = "film_article/register.html"

	def form_valid(self, form):
		form.save()
		return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
	form_class = AuthenticationForm
	template_name = "film_article/login.html"
	success_url = "/"

	def form_valid(self, form):
		self.user = form.get_user()
		login(self.request, self.user)
		return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


def profile(request,username):
	liked = Article.objects.filter(likes=User.objects.get(username=username).pk)
	return render(request,'film_article/profile.html',{'username':username,'liked':liked})

def like_post(request,genre,pk):
	article = Article.objects.get(id=pk)
	article.likes.add(request.user)
	return HttpResponseRedirect('/films/'+str(genre)+'/'+str(pk))


def search(request):
	random_film = random.choice(Article.objects.all().filter(category=Category.objects.get(title='Films')))
	random_serial = random.choice(Article.objects.all().filter(category=Category.objects.get(title='Serials')))

	q = request.GET.get('query')
	if q:
		posts = Article.objects.filter(title__icontains=q)
	else:
		posts = []
	return render(request,'film_article/search.html',{'random_film':random_film,'random_serial':random_serial,'articles':posts})

def sitemap(request):
	from django.utils.encoding import smart_str

	response = HttpResponse(mimetype='application/force-download') # mimetype is replaced by content_type for django 1.7
	response['Content-Disposition'] = 'attachment; filename=%s' % smart_str('sitemap.xml')
	response['X-Sendfile'] = smart_str('sitemap.xml')
	# It usually a good idea to set the 'Content-Length' header too.
	# You can also set any other required headers: Cache-Control, etc.
	return response
