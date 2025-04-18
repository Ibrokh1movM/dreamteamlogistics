from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.OrderTemplateView.as_view(), name='order-list'),
    path('api/orders/', views.OrderListCreateAPIView.as_view(), name='api-order-list'),
    path('api/orders/<str:order_id>/', views.OrderDetailAPIView.as_view(), name='order-detail'),
    path('api/orders/<str:order_id>/close/', views.OrderClosureAPIView.as_view(), name='order-close'),
    path('accounting/', views.AccountingTemplateView.as_view(), name='accounting'),
    path('api/accounting/', views.AccountingListAPIView.as_view(), name='api-accounting-list'),
    path('api/accounting/<str:order__order_id>/', views.AccountingUpdateAPIView.as_view(), name='accounting-update'),
    path('login/', views.custom_login_view, name='custom_login'),
    path('logout/', views.custom_logout_view, name='custom_logout'),
    path('create-order/', views.create_order_view, name='create_order'),
    path('close-order/<str:order_id>/', views.close_order_page, name='close_order'),
    path('filter/', views.FilterTemplateView.as_view(), name='filter'),
    path('filter-order/<str:order_id>/', views.filter_order_view, name='filter_order'),
    path('statistics/', views.StatisticsTemplateView.as_view(), name='statistics'),
    path('mark-paid/<str:order_id>/', views.mark_paid_view, name='mark_paid'),
    path('undo-payment/<str:order_id>/', views.undo_payment_view, name='undo_payment'),
    path('return-order/<str:order_id>/', views.return_order_to_dispecher, name='return_order'),
    path('chat/', views.ChatTemplateView.as_view(), name='chat'),
    path('chat/post/', views.post_chat_message, name='post_chat_message'),
    path('users/', include('users.urls')),
]
