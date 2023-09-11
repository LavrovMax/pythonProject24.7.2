from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

def test_add_new_pet_with_no_valid_age(name='Барсик', animal_type='Кот',
                                     age='-99', pet_photo='images/cat.jpg'):
    """Проверяем что можно добавить питомца с отрицательным возрастом"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == '400'
    assert result['name'] == name
    """на сайт питомец добавляется, однако это является ошибкой т.к. возраст не может быть отрицательным"""


def test_add_new_pet_with_no_valid_name(name='@@@', animal_type='двортерьер',
                                     age='2', pet_photo='images/cat.jpg'):
    """Проверяем что можно добавить питомца с именем состоящим из символов"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == '400'
    assert result['name'] == name
    """на сайт питомец добавляется, однако это является ошибкой т.к. имя не должно состоять из символов"""


def test_add_new_pet_with_no_valid_type(name='Барбоскин', animal_type='12!!%%%*',
                                     age='7', pet_photo='images/cat.jpg'):
    """Проверяем что можно добавить питомца с некоректным типом питомца"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == '400'
    assert result['name'] == name
    """на сайт питомец добавляется, однако это является ошибкой т.к. тип указан некоректно"""

def  test_add_new_pet_with_no_valid_photo(name='Барбоскин', animal_type='cat',
                                     age='7', pet_photo='images/No_valid.pdf'):
    """Проверяем что можно добавить питомца с некоректным фото"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == '400'
    assert result['name'] == name
    """на сайт питомец добавляется, однако без фото"""


def test_successful_update_self_pet_info_no_valid_name(name='!!!', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 400 и имя питомца соответствует заданному
        assert status == 400
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")
    """информация о питомце на сайте будет обновлена, однако это является ошибкой так как имя питомца некоректное"""


def test_successful_update_self_pet_info_no_valid_type(name='!!!', animal_type='%%%%%', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 400 и имя питомца соответствует заданному
        assert status == 400
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")
    """информация о питомце на сайте будет обновлена, однако это является ошибкой так как тип питомца некоректен"""

def test_successful_update_self_pet_info_no_valid_age(name='тьфу', animal_type='Котэ', age='Десять'):
    """Проверяем возможность обновления информации о питомце с некоректным возрастом"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 400 и имя питомца соответствует заданному
        assert status == 400
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")
    """информация о питомце на сайте будет обновлена, однако это является ошибкой так как возраст указан некоректно"""

def test_add_new_pet_without_photo_no_valid_age(name= 'Дыгырпыр', animal_type= 'Носорог', age= '~~~'):
    """Проверяем возможность добавить нового питомца без фото"""
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_information_about_new_pet_without_photo(auth_key, name, animal_type, age)
    # Сверяем полученый ответ с ожидаемым результатом
    assert status == 400
    assert result['name'] == name
    """Питомец добовляется с некоректным возрастом"""


def test_add_photo_of_pet(pet_photo='images/cat.jpg'):
    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Берём id первого питомца из списка и отправляем запрос на добавление фото
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и что добавлена наша фотография
    assert status == 200
    assert result['pet_photo'] == pet_photo
    """не смог сделать данный тест, постоянно отключает от сервера:(Connection aborted)"""