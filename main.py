import numpy as np


def game_core_v1(number):
    '''
        Просто угадываем на random, никак не используя информацию о больше или
        меньше. Функция принимает загаданное число и возвращает число попыток
    '''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1, 101) # предполагаемое число
        if number == predict:
            return(count) # выход из цикла, если угадали


def game_core_v2(number):
    '''Учитываем больше меньше в грницах угадывания'''
    count = 0
    low = 1
    high = 100
    while True:
        count+=1
        predict = np.random.randint(low, high + 1) # предполагаемое число
        if number == predict:
            return(count) # выход из цикла, если угадали
        elif number > predict:
            # Число больше предсказания - дальше угадываем все числа больше
            low = predict + 1
        else:
            # Число меньше предсказания - дальше угадываем все числа меньше
            high = predict - 1


def game_core_v3(number):
    '''
        Учитываем больше меньше в грницах угадывания,
        используем метод половинного деления
    '''
    count = 0
    low = 1
    high = 100
    while True:
        count+=1
        predict = (high - low) // 2 + low # Выбираем середину текущего
                                          # диапазона
        if number == predict:
            return(count) # выход из цикла, если угадали
        elif number > predict:
            # Число больше предсказания - дальше угадываем все числа больше
            low = predict + 1
        else:
            # Число меньше предсказания - дальше угадываем все числа меньше
            high = predict - 1



def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


if __name__ == "__main__":
    print("Оригинальный вариант")
    score_game(game_core_v1)
    print("Вариант с учётом больше/меньше")
    score_game(game_core_v2)
    print("Метод половинного деления")
    score_game(game_core_v3)

