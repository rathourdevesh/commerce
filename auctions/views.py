from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from .forms import itemDetailsForm
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import Count
from .models import User,itemDetails,bidDetails,comments,watchlist


def index(request):
    items=itemDetails.objects.filter(status='Active')
    return render(request, "auctions/index.html",{
        "items":items
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

@login_required
def create_view(request):
    if request.user.is_authenticated:
        if(request.method == 'POST'):
            user = request.user
            form = itemDetailsForm(request.POST,request.FILES)
            if(form.is_valid):
                obj = form.save(commit=False)
                obj.User=user
                obj.time=date.today()
                obj.bidPrice=request.POST['bid']
                obj.status='Active'
                obj.save()
                return HttpResponseRedirect(reverse("itemListing",args=[obj.id]))

        else:
            form = itemDetailsForm()
            return render(request,"auctions/createView.html",{
                "titleMessage":"Create New listing",
                "form":form
            })
    else:
        return render(request,"auctions/login.html",{
                "message":"Please Login to Create listing!!"
            })


def categories(request,category):
    if (category == 'categoryList'):
        categories = itemDetails.objects.values('category').distinct()
        cat_list=[]
        for category in categories:
            cat_list.append(category['category'])
        print(cat_list)
        return render(request,"auctions/categories.html",{
            "categories":cat_list
        })
    else:
        items=itemDetails.objects.filter(status='Active',category=category)
        return render(request, "auctions/index.html",{
            "items":items
        })



def item_listing(request,itemId):
    if(request.method == 'POST'):

        item=itemDetails.objects.filter(id=itemId).get()
        user=getattr(request, 'user', None)
        if('bidding' in request.POST):
            bid=bidDetails()
            bid.User=user
            bid.item=item
            bid.amount=request.POST['bidAmt']
            bid.time=date.today()
            bid.save()
            item.bidWinner=user.username
            item.bidPrice=request.POST['bidAmt']
            item.save()
        if('commenting' in request.POST):
            comment=comments()
            comment.User=user
            comment.item=item
            comment.Comment=request.POST['newComment']
            comment.time=date.today()
            comment.save()
        if('closing' in request.POST):
            item.status='Closed'
            item.save()
        if('RemoveWatchlist' in request.POST):
            watchlist.objects.filter(item=item).delete()
        if('AddWatchlist' in request.POST):
            watch=watchlist()
            watch.User=user
            watch.item=item
            watch.save()

        return HttpResponseRedirect(reverse("itemListing",args=[itemId]))         

    else:
        user=getattr(request, 'user', None)
        item=itemDetails.objects.filter(id=itemId).get()
        bidList=bidDetails.objects.filter(item=item)
        commentList=comments.objects.filter(item=item)
        watchtag=watchlist.objects.filter(item=item).aggregate(Count('item'))['item__count']
        return render(request,"auctions/listing.html",{
            "item":item,
            "bids":bidList,
            "comments":commentList,
            "watchtag":watchtag
        })

def Watchlist(request):
    user=getattr(request, 'user', None)
    wl=watchlist.objects.filter(User=user)
    return render(request, "auctions/watchlist.html",{
        "wl":wl
    })
