from django.contrib import admin
from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path("aboutus/", views.about, name="aboutus"),
    path("details/", views.Detail, name="details"),
    path("services/Crime", views.Crime, name="Crime"),
    path("services/Mystery", views.Mystery, name="Mystery"),
    path("services/Thriller", views.Thriller, name="Mystery"),
    path("services/Horror", views.Horror, name="Horror"),
    path("queryus/", views.queryus, name="queryus"),
    path("contactus/", views.contactus, name="contactus"),
    path("privacy&policy/", views.privacy_policy, name="privacy&policy"),
    path("terms&condition/", views.terms_condition, name="terms&condition"),
    # path("services/",views.services,name="services"),
    #path("services/Fantasy", views.Fantasy, name="Fantasy"),
   

    path("tracker/",views.tracker,name="tracker"),
    path("search/",views.search,name="search"),
    path("productview/<int:myid>",views.productview,name="productview"),
    path("checkout/",views.checkout,name="checkout"),
    path('login/', views.admin_login, name="admin"),
    
    path('signup',views.handleSignup,name="handleSignup"),
    path('login',views.handleLogin,name="handleLogin"),
    path('logout/',views.handleLogout,name="handleLogout"),
]