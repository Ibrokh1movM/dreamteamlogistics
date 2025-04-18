from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.status == 'admin'


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.status == 'manager'


class IsDispecher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.status == 'dispecher'


class IsBugalter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.status == 'bugalter'


class IsFilter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.status == 'filter'
