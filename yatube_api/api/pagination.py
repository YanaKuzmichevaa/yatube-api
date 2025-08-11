from rest_framework.response import Response
from rest_framework.pagination import BasePagination, LimitOffsetPagination


class SmartPagination(BasePagination):

    def paginate_queryset(self, queryset, request, view=None):
        if 'limit' in request.query_params or 'offset' in request.query_params:
            self.paginator = LimitOffsetPagination()
            return self.paginator.paginate_queryset(queryset, request, view)
        else:
            return list(queryset)

    def get_paginated_response(self, data):
        if hasattr(self, 'paginator'):
            return Response({
                'count': self.paginator.count,
                'next': self.paginator.get_next_link(),
                'previous': self.paginator.get_previous_link(),
                'results': data
            })
        else:
            return Response(data)
