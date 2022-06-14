from django.shortcuts import render
from .Forms import KeyWordForm
from .image_list_generator import generate_image_list
from .image_table import Image_Table

def index(request):
    context = {"key_word" : 'магазин игрушек'}
    if request.method == 'POST':
        form = KeyWordForm(request.POST)
        if form.is_valid():
            table  = Image_Table(form.cleaned_data['word'])
            context["form"] = form
            context["b"] = form.cleaned_data
            context["table"] = table
    return render(request, 'generator/index.html',context)
# Create your views here.
'''
--сделать страницу документации
--сделать стилизованное место под картиники(поиграться со стилями для таблицы)
--прикрутить вывод от артема
--вывести в боевое состояние:
    1 сделать страницу-ошибку(если проверяющие захотят посетить не тот адрес)
    2 дать возможность заходить на сайт с других компов
    3 выгрузить это на Heroku
'''