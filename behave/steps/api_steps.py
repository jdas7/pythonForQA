import requests
from behave import Given, When, Then


@Given('que tengo un endpoint "{url}"')
def end_point(context, url):
    context.api_url = url


@Given('cuento con los siguientes query params "{param}" y su valor "{value}"')
def get_params(context, param, value):
    context.query_params = {param: value}


@When('hago la peticion')
def request(context):
    context.response = requests.get(context.api_url, params=context.query_params)


@Then('visualizo el statuscode')
def status(context):
    status_code = context.response.status_code
    assert status_code == 200, f'statuscode: {status_code}'


@Then('me responde el contenido con el nombre "{name}"')
def step_impl(context, name):
    contents = context.response.json()['results']
    content_names = [content['name'] for content in contents]
    assert name in content_names, f'te llamas {name}'
