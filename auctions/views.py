from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse,HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse
from django.core.files.storage import default_storage
from .models import User,Listing,Bid,Category,Comment
import os,json
from commerce.settings import MEDIA_ROOT
def index(request): 
    return render(request, "auctions/index.html",{
        "listings":Listing.objects.filter(active=True).all(),
    })
def listing_page(request,listId):
    listing = Listing.objects.get(pk=listId)
    if request.method == "POST":
        bid_value = 0
        try: 
            bid_value = float(request.POST["bid_value"])
        except:
            return render(request, "auctions/listing.html",{
                "listing": listing,
                "error_message": "enter a valid bid"
            })
        if float(bid_value) > listing.latest_bid_price:
            Listing.objects.filter(pk=listId).update(latest_bid_price=float(bid_value),latest_bider=request.user)
            bid = Bid(price=float(bid_value),listing=listing,user=request.user)
            bid.save()
            return render(request, "auctions/listing.html",{
                "listing": Listing.objects.get(pk=listId),
                "message": "Your bid has been placed successfully"
            })
        else:
            return render(request, "auctions/listing.html",{
                "listing": listing,
                "error_message": "bid must be heigher"
            })
    return render(request, "auctions/listing.html",{
        "listing": listing
    })
def closeListing(request):
    if request.method == "POST":
        listingId = request.POST["listingId"]
        Listing.objects.filter(pk=listingId).update(active=False)
        Listing.objects.get(pk=listingId).save()
        return HttpResponseRedirect(redirect_to=f"listing/{listingId}")
def addComment(request,listId):
    if request.method == "POST":
        data = json.loads(request.body)
        comment = data.get('comment')
        listing = Listing.objects.get(pk=listId)
        commentInstance = Comment.objects.create(user=request.user,listing=listing,comment=comment)
        commentInstance.save()
        return JsonResponse({
        "message":"success",
        "id":commentInstance.pk,
        "created_at": commentInstance.created_at
        })
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
def addWatchList(request):
    user = request.user
    listingId = request.GET.get("listingId")
    listing = Listing.objects.get(pk=listingId)
    if user.watchList.filter(pk=listingId).count() == 0:
        User.objects.get(pk=request.user.pk).watchList.add(listing)
        return JsonResponse({
            "message":"added"
        })
    else:
        User.objects.get(pk=request.user.pk).watchList.remove(listing)
        return JsonResponse({
            "message":"removed"
        })
@login_required
def watchlist(request):
    return render(request,"auctions/watchlist.html")   
@login_required 
def category(request):
    categories = Category.objects.all()
    firstCat = Category(id=0,name="No Categories")
    if Category.objects.count() != 0:
        firstCat = Category.objects.all()[0]
    if request.method == "POST":
        print(request.POST["category"])
        firstCat = Category.objects.get(name=request.POST["category"])
        print("hello")
    return render(request,"auctions/category.html",{
        "categories":categories,
        "firstCat":firstCat
    })
@login_required
def createListing(request):
    if request.method == "POST":
        if request.POST["title"] and request.POST["description"] and request.POST["minPrice"]:
            title = request.POST["title"]
            description = request.POST["description"]
            min_price = request.POST["minPrice"]
            listing = Listing.objects.create(title=title,description=description,latest_bid_price=min_price,created_by=request.user)
            for category in request.POST.getlist('categories'):
                print(category)
                if Category.objects.filter(name=category).count() != 0:
                    Category.objects.filter(name=category)[0].listings.add(listing)
                else:
                    newCat = Category.objects.create(name=category)
                    newCat.listings.add(listing)
                    newCat.save()
            if 'image' in request.FILES:
                image = request.FILES['image']
                directory = os.path.join(MEDIA_ROOT, 'auctions/categoryIcons')
                if not os.path.exists(directory):
                    os.makedirs(directory)
                file_path = os.path.join(directory,image.name)
                try:
                    with default_storage.open(file_path,"wb+") as distination:
                        for chunk in image.chunks():
                            distination.write(chunk)
                    listing.img = file_path
                    listing.save()
                    return HttpResponseRedirect(reverse(index))
                except Exception as e:
                    return HttpResponseBadRequest("Failed to upload image: " + str(e))
            else:
                print("no image provided")
        else:
            return render(request,"auctions/createListing.html",{
                "message":"some fields are missing"
            })
    return render(request,"auctions/createListing.html")