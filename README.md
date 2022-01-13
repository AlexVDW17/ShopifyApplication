Hello and welcome to my shopify application! 
I created an inventory system using python and the django rest framework. 
The system supports CRUD operations for Products, which can be viewed as the "idea" of an item, 
as well as Items, which can be viewed as the physical implementation of a Product. Therefore every item is associated with the Product it represents.
Finally, these Items can be placed in and moved around warehouses, which are simple objects with only a name and id. Deleting a warehouse will also delete any items within it.

SETUP:
1) install git if necessary, and clone this repository!
2) install python 3 if necessary
3) install pip if necessary
4) run: pip install "dependencies" a list of which can be found in requirements.txt
5) run: python manage.py migrate
6) run: python manage.py createsuperuser 
7) follow the prompts and keep your user/password in mind 
8) run: python manage.py runserver 
9) go to http://127.0.0.1:8000/admin and enter your user/password
10) give me an interview! (pretty please)


NOTES: If you look through the git history, you'll see I tried to set up heroku for easy access for you guys. Turns out heroku has a file policy of deleting everything in database when the dyno goes down if you use sqlite, and I don't have the paid package so I couldn't keep the dyno up 24/7. Sorry about that, hopefully setup still goes fine.
I used the auto generated admin site as the frontend for this because, in my opinion, its a big strength of django and it looks better than anything I could throw together. 
Finally, thanks for the opportunity and have a great day!

-Alex