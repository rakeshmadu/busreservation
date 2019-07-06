from django.urls import path
from . import views
#### signin and find the bus
urlpatterns = [
    path('', views.home, name="home"),
    path('findbus', views.findbus, name="findbus"),#with out signup/signin it will not work
    path('bookings', views.bookings, name="bookings"),#with out signup/signin it will not work
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('success', views.success, name="success"),
    path('list', views.findbus, name="list"),
    path('signout', views.signout, name="signout"),

]
