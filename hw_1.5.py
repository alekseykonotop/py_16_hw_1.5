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
# 1.
# Среднюю оценку за домашние задания и за экзамен по всем группе в следующем виде:
# Средняя оценка за домашние задания по группе: X
# Средняя оценка за экзамен: Y
#
sex_dict = {'male': 'мужчин', 'female': 'женщин'}  # Словарь для вывода результатов вычислений


def get_average_score(type_score, sex_type='all', experience='not_matter'):
    """Функция одновременно принимает от одного до 2-х аргументов.

    При передаче только type_score производится расчет среднего значение оценки по ДЗ и
    экзамену по всей группе. При приеме type_score и sex_type производится расчет
    среднего значение оценки по ДЗ и экзамену с учетом пола.
    При приеме type_score и experience производиться расчет средней оценки по
    ДЗ и экзамену с учетом опыта.
    """

    all_scores_list = []
    # Подсчет среднего значение оценки по ДЗ и экзамену по всей группе
    if sex_type == 'all':
        if type_score == 'hw_score' and experience == 'not_matter':
            for student_data in group.values():
                for score in student_data[type_score]:
                    all_scores_list.append(score)  # Получили список всех оценок за ДЗ
            print('Средняя оценка за домашние задания по группе: {0:.2}'.format(sum(all_scores_list) / len(all_scores_list)))

        elif type_score == 'exam_score' and experience == 'not_matter':
            for student_data in group.values():
                all_scores_list.append(student_data[type_score])  # Получили список всех оценок за экзамены
            print('Средняя оценка за экзамен: {0:.2}'.format(sum(all_scores_list) / len(all_scores_list)))

    # Подсчет среднего значение оценки по ДЗ и экзамену с учетом пола
    else:
        if type_score == 'hw_score':
            for student_data in group.values():
                if student_data['sex'] == sex_type:
                    for score in student_data[type_score]:
                        all_scores_list.append(score)  # Получили список всех оценок за ДЗ по конкретному полу
            print(
                'Средняя оценка за домашние задания у {0}: {1:.2}'.format(sex_dict[sex_type], sum(all_scores_list) / len(all_scores_list)))

        elif type_score == 'exam_score':
            for student_data in group.values():
                if student_data['sex'] == sex_type:
                    all_scores_list.append(student_data[type_score])  # Получили список всех оценок за экзамены по конкретному полу
            print('Средняя оценка за экзамен у {0}: {1:.2}'.format(sex_dict[sex_type], sum(all_scores_list) / len(all_scores_list)))

    # Подсчет средней оценки по ДЗ и экзамену с учетом опыта
    if type_score == 'hw_score' and experience != 'not_matter':
        for student_data in group.values():
            if student_data['it_experience'] == experience:
                for score in student_data[type_score]:
                    all_scores_list.append(score)  # Получили список всех оценок за ДЗ по указанному опыту
        if experience:
            print('Средняя оценка за домашние задания у студентов с опытом: {0:.2}'.format(sum(all_scores_list) / len(all_scores_list)))
        else:
            print('Средняя оценка за домашние задания у студентов без опыта: {0:.2}'.format(sum(all_scores_list) / len(all_scores_list)))

    elif type_score == 'exam_score' and experience != 'not_matter':
        for student_data in group.values():
            if student_data['it_experience'] == experience:
                all_scores_list.append(student_data[type_score])  # Получили список всех оценок за экзамены с учетом опыта
        if experience:
            print('Средняя оценка за экзамен у студентов с опытом: {0:.2}'.format(sum(all_scores_list) / len(all_scores_list)))
        else:
            print('Средняя оценка за экзамен у студентов без опыта: {0:.2}'.format(sum(all_scores_list) / len(all_scores_list)))


get_average_score('hw_score')
get_average_score('exam_score')
print('=====')
get_average_score('hw_score', sex_type='male')
get_average_score('exam_score', sex_type='male')
print('-----')
get_average_score('hw_score', sex_type='female')
get_average_score('exam_score', sex_type='female')
print('=====')
get_average_score('hw_score', experience=True)
get_average_score('exam_score', experience=True)
print('-----')
get_average_score('hw_score', experience=False)
get_average_score('exam_score', experience=False)


