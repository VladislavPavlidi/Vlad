# Cписки для хранения выбранных ответов

accoustics = []
electrics = []
ukuleles = []
basses = []

# Возможные результаты:

# Для аккустических гитар:

result1 = 'аккустическая гитара на нейлоновых струнах!'
result2 = 'классическая гитара!'
result3 = 'аккустическая гитара!'
result4 = 'полуаккустическая гитара!'

# Для электрических гитар:

result5 = 'электрогитара telecaster!'
result6 = 'электрогитара stratocaster!'
result7 = 'электрогитара les paul!'
result8 = 'электрогитара superstrat!'

# Для гитар укулеле:

result9 = 'Укулеле сопрано!'
result10 = 'Укулеле концерт!'

# Для басс гитар:

result11 = '4-струнная басс-гитара!'
result12 = '5-струнная басс-гитара!'

# Вопросы и варианты:

q1 = 'Выбери жанр, который больше подходит'
ac_chse1 = 'Классическая музыка'
el_chse1 = 'Рок'
uk_chse1 = 'Поп'
b_chse1 = 'Ритм-н-блюз'

q2 = 'Кто больше нравится?'
ac_chse2 = 'Johnny Cash'
el_chse2 = 'James Hetfield'
uk_chse2 = 'Elvis Presley'
b_chse2 = 'Eminem'

q3 = 'Чья музыка больше нравится?'
ac_chse3 = 'Beatles'
el_chse3 = 'Daft Punk'
uk_chse3 = 'Twenty one pilots'
b_chse3 = 'MC Hammer'

q4 = 'На что больше обращаешь внимание, когда слушаешь музыку?'
ac_chse4 = 'Ритм-гитару'
el_chse4 = 'Соло-гитару'
uk_chse4 = 'Вокал'
b_chse4 = 'Басс, барабаны'

q5 = 'Этим можно описать твои пальцы:'
ac_chse5 = 'Пальцы пианиста'
el_chse5 = 'Длинные'
uk_chse5 = 'Короткие'
b_chse5 = 'Пальцы-сардельки'

q6 = 'Выбери жанр, который хочешь играть:'
ac_chse6 = 'Авторские песни (дворовые)'
el_chse6 = 'Джаз'
uk_chse6 = 'Рэп'
b_chse6 = 'Блюз'

q7 = 'Как часто планируешь выходить с гитарой из дома?'
ac_chse7 = 'Часто'
el_chse7 = 'Иногда'
uk_chse7 = 'Везде со мной'
b_chse7 = 'Почти никогда'

q8 = 'Для чего гитара?'
ac_chse8 = 'Блестнуть перед противоположным полом'
el_chse8 = 'Записывать клипы, каверы, обственную музыку'
uk_chse8 = 'Чтобы не скучать в путешествиях'
b_chse8 = 'Наслаждаться игрой после тяжелого дня'

q9 = 'На каком уровне игры?'
ac_chse9 = 'Новичок'
el_chse9 = 'Профессионал'
uk_chse9 = 'Средний'
b_chse9 = 'Новичок, но хочу сесть и сразу начать играть'

q10 = 'Что для тебя важнее в гитаре?'
ac_chse10 = 'Универсальность'
el_chse10 = 'Возможность игры со звуком, точь-в-точь совпадающим в песне'
uk_chse10 = 'Небольшие габариты гитары'
b_chse10 = 'Простота в использовании'

q11 = 'Готов покупать дополнительное оборудование для своей гитары?'
ac_chse11 = 'Максимум медиатор и струны'
el_chse11 = 'В пределах разумного'
uk_chse11 = 'Нет'
b_chse11 = 'Да'

q12 = 'Это твоя первая гитара?'
ac_chse12 = 'Да'
el_chse12 = 'Люблю коллекционировать гитары'
uk_chse12 = 'Нет'
b_chse12 = 'Уже так много, что не знаю даже какую купить'


def add_in_question(aswr: input):
    """Добавляет цифру в нужный список, в зависимости от выбранного ответа"""
    if aswr == '1':
        accoustics.append(1)
    elif aswr == '2':
        electrics.append(1)
    elif aswr == '3':
        ukuleles.append(1)
    elif aswr == '4':
        basses.append(1)


def question(quest, choose1, choose2, choose3, choose4: list):
    """Выводит на экран вопрос, и 4 варианта ответа"""
    print(quest)
    print('1) ' + choose1)
    print('2) ' + choose2)
    print('3) ' + choose3)
    print('4) ' + choose4)


def easy_way(quest, choose1, choose2, choose3, choose4: list):
    """Берет нужный вопрос, 4 варианта ответа и выводит в виде анкеты, добавляя в списки нужные ответы"""
    question(quest, choose1, choose2, choose3, choose4)
    answer = input('Напишите цифру от 1 до 4')
    add_in_question(answer)


# Вывод на экран вопросы:


easy_way(q1, ac_chse1, el_chse1, uk_chse1, b_chse1)
easy_way(q2, ac_chse2, el_chse2, uk_chse2, b_chse2)
easy_way(q3, ac_chse3, el_chse3, uk_chse3, b_chse3)
easy_way(q4, ac_chse4, el_chse4, uk_chse4, b_chse4)
easy_way(q5, ac_chse5, el_chse5, uk_chse5, b_chse5)
easy_way(q6, ac_chse6, el_chse6, uk_chse6, b_chse6)
easy_way(q7, ac_chse7, el_chse7, uk_chse7, b_chse7)
easy_way(q8, ac_chse8, el_chse8, uk_chse8, b_chse8)
easy_way(q9, ac_chse9, el_chse9, uk_chse9, b_chse9)
easy_way(q10, ac_chse10, el_chse10, uk_chse10, b_chse10)
easy_way(q11, ac_chse11, el_chse11, uk_chse11, b_chse11)
easy_way(q12, ac_chse12, el_chse12, uk_chse12, b_chse12)

# Условия на которых выбирается ответ:

if len(accoustics) == len(electrics) == len(ukuleles) == len(basses):
    print('Твои вкусы очень специфичны, твоя гитара - семиструнная электро')
elif len(accoustics) > 6:
    print('Вам больше всего подходит ' + result4)
elif len(accoustics) > 5:
    print('Вам больше всего подходит ' + result3)
elif len(accoustics) > 4:
    print('Вам больше всего подходит ' + result2)
elif len(accoustics) > 3:
    print('Вам больше всего подходит ' + result1)
elif len(electrics) > 6:
    print('Вам больше всего подходит ' + result8)
elif len(electrics) > 5:
    print('Вам больше всего подходит ' + result7)
elif len(electrics) > 4:
    print('Вам больше всего подходит ' + result6)
elif len(electrics) > 3:
    print('Вам больше всего подходит ' + result5)
elif len(ukuleles) > 4:
    print('Вам больше всего подходит ' + result10)
elif len(ukuleles) > 3:
    print('Вам больше всего подходит ' + result9)
elif len(basses) > 4:
    print('Вам больше всего подходит ' + result12)
elif len(basses) > 3:
    print('Вам больше всего подходит ' + result11)
