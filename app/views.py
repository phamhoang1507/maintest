from django.http import JsonResponse
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework import  permissions,generics
#
# from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, get_object_or_404, \
#     RetrieveAPIView
#
# # Create your views here.
#
# class ListPostView(ListAPIView):
#     model=Post
#     serializer_class = PostSerializers
#
#     def get_queryset(self):
#            return Post.objects.all()
#
# class SearchPostView(RetrieveAPIView):
#     queryset = Post.objects.all()  # queryset để truy vấn tất cả các bài viết
#     serializer_class = PostSerializers
#
#     def get_object(self):
#         pk = self.kwargs.get('pk')
#         return get_object_or_404(Post, pk=pk)
#
#
# class SearchNamePostView(ListAPIView):
#     serializer_class = PostSerializers
#
#     def get_queryset(self):
#         # Lấy tham số tên từ request query string
#         search_name = self.request.query_params.get('name', None)
#
#         # Nếu không có tham số tên, trả về tất cả các bài viết
#         if not search_name:
#             return Post.objects.all()
#
#         # Lọc bài viết dựa trên tên
#         return Post.objects.filter(title=search_name)
#
#
# class CreatePostView(CreateAPIView):
#     model=Post
#     serializer_class = PostSerializers
#
#     def create(self, request, *args, **kwargs):
#         serializers=PostSerializers(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return JsonResponse(
#                 {'message':'Create a new Post Successfull'},
#                 status=status.HTTP_201_CREATED)
#         return JsonResponse({
#             'message':'Create a new Post UnSuccessfull'
#         },status=status.HTTP_400_BAD_REQUEST)
#
# class UpdatePostView(UpdateAPIView):
#     model=Post
#     serializer_class = PostSerializers
#
#     def update(self, request, *args, **kwargs):
#         post=Post.objects.get(id=kwargs.get('pk'))
#         serializers=PostSerializers(post,data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return JsonResponse({
#                 'message':'Update Post Successfull'
#             },status=status.HTTP_200_OK)
#
#         return JsonResponse({
#             'message':'Update Post UnSuccessfull'
#         },status=status.HTTP_400_BAD_REQUEST)
#
# class DeletePostView(DestroyAPIView):
#     model=Post
#     serializer_class = PostSerializers
#
#     def delete(self, request, *args, **kwargs):
#         post=get_object_or_404(Post,id=kwargs.get('pk'))
#         post.delete()
#         return JsonResponse({
#             'message':'Delete Post Successsful'
#         },status=status.HTTP_200_OK)
#
#
#
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    # permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser,]
    # def get_permissions(self):
    #     if self.action=='list':
    #         return [permissions.AllowAny()]
    #
    #     return  [permissions.IsAuthenticated()]


class UserViewSet(viewsets.ViewSet , generics.CreateAPIView,generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializers
    # swagger_schema=None

    # @swagger_auto_schema(
    #     operation_description='Api User',
    #     responses={
    #         status.HTTP_200_OK:UserSerializers()
    #     }
    # )

    # def get_permissions(self):
    #     if self.action=='retrieve':
    #         return [permissions.IsAuthenticated()]
    #     return [permissions.AllowAny()]