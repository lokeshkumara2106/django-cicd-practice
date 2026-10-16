from django.http import JsonResponse


def health(request):
    return JsonResponse({
        "status": "ok",
        "application": "django-cicd-practice"
    })