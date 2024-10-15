from django.urls import path

from app.views import Home, Redir, StaffView, CategoryView, CategoryDelete, CategoryEdit, DishView, DishDelete, \
    DishEdit, UsersView, CategoryDetail, AddDishToBasket, DeleteOneDishToBasket, BasketDelete, BasketView, \
    AddDishInBasket, CatHome

urlpatterns = [
    path('', Redir.as_view(), name='redir'),
    path('staff/users/', UsersView.as_view(), name='users'),
    path('home/', Home.as_view(), name='menu'),
    path('home/cat/<int:pk>/', CatHome.as_view(), name='cat_menu'),
    path('home/<int:pk>/', CategoryDetail.as_view(), name='cat_detail'),
    path('staff/', StaffView.as_view(), name='staff'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/delete/<int:pk>/', CategoryDelete.as_view(), name='delete_category'),
    path('categories/edit/<int:pk>/', CategoryEdit.as_view(), name='edit_category'),
    path('dishes/', DishView.as_view(), name='dishes'),
    path('dishes/delete/<int:pk>/', DishDelete.as_view(), name='delete_dish'),
    path('dishes/edit/<int:pk>/', DishEdit.as_view(), name='edit_dish'),
    path('add_dish_to_basket/<int:pk>/', AddDishToBasket.as_view(), name='add_dish_to_basket'),
    path('add_dish_in_basket/<int:pk>/', AddDishInBasket.as_view(), name='add_dish_in_basket'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('basket/delete/<int:pk>/', BasketDelete.as_view(), name='delete_basket'),
    path('delete_one_dish_to_basket/<int:pk>/', DeleteOneDishToBasket.as_view(), name='delete_one_dish_to_basket'),

]
