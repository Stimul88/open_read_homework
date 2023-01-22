import os

dict_ = {}
file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'
file_name_4 = '4.txt'
with open('1.txt', 'rt', encoding='utf-8') as f:
    res1 = f.readlines()
    dict_[file_name_1] = (len(res1))

with open(file_name_2, 'rt', encoding='utf-8') as f:
    res2 = f.readlines()
    dict_[file_name_2] = (len(res2))

with open(file_name_3, 'rt', encoding='utf-8') as f:
    res3 = f.readlines()
    dict_[file_name_3] = (len(res3))

with open('4.txt', 'w', encoding='utf-8') as f:
    for w in sorted(dict_, key=dict_.get):
        f.write(w)
        f.write('\n')
        f.write(str(dict_[w]))
        f.write('\n')
        for i in range(dict_[w]):
            f.write(f'Cтрока номер {int(i)+1} файл номер {w[:-4]}')
            f.write('\n')






