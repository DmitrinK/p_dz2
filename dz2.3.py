"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
времени года относится месяц (зима, весна, лето, осень). Напишите решения через
list и через dict.
"""
season_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
count_list = -1
while count_list < len(season_list):
    if count_list < 2:
        season_list[count_list] = "Зима"
    elif 2 < count_list < 5:
        season_list[count_list] = "Весна"
    elif 5 < count_list < 8:
        season_list[count_list] = "Лето"
    else:
        season_list[count_list] = "Осень"
    count_list = count_list + 1
user_num = int(input())
print(season_list[user_num])
