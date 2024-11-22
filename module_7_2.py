def custom_write(file_name, strings):
    strings_positions = {}
    
    f = open(file_name, 'w', encoding='utf-8')  # Открываем файл

    # Цикл для записи строк в файл
    for index, string in enumerate(strings, start=1):
        start_byte = f.tell()  # Получаем текущую позицию в байтах
        f.write(string + '\n')  # Записываем строку в файл с переходом на новую строку
        strings_positions[(index, start_byte)] = string  # Сохраняем в словарь

    f.close()  # Закрываем файл

    return strings_positions

# Пример использования
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
