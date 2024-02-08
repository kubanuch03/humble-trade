
from rest_framework import permissions
class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Пользователи-администраторы могут выполнять любые действия,
    в то время как остальные могут только просматривать.
    """
    def has_permission(self, request, view):
        # Разрешение на чтение всегда разрешено
        if request.method in permissions.SAFE_METHODS:
            return True
        # Проверяем, является ли пользователь администратором
        return request.user and request.user.is_staff