
from django.contrib import admin
from django.urls import path, include,re_path
from mzakapp import views
from mzakapp.models import User
# from django.views.generic import TemplateView
from rest_framework import routers 
from mzakapp.views import HomeViewSet
from django.views.generic import TemplateView,ListView

router = routers.DefaultRouter() 
# router.register(r'home', views.CustomBrowsableAPIRenderer) 
router.register(r'homes',views.HomeViewSet)
  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls')),
    path("ac/",views.home, name="users"),
    # path("user/",views.home_view, name="home_view"),
    # path('show/',views.show),  
    # path("delete/<int:id>/",views.delete),
    # path("update/<int:id>/", views.update),
    # path('users/',TemplateView.as_view(template_name="home.html")),
    path('user-list/',views.UserList, name="user-list"),
    # path('user-detail/<int:pk>/',views.UserDetail, name="user-detail"),
    # path('user-create/',views.UserCreate, name="user-create"),
    path('user-update/<int:pk>/',views.UserUpdate, name="user-update"),
    path('user-delete/<int:pk>/',views.UserDelete, name="user-delete"),
    path('users/', views.ProfileList.as_view()),
    path('user_detail/', views.ProfileDetail.as_view()),
    # re_path(r'^upload/(?P<filename>[^/]+)$', views.FileUploadView.as_view()),
    path('generic_detail/<int:pk>/', views.UserDetail.as_view()),
    # static pages
    path('view/',TemplateView.as_view(template_name = 'static.html')),
    # List and Display Data from DB (use object_list in templates)
    path('views/',ListView.as_view(model = User,template_name = 'static.html',context_object_name = "User_objects"))

]
