import sender_stand_request
import data


def get_kit_body(name): # se da el parametro name, que es el valor que queremos modificar en el kit
    current_kit_body=data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body    # retorna el nuevo nombre del kit

def get_new_user_token():
    user_body = data.user_body
    response = sender_stand_request.post_create_new_user(user_body)
    return response.json()["authToken"]   # con esto llamamos la función  create new user, para nos retorne el token que necesitamos para la creación del kit

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token()) # Aqui llamamos a la función para crear el kit
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

def test1_create_kit_1_letter_in_name_success_response():
    current_kit_body = get_kit_body(data.test1_kit_name)
    positive_assert(current_kit_body)

def test2_create_kit_511_letter_in_name_success_response():
    current_kit_body = get_kit_body(data.test2_kit_name)
    positive_assert(current_kit_body)

def test3_create_kit_without_name():
    current_kit_body = get_kit_body(data.test3_kit_name)
    negative_assert_400(current_kit_body)

def test4_create_kit_exceeds_512_letter_in_name():
    current_kit_body = get_kit_body(data.test4_kit_name)
    negative_assert_400(current_kit_body)

def test5_create_kit_with_special_characters_in_name():
    current_kit_body = get_kit_body(data.test5_kit_name)
    positive_assert(current_kit_body)

def test6_create_kit_with_spaces_in_name():
    current_kit_body = get_kit_body(data.test6_kit_name)
    positive_assert(current_kit_body)

def test7_create_kit_with_str_in_name():
    current_kit_body = get_kit_body(data.test7_kit_name)
    positive_assert(current_kit_body)

def test8_create_kit_without_name_parameter():
    current_kit_body = data.kit_body.copy()   #Se hace este copy porque vamos a hacer cambios en el directorio
    current_kit_body.pop("name")
    negative_assert_400(current_kit_body)

def test9_create_kit_with_123_in_name_parameter():
    current_kit_body = get_kit_body(data.test9_kit_name)
    negative_assert_400(current_kit_body)
























