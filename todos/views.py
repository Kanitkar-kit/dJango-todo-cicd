from django.http import JsonResponse
from .models import Todo


def todo_list(request):
    todos = list(
        Todo.objects.values("id", "title", "completed", "created_at")
    )
    return JsonResponse(todos, safe=False)
