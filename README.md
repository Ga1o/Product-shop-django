* Product Shop project

Django base project of product shop with register, auth users, reset password, product reviews, 
list of favorites products, search of products by name and by category, rating of products, 
cart of products, celery, redis.

Libraries:
- django
- pillow
- celery
- redis
- eventlet

For correct work you need to:
- make migrations
- create folder 'media/product_images/' in root directory 
- create superuser for adding products in admin panel

For start this project:
- redis-server // start redis server
- celery -A project worker --loglevel=info -P eventlet // start celery
- python manage.py runserver // run django