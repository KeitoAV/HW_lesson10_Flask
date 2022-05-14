import requests


def get_candidates():
    """Получаем список кандидатов из файла json"""
    candidates = requests.get(r'https://jsonkeeper.com/b/2J69')
    # print(candidates.status_code)
    candidates_json = candidates.json()  # получаем файл json
    # print(candidates_json)
    return candidates_json


# print(get_candidates())


def load_page():
    """Получаем данные всех кандидатов"""
    page_list = get_candidates()
    page = ""
    for data in page_list:
        page += 'Имя кандидата: ' + data['name'] + '\n' + \
                'Позиция кандидата: ' + data['position'] + '\n' + \
                'Навыки через запятую: ' + data['skills'] + '\n' + '\n'

    return '<pre>' + '\n' + page + '</pre>'


# print(load_page())

def get_img(x):
    """Получаем 'img' и данные одного кандидата по id"""
    img_read = get_candidates()
    img = ""
    for data in img_read:
        if data["id"] == x:
            img += '<img src =' + data["picture"] + '>' + '\n' + '<pre>' + '\n' + \
                   'Имя кандидата:' + data["name"] + '\n' + \
                   'Позиция кандидата:' + data["position"] + '\n' + \
                   'Навыки через запятую:' + data["skills"] + '\n' + '</pre>'

    return img


# print(get_img(5))


def get_skill(x):
    """Получаем кандидатов у которых есть 'skills'"""
    skill_read = get_candidates()
    skill = ""
    for data in skill_read:
        if x in data["skills"].title() or x in data["skills"].lower():
            skill += 'Имя кандидата: ' + data['name'] + '\n' + \
                     'Позиция кандидата: ' + data['position'] + '\n' + \
                     'Навыки через запятую: ' + data['skills'] + '\n' + '\n'

    return '<pre>' + '\n' + skill + '</pre>'


# print(get_skill('flask'))

def get_id(x):
    id_img = get_candidates()
    y = False
    for dict in id_img:
        if x == dict['id']:
            y = True
    return y


# print(get_id(7))
# print(get_id(70))


def get_skills(x):
    id_skill = get_candidates()
    y = False
    for dict in id_skill:
        if x in dict['skills']:
            y = True
    return y


# print(get_skills('flask'))
# print(get_skills('ничего'))


