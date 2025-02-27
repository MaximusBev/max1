from django.urls import path
from .views import register, user_login
from .views import custom_logout
from users.views import orders_view
from .views import users_list, delete_user, edit_user, make_admin, product_list, product_detail, add_product

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path('logout/', custom_logout, name='logout'),
    path('orders/', orders_view, name='orders'),
    path('users/', users_list, name='users_list'),
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),
    path('users/edit/<int:user_id>/', edit_user, name='edit_user'),
    path('users/make-admin/<int:user_id>/', make_admin, name='make_admin'),
    path('products/', product_list, name='products'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('products/add/', add_product, name='add_product'),
]
