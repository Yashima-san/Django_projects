from django.shortcuts import render

def counter(request):
    word = None
    text = ''
    i = False

    if request.method == 'POST':
        # Получаем текст из формы
        text = request.POST.get('texttocount', '')

        # Проверяем, что текст не пустой
        if text.strip():
            # Разделяем текст на слова и считаем количество
            words = text.split()
            word = len(words)
            i = True

    # Возвращаем шаблон с данными
    return render(request, 'counter.html', {'word': word, 'text': text, 'i': i})