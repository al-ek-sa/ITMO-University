# Author = Lishik Aleksandra Yuryevna
# Group = P3106
# Date = 11.10.2025
# Option 503302%3=1
# Task 3
import re
from collections import defaultdict
def change_adjective_cases(text, word_number):
    pattern = re.compile(r'\b(\w+?)(?:ый|ий|ой|ая|яя|ое|ее|ые|ие|ого|его|ой|ей|ому|ему|ую|юю|ым|им|ыми|ими|ом|ем|ых|их)\b')
    groups = defaultdict(list)
#хранение позиций
    word_positions = []
    for match in pattern.finditer(text):
        original_word = match.group(0)
        base = match.group(1).lower()
        
        groups[base].append(original_word)
    
        word_positions.append((match.start(), match.end(), base, original_word))
    new_text_parts = []
    last_pos = 0 
    for start, end, base, original in word_positions:
        new_text_parts.append(text[last_pos:start])
        if len(groups[base]) > 1:
            idx = max(0, min(word_number-1, len(groups[base])-1))
            replacement = groups[base][idx]
            if original[0].isupper():
                replacement = replacement[0].upper() + replacement[1:]
            new_text_parts.append(replacement)
            (f"Заменяем '{original}' на '{replacement}' (группа '{base}')")
        else:
            new_text_parts.append(original)
        last_pos = end
    new_text_parts.append(text[last_pos:])
    return ''.join(new_text_parts)
# Test 1
print("Тест 1")
text = """Футбольный клуб «Реал Мадрид» является 15-кратным обладателем главного
футбольного европейского трофея – Лиги Чемпионов. Данный турнир организован
Союзом европейских футбольных ассоциаций (УЕФА). Идея о континентальном
футбольном турнире пришла к журналисту Габриэлю Ано в 1955 году."""
selected_number = 3  # Вторая форма из каждой группы
print("Индекс:", selected_number)
print("Исходный текст:", text)
new_text = change_adjective_cases(text, selected_number)
print("Текст после замены:", new_text)
# Test 2
print("Тест 2")
text = """Синий розовый красный розовая Розового Красный Зеленого Розовому"""
selected_number = 2  # Вторая форма из каждой группы
print("Индекс:", selected_number)
print("Исходный текст:", text)
new_text = change_adjective_cases(text, selected_number)
print("Текст после замены:", new_text)
# Test 3
print("Тест 3")
text = """Старый дом стоял рядом с старой оградой и старым садом"""
selected_number = 2  # Вторая форма из каждой группы
print("Индекс:", selected_number)
print("Исходный текст:", text)
new_text = change_adjective_cases(text, selected_number)
print("Текст после замены:", new_text)
# Test 4
print("Тест 4")
text = """Большой город был полон большие улицы и большие дома. Мы видели красивые картины, красивая ваза и красивое здание."""
selected_number = 2  # Вторая форма из каждой группы
print("Индекс:", selected_number)
print("Исходный текст:", text)
new_text = change_adjective_cases(text, selected_number)
print("Текст после замены:", new_text)
# Test 5
print("Тест 5")
text = """Светлый день озарял светлую комнату и светлое будущее. Глубокий овраг, глубокая река и глубокое озеро."""
selected_number = 2  # Вторая форма из каждой группы
print("Индекс:", selected_number)
print("Исходный текст:", text)
new_text = change_adjective_cases(text, selected_number)
print("Текст после замены:", new_text)