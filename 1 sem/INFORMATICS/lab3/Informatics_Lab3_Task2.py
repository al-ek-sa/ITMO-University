# Author = Lishik Aleksandra Yuryevna
# Group = P3106
# Date = 09.10.2025
# Option 503302%5=2
# Task 2
# Студент Вася очень любит курс «Компьютерная безопасность». Однажды Васе
# задали домашнее задание зашифровать данные, переданные в сообщении. Недолго
# думая, Вася решил заменить все целые числа на функцию от этого числа. Функцию
# он придумал не сложную 5x^3−13,где x−исходное число . Помогите Васе с его домашним заданием.
#Предусмотреть ситуацию, когда в тексте будут не только целые числа, но и любые символы.
import re
def task2(text):
    def num (match):
        a1 = match.group()
        try:
            a1 =a1.replace(",", ".")
            x = float(a1)
            y = 5 * (x ** 3) - 13
            return str(y)
        except ValueError:
            return a1
    pattern = r'\-?\+?\d+\.?\,?\d*'
    result = re.sub(pattern, num , text)
    return result
# Test 1
print("Тест 1")
print("Текст: 15 + 22 = 37")
text = "15 + 22 = 37"
result = task2(text)  
print("Вывод:", result) 
# Test 2
print("Тест 2")
print("Текст: ВТ существует уже 983 лет")
text = "ВТ существует уже 983 лет"
result = task2(text) 
print("Вывод:", result) 
# Test 3
print("Тест 3")
print("Текст: Баланс на карте у транжиры -500 рублей")
text = "Баланс на карте у транжиры -500 рублей"
result = task2(text)  
print("Вывод:", result) 
# Test 4
print("Тест 4")
print("Текст: 1001 копейка равна 10,01 рубля")
text = "1001 копейка равна 10,01 рубля"
result = task2(text)  
print("Вывод:", result) 
# Test 5
print("Тест 5")
print("Текст: 1 + 0 = 1")
text = "1 + 0 = 1"
result = task2(text)
print("Вывод:", result) 
# Test 6
print("Тест 1")
print("Текст: 8 9 20 -7 -1,023 2,37")
text = "8 9 20 -7 -1.023 2.37"
result = task2(text)
print("Вывод:", result) 