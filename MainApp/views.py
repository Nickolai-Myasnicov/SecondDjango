from django.shortcuts import render, HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from MainApp.models import Item

user = {
    "name": "Иван",
    "middle": "Петрович",
    "surname": "Сидоров",
}

#items = [
#    {"id": 1, "name": "Кросовки abibas", "quantity":5},
#    {"id": 2, "name": "Куртка кожанная", "quantity":2},
#    {"id": 3, "name": "Coca-cola 1 литр", "quantity":12},
#    {"id": 4, "name": "Картофель фри", "quantity":0},
#    {"id": 5, "name": "Кепка", "quantity":124},
#]


def main(request):
    return render(request, 'index.html')


def about(request):
    text = f"""
    Имя: {user['name']}<br>
    Отчество: {user['middle']}<br>
    Фамилия: {user['surname']}<br>
    """
    return HttpResponse(text)


def show_item(request, id):
    try:
        current_item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404
    context = {
        "item": current_item
    }
    return render(request, "item.html", context)


def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items.html", context)