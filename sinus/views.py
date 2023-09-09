from django.shortcuts import render, redirect
import random
def register(request):
    if request.method == 'POST':
        a = request.POST.get('reg')
        return redirect('basic')
    return render(request, 'registration.html')
def basik(request):
    if request.method == 'POST':
        a = request.POST.get('game')
        if a == '1':
            return redirect('get_random_number')
        elif a == '2':
            return redirect('get_random_box')
        elif a == '3':
            return redirect('get_mathik')
        elif a == '4':
            return redirect('problems')
        elif a == '5':
            request.session.clear()
            return redirect('register')
    return render(request, 'base.html')
def get_random_number(request):
    if 'random_number' not in request.session:
        request.session['random_number'] = random.randint(1, 100)
        request.session['attempts'] = 0

    if request.method == 'POST':
        guessed_number = int(request.POST['guessed_number'])
        random_number = request.session['random_number']
        attempts = request.session['attempts'] + 1

        if guessed_number == random_number:
            request.session['random_number'] = random.randint(1, 100)
            request.session['attempts'] += 1
            message = f'Поздравляю, вы угадали число ({random_number})! Новое случайное число сгенерировано.'
        elif guessed_number < random_number:
            message = 'Попробуйте еще раз. Загаданное число больше.'
        else:
            message = 'Попробуйте еще раз. Загаданное число меньше.'
    else:
        message = 'Угадайте случайное число от 1 до 100.'
        attempts = 0
    random_number = request.session['random_number']

    return render(request, 'game_randomchick.html',{'random_number': random_number, 'message': message, 'attempts': attempts})
def get_random_box(request):
    if 'random_number' not in request.session:
        request.session['random_number'] = random.randint(1, 3)
        request.session['attempts'] = 0
    if request.method == 'POST':
        random_box = request.session['random_number']
        a = int(request.POST.get('box'))
        attempts = request.session['attempts']
        print(random_box)
        if a == random_box:
            request.session['random_number'] = random.randint(1, 3)
            request.session['attempts'] += 1
            message = f'ААААААААААААААААААААА МЕДВЕДЬ.ИЩИ ДРУГОГО'
        else:
            request.session['random_number'] = random.randint(1, 3)
            request.session['attempts'] = attempts
            message = f'Мне жаль,ты проиграл....................Но он ушел в другую коробку'
    else:
        message = 'Угадай в какой коробке спрятался медведь!'
        attempts = 0
    return render(request, 'game-box.html', {'message': message,'attempts': attempts})
def get_mathik(request):
    if 'random_number_one' not in request.session:
        request.session['random_number_one'] = random.randint(1, 100)
        request.session['random_number_two'] = random.randint(1, 100)
        request.session['objects'] = random.choice(['+', '-', '*', '/'])
        request.session['attempts'] = 0

    if request.method == 'POST':
        otvet = request.POST.get('otvet')
        random_number_one = request.session['random_number_one']
        random_number_two = request.session['random_number_two']
        operator = request.session['objects']
        attempts = request.session.get('attempts', 0) + 1

        try:
            otvet = int(otvet)
            if operator == '+':
                correct_answer = random_number_one + random_number_two
            elif operator == '-':
                correct_answer = random_number_one - random_number_two
            elif operator == '*':
                correct_answer = random_number_one * random_number_two
            elif operator == '/':
                if random_number_two == 0:
                    raise ZeroDivisionError("Деление на ноль!")
                correct_answer = random_number_one / random_number_two

            if otvet == correct_answer:
                request.session['attempts'] = attempts
                request.session['random_number_one'] = random.randint(1, 100)
                request.session['random_number_two'] = random.randint(1, 100)
                request.session['objects'] = random.choice(['+', '-', '*', '/'])
                message = 'Верно! Правильный ответ.'
            else:
                message = 'Неправильный ответ. Попробуйте еще раз.'
        except (ValueError, ZeroDivisionError):
            message = 'Ошибка: Введите корректный ответ.'

    else:
        message = 'Начнем математику!'
        attempts = 0

    random_number_one = request.session['random_number_one']
    random_number_two = request.session['random_number_two']
    operator = request.session['objects']

    return render(request, 'game-math.html', {'attempts': attempts, 'random_number_one': random_number_one, 'message': message, 'random_number_two': random_number_two, 'operator': operator})

def problems(request):
    return render(request, 'problems.html')

def make_problems(request):
    return render(request, 'make_problems.html')

