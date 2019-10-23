from django.urls import path,include
from .views import api_library_list_view,api_library_details_view,\
    api_member_list_view,api_member_details_view,api_author_list_view,\
    api_author_details_view,api_borrows_list_view,api_borrows_details_view,\
    api_library_update_list_view,api_library_delete_view,api_library_post_view
from rest_framework import routers
from . import views


# router = routers.DefaultRouter()
# router.register('library',views.BookView)
# router.register('library',views.MemberView)
# router.register('library',views.AuthorView)
# router.register('library',views.BorrowsView)
app_name = 'libraryapp'

urlpatterns = [
    path('library', api_library_list_view, name='list-libraries'),
    path('library/<int:pk>/', api_library_details_view, name='library-details'),
    # path('library/<pk>/update/', api_library_update_list_view, name='library_update'),
    # path('library/<pk>/delete',api_library_delete_view,name='library_delete'),
    path('library/create',api_library_post_view,name='library_create'),
    path('library/<pk>/delete',api_library_delete_view,name='library_delete'),

]