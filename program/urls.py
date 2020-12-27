from django.urls import path
from django.contrib.auth import views as auth_view
from .views import Programs,UserloginForm,Home,PostView

urlpatterns = [
    path('login/',UserloginForm.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('',Home.as_view(), name='home'),
    path('category/<slug:slug>/',PostView.as_view(),name="cat-detail"),
    # path('category/<slug:slug>/<slug:slug>',PostView.as_view(),name="detail-post"),
    # path('category/<slug:slug>', ,name = 'cat-page'),
    path('program/',Programs.as_view(), name='program'),
]