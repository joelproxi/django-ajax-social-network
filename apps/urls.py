from django.urls import path

from . import views


urlpatterns = [
	path('create-post/', views.create_post, name='create_post'),
	path('post/<int:post_id>/edit/', views.update_post, name='update_post'),
	path('comment/<int:post_id>/add/', views.add_comment, name='add_comment'),
	path('comment/<int:post_id>/<int:id>/edit/', views.update_comment, name='update_comment'),
	path('', views.post_list, name='post_list'),
 
	path('ajax/', views.like_item, name='like_item'),
	path('ajax-add-comment/', views.add_ajax_comment, name='add_ajax_comment'),
	path('ajax-follow/', views.follow_user, name='follow_user'),
 
	
]
