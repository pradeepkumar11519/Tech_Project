from rest_framework.pagination import CursorPagination

class MyContestPagination(CursorPagination):
    page_size = 6
    ordering = "-OnGoing"