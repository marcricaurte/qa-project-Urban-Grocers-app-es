# Pruebas para el parámetro Name al crear un kit dentro de un/a usuario/a en la aplicación Urban Grocers
## _Pasos para Ejecutar las Pruebas
## Requisitos Previos

1. **Python** instalado en tu sistema.
2. **Framework de pruebas**  `pytest` 
3. **Dependencias** necesarias instaladas (si utilizas dependencias externas, asegúrate de tenerlas en tu entorno de trabajo).

## 1. Crear un Archivo de Prueba

 Crear el archivo de pruebas Python,   `create_kit_name_kit_test.py`, en el cual se van a agregar las pruebas.

### Estructura del archivo de prueba:

Para llamar a las funciones post_create_new_user  y  post_new_client_kit, importar los siguientes archivos:

```python
import sender_stand_requests  
import data

Luego define las funciones para realizar las pruebas así:
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
    current_kit_body = data.kit_body.copy()
    current_kit_body.pop("name")
    negative_assert_400(current_kit_body)

def test9_create_kit_with_123_in_name_parameter():
    current_kit_body = get_kit_body(data.test9_kit_name)
    negative_assert_400(current_kit_body)
