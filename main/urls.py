from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('carla', views.carla, name='carla'),
    path('about', views.about, name='about'),
    path('last', views.last, name='last'),
    path('fifth', views.fifth, name='fifth'),
    path('seventh', views.seventh, name='seventh'),
    path('eighth', views.eighth, name='eighth'),
    path('sixth', views.sixth, name='sixth'),
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload-book'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book),
    path('post/<int:post_id>',views.show_post,name='post'),
    path('', views.book, name = 'book'),
    path('add_emp/', views.add_emp),
]


