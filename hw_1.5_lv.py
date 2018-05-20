# coding=utf-8

dict_of_students = {
    10001: {
        'first_name': 'Максим', 'last_name': 'Волков', 'sex': 'male', 'it_experience': True, 'regular_score': [7, 8, 7, 8, 9], 'exam_score': 9
    },
    10002: {
        'first_name': 'Александр', 'last_name': 'Щербаков', 'sex': 'male', 'it_experience': False, 'regular_score': [6, 7, 5, 6, 6], 'exam_score': 7
    },
    10003: {
        'first_name': 'Алексей', 'last_name': 'Чернов', 'sex': 'male', 'it_experience': True, 'regular_score': [6, 9, 5, 8, 8], 'exam_score': 8
    },
    10004: {
        'first_name': 'Виктория', 'last_name': 'Новикова', 'sex': 'female', 'it_experience': False, 'regular_score': [5, 6, 5, 6, 6], 'exam_score': 6
    },
    10005: {
        'first_name': 'Анна', 'last_name': 'Епифанова', 'sex': 'female', 'it_experience': True, 'regular_score': [7, 6, 8, 7, 7], 'exam_score': 7
    },
    10006: {
        'first_name': 'Елена', 'last_name': 'Краснова', 'sex': 'female', 'it_experience': False, 'regular_score': [5, 7, 6, 6, 5], 'exam_score': 7
    },
    10007: {
        'first_name': 'Андрей', 'last_name': 'Златарев', 'sex': 'male', 'it_experience': True, 'regular_score': [8, 8, 8, 7, 7], 'exam_score': 8
    },
    10008: {
        'first_name': 'Сергей', 'last_name': 'Полывяный', 'sex': 'male', 'it_experience': False, 'regular_score': [6, 6, 5, 5, 7], 'exam_score': 7
    },
    10009: {
        'first_name': 'Ольга', 'last_name': 'Ершова', 'sex': 'female', 'it_experience': True, 'regular_score': [7, 7, 7, 7, 7], 'exam_score': 8
    },
    10010: {
        'first_name': 'Михаил', 'last_name': 'Токовинин', 'sex': 'male', 'it_experience': True, 'regular_score': [9, 9, 8, 8, 8], 'exam_score': 9
    }
}


def mark_average_count_in_group(mark_type):
    """Функция получает в качестве атрибута ключ словаря,
    вложенного в словарь dict_of_students и делает
    подсчет среднего значения с выводом результатов.
    """

    marks_list = []
    for student in dict_of_students.values():
        if mark_type == 'дз':
            marks_list = marks_list + student['regular_score']
        elif mark_type == 'экз':
            marks_list.append(student['exam_score'])
        else:
            print('Неверный тип оценки, повторите ввод.')
            break

    if len(marks_list) == 0:
        print('Подсчет невозможен.')
    else:
        print(('Средняя оценка по {} в группе: {}\n').format(mark_type, round(sum(marks_list)/ len(marks_list), 2)))


gender_dict = {'муж': 'male', 'жен': 'female'}  # Этот словарь необходим для функции подсчета оценок с учетом пола
gender_input_dict = {'муж': 'мужчинам', 'жен': 'женщинам'}


def mark_average_count_in_group_gender_of_student(sex_type, mark_type):
    """Функция получает на входе 2 аргумента и делает подсчет средней
    оценки с учетом введенных параметров.
    """

    marks_list = []
    for student in dict_of_students.values():
        if student['sex'] == gender_dict[sex_type]:
            if mark_type == 'дз':
                marks_list = marks_list + student['regular_score']
            elif mark_type == 'экз':
                marks_list.append(student['exam_score'])
            else:
                print('Неверный тип оценки, повторите ввод.')
                return

    if len(marks_list) == 0:
        print('Подсчет невозможен.')
    else:
        print('Средняя оценка по {0} за {1} в группе {2}\n'.format(gender_input_dict[sex_type], mark_type,
                                                                   round(sum(marks_list)/ len(marks_list), 2)))

def run_mark_average_count_in_group_gender_of_student():
    sex_type = input('Введите пол студента (муж/жен)').lower()
    mark_type = input('Введите тип работы (дз/экз):').lower()
    mark_average_count_in_group_gender_of_student(sex_type, mark_type)


experience_dict = {'с опытом': True, 'без опыта': False}  # Словарь для подсчета среднего значение с учетом опыта


def mark_average_count_in_group_based_on_experience(experience_value, mark_type):
    """Функция производит посчет среднего значение оценок с учетом опыта и типа оценки."""
    marks_list = []
    for student in dict_of_students.values():
        if student['experience'] == experience_dict[experience_value]:
            if mark_type == 'дз':
                marks_list = marks_list + student['regular_score']
            elif mark_type == 'экз':
                marks_list.append(student['exam_score'])

            else:
                print('Неверный тип оценки, повторите ввод.')
                break

    if len(marks_list) == 0:
        print('Подсчет невозможен.')
    else:
        print(('Средняя оценка студентов {} по {} в группе {}\n').format(experience_value, mark_type,
                                                                         round(sum(marks_list)/ len(marks_list), 2)))


def run_mark_average_count_in_group_based_on_experience():
    experience_value = input('Выберите наличие опыта (с опытом/без опыта)').lower()
    mark_type = input('Введите тип работы (дз/экз):').lower()
    mark_average_count_in_group_based_on_experience(experience_value, mark_type)


def get_integral_score():
    d = {}
    for number, student in dict_of_students.items():
        student_data = 0
        integral_score = 0
        integral_score = ((sum(student['regular_score']) / len(student['regular_score'])) * 0.6 + student['exam_score'] * 0.4)
        student_data = round(integral_score, 2)
        d[number] = student_data
    return d


def max_integral_score():
    max_lst = []
    dict_with_integral_score = get_integral_score()
    inverse = [(value, key) for key, value in dict_with_integral_score.items()]
    for j in inverse:
        if j[0] == max(inverse)[0]:
            max_lst.append(j)
    return max_lst


def get_name_best_students():
    best_students_number = max_integral_score()
    best_student_name = []
    for i in best_students_number:
        for number, student in dict_of_students.items():
            if number == i[1]:
                best_student_name += [dict_of_students[number]['first_name'], dict_of_students[number]['last_name']]
    if len(best_student_name) > 2:
        print(
            ('Лучшие студенты:\n {} с интегральной оценкой {}\n').format(best_student_name, best_students_number[0][0]))
    elif len(best_student_name) == 2:
        print(
            ('Лучший студент:\n {} с интегральной оценкой {}\n').format(best_student_name, best_students_number[0][0]))
    return


def main_def():
    while True:
        user_choice = input('''Выберите действие:
t - узнать среднюю оценку за ДЗ или экзамен; 
g - узнать среднюю оценку за ДЗ или экзамен с учетом пола студента;
e - узнать среднюю оценку за ДЗ или экзамен с учетом опыта студента;
b - определить лучшего студента;
q - выход
Введите ваш выбор тут: \n''').lower()
        if user_choice == 't':
            mark_average_count_in_group(input("Введите тип работы (дз/экз):").lower())
        elif user_choice == 'g':
            run_mark_average_count_in_group_gender_of_student()
        elif user_choice == 'e':
            run_mark_average_count_in_group_based_on_experience()
        elif user_choice == 'b':
            get_name_best_students()
        elif user_choice == 'q':
            print('Прорамма завершена')
            break
        else:
            print('Ошибка ввода, пожалуйста повторите.')


main_def()
