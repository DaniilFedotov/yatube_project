from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница новейшего веб-приложения!')


def group_posts(request, any_slug):
    return HttpResponse(f'Вы ввели в адресную строку что-то странное: {any_slug}')
