# coding=utf-8
#  Условия задачи:
#  Имеется группа студентов, у каждого из которых есть следующие характеристики:
#  имя, фамилия, пол, предыдущий опыт в программировании (бинарная переменная),
#  5 оцененных по 10-бальной шкале домашних работ, оценка за экзамен по 10-балльной шкале.

group = {
    10001:
        {'name': 'Максим', 'surname': 'Волков', 'sex': 'male', 'it_experience': True, 'hw_score': [7, 8, 7, 8, 9], 'exam_score': 9},
    10002:
        {'name': 'Александр', 'surname': 'Щербаков', 'sex': 'male', 'it_experience': False, 'hw_score': [6, 7, 5, 6, 6], 'exam_score': 7},
    10003:
        {'name': 'Алексей', 'surname': 'Чернов', 'sex': 'male', 'it_experience': True, 'hw_score': [6, 9, 5, 8, 8], 'exam_score': 8},
    10004:
        {'name': 'Виктория', 'surname': 'Новикова', 'sex': 'female', 'it_experience': False, 'hw_score': [5, 6, 5, 6, 6], 'exam_score': 6},
    10005:
        {'name': 'Анна', 'surname': 'Епифанова', 'sex': 'female', 'it_experience': True, 'hw_score': [7, 6, 8, 7, 7], 'exam_score': 7},
    10006:
        {'name': 'Елена', 'surname': 'Краснова', 'sex': 'female', 'it_experience': False, 'hw_score': [5, 7, 6, 6, 5], 'exam_score': 7},
    10007:
        {'name': 'Андрей', 'surname': 'Златарев', 'sex': 'male', 'it_experience': True, 'hw_score': [8, 8, 8, 7, 7], 'exam_score': 8},
    10008:
        {'name': 'Сергей', 'surname': 'Полывяный', 'sex': 'male', 'it_experience': False, 'hw_score': [6, 6, 5, 5, 7], 'exam_score': 7},
    10009:
        {'name': 'Ольга', 'surname': 'Ершова', 'sex': 'female', 'it_experience': True, 'hw_score': [7, 7, 7, 7, 7], 'exam_score': 8},
    10010:
        {'name': 'Михаил', 'surname': 'Токовинин', 'sex': 'male', 'it_experience': True, 'hw_score': [9, 9, 8, 8, 8], 'exam_score': 9}
}


#  print('Студент {0} {1} получил на экзамене {2} баллов'.format(group[10001]['surname'], group[10001]['name'], group[10001]['exam_score']))
