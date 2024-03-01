from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
class User(AbstractUser):
    watchList = models.ManyToManyField('Listing',blank=True,related_name="user_watching")
class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    img = models.ImageField(upload_to='auctions/images/',default="auctions/images/default-placeholder.png")
    latest_bid_price = models.FloatField(blank=False,default=0)
    latest_bider = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    biders = models.ManyToManyField(User,blank=True,related_name="listings")
    created_at = models.DateTimeField(default=datetime.now())
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="created_listings",blank=False,null=True)
class Bid(models.Model):
    price = models.FloatField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="bids")
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="bids")
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())
class Category(models.Model):
    listings = models.ManyToManyField(Listing,related_name="categories")
    name = models.CharField(max_length=64,unique=True)
    icon = models.ImageField(upload_to="media/auctions/categoryIcons",default="media/auctions/categoryIcons/category-base.png")
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Categories"