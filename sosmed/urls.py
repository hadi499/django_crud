from django.urls import path
from . import views

urlpatterns = [    
    path('',views.list, name='list' ),
    path('delete/<int:pk>', views.delete, name='delete'),
	path('update/<int:pk>', views.update, name='update'),
	path('create/',views.create, name='create'),
]