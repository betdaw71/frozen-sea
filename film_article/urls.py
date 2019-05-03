from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='home'),
	path('films',views.films,name='films'),
	path('films/<int:genre>',views.film_genre,name='film_genre'),
	path('films/<int:genre>/<int:pk>',views.article,name='article'),
	path('serials',views.serials,name='serials'),
	path('register/', views.RegisterFormView.as_view(),name='register'),	
	path('login/',views.LoginFormView.as_view(),name='login'),
	path('logout/',views.LogoutView.as_view(),name='logout'),
	path('profile/<str:username>/',views.profile,name='profile'),
	path('films/<int:genre>/<int:pk>/like',views.like_post,name='like-post'),
	path('search',views.search,name='search')
]


