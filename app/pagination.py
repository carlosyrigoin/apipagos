from rest_framework.pagination import PageNumberPagination

class SimplePagination(PageNumberPagination):
    page_size = 1
    page_query_param = "page_size"
    max_page_size = 2000