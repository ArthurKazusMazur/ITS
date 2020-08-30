from collections import Counter


def word_count_within_file(filename):
    separators = ['.', ',', '!', '?', ':', ';']
    f = open(filename, 'r', encoding='UTF-8')
    line = f.readlines()

    # привдение разделителей к одному виду
    # и фомирование однородного списка слов из тектса файл
    for char in line[0]:
        if char in separators:
            line[0] = line[0].replace(char, "")
            words = line[0].split()

    # подсчет и вывод на печать количества входжений слов в тексте файла
    nums = []
    d = dict(Counter(words))
    for key in d:
        nums.append(d.get(key))
    print(nums)
    f.close()


word_count_within_file('test.txt')
