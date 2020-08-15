from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_view, name="createView"),
    path("categories/<str:category>", views.categories, name="categories"),
    path("item/<str:itemId>",views.item_listing,name="itemListing"),
    path("watchlist",views.Watchlist,name="watchlist")

]
