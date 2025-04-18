# users/urls.py
from django.urls import path
from notifications.views import NotificationViewList
from . import views

urlpatterns = [
    path('', views.OrderTemplateView.as_view(), name='order_list'),
    path('api/orders/', views.OrderListCreateAPIView.as_view(), name='api-order-list'),
    path('api/orders/<str:order_id>/', views.OrderDetailAPIView.as_view(), name='order-detail'),
    path('api/orders/<str:order_id>/close/', views.OrderClosureAPIView.as_view(), name='order-close'),
    path('accounting/', views.AccountingTemplateView.as_view(), name='accounting'),
    path('api/accounting/', views.AccountingListAPIView.as_view(), name='api-accounting-list'),
    path('api/accounting/<str:order__order_id>/', views.AccountingUpdateAPIView.as_view(), name='accounting-update'),
    path('api/manager-stats/', views.manager_stats, name='manager_stats'),
    path('api/dispatcher-stats/', views.dispatcher_stats, name='dispatcher_stats'),
    path('manager-stats/', views.ManagerStatsTemplateView.as_view(), name='manager_stats_page'),
    path('dispatcher-stats/', views.DispatcherStatsTemplateView.as_view(), name='dispatcher_stats_page'),
    path('edit-order/<str:order_id>/', views.edit_order_page, name='edit_order_page'),
    path('api/orders/<str:order_id>/update/', views.update_order, name='update_order'),
    path('api/orders/<str:order_id>/delete/', views.delete_order, name='delete_order'),
    path('login/', views.custom_login_view, name='custom_login'),
    path('logout/', views.custom_logout_view, name='custom_logout'),
    path('create-order/', views.create_order_view, name='create_order'),
    path('close-order/<str:order_id>/', views.close_order_page, name='close_order'),
    path('filter/', views.FilterTemplateView.as_view(), name='filter'),
    path('filter-order/<str:order_id>/', views.filter_order_view, name='filter_order'),
    path('statistics/', views.StatisticsTemplateView.as_view(), name='statistics'),
    path('mark-paid/<str:order_id>/', views.mark_paid_view, name='mark_paid'),
    path('return-order/<str:order_id>/', views.return_order_to_dispecher, name='return_order'),
    path('api/firma-suggestions/', views.firma_suggestions, name='firma_suggestions'),
    path('accounting/export/excel/', views.export_accounting_excel, name='export_accounting_excel'),
    path('accounting/export/pdf/', views.export_accounting_pdf, name='export_accounting_pdf'),
    path('notifications/', NotificationViewList.as_view(), name='notifications'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('notifications/', views.NotificationViewList.as_view(), name='notifications'),
]
