from django.contrib import admin
from django.urls import path, include
from users import views
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static


def home(request):
    return render(request, "base.html")  # Головна сторінка

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Головна сторінка (залиш один із варіантів)
    path("", home, name="home"),  # ✅ Якщо `main.urls` не має своєї головної
    # path('', include('main.urls')),  # ✅ Якщо головна сторінка є в `main.urls`
    
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
    path('users/', include('users.urls')),  # ✅ Управління користувачами
    path('products/', views.products, name='products'),  # ✅ Продукти
    path('contact/', views.contact, name='contact'),  # ✅ Контакти
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),  # ✅ Панель адміністратора
]

# ✅ Додай `static()` для медіафайлів у кінці
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
