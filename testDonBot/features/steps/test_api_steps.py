from donbot.requests_utils import RequestsUtils
from behave import given, then


@given('who made a GET request to "https://pokeapi.co/api/v2/"')
def step_impl(context):
    url = "https://pokeapi.co/api/v2/"
    context.response = RequestsUtils.send_get_request(url)


@then('the response must have status code 200')
def step_impl(context):
    assert context.response is not None, "No se ha realizado la solicitud GET"
    assert context.response.status_code == 200, f"La solicitud GET tuvo un código de estado inesperado: {context.response.status_code}"
    print("Petición GET exitosa:")
    print(context.response.text)
