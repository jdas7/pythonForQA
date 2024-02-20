from donbot.requests_utils import RequestsUtils
from behave import given, when, then

response = None


@given('who made a GET request to "https://pokeapi.co/api/v2/"')
def step_impl(context):
    url = "https://pokeapi.co/api/v2/"
    global response
    response = RequestsUtils.send_get_request(url)


@then('the response must have status code 200')
def step_impl(context):
    assert response is not None, "No se ha realizado la solicitud GET"
    assert response.status_code == 200, f"La solicitud GET tuvo un código de estado inesperado: {response.status_code}"
    print("Petición GET exitosa:")
    print(response.text)
