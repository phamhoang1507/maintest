from django.contrib import admin
from django.urls import path, include
from . import views
from  rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('post',views.PostViewSet)
router.register('users',views.UserViewSet)
# /post/get
# /post/post
# /post/id/up
# /post/id/de
# /post/id/get

urlpatterns = [
    # path("post/getall", views.ListPostView.as_view()),
    # path("post/searchname/", views.SearchNamePostView.as_view(),name='search_name'),
    # path("post/searchid/<int:pk>", views.SearchPostView.as_view()),
    # path("post/create",views.CreatePostView.as_view()),
    # path("post/update/<int:pk>",views.UpdatePostView.as_view()),
    # path("post/delete/<int:pk>",views.DeletePostView.as_view()),
    path('',include(router.urls)),


]