from clients.models import User
from clients.utils import SearchFilterSet


class UserFilter(SearchFilterSet):
    """
    Фильтр пользователей
    """

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'gender',
        )

    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)  # type: User
        return qs