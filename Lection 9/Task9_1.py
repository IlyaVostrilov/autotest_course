# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

from pathlib import Path


with open(Path('test_file/task1_data.txt'), 'r', encoding='utf-8') as f1:
    with open(Path('test_file/task1_answer.txt'), 'w', encoding='utf-8') as f2:
        for line in f1.readlines():
            norm_line = ''.join([i for i in line if not i.isdigit()])
            f2.write(norm_line)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
