from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<str:listId>", views.listing_page, name="listing_page"),
    path("addWatchList",views.addWatchList,name="addWatchList"),
    path("watchlist",views.watchlist,name="watchlist"),
    path("category",views.category,name="category"),
    path("createListing",views.createListing,name="createListing"),
    path("listing/<str:listId>/addComment",views.addComment,name="addComment"),
    path("closeListing",views.closeListing,name="addComment")
]
