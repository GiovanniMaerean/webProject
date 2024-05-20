from behave import *
from django.urls import reverse

from steamApp.models import Publisher

use_step_matcher("parse")


@given("Exists publisher registered by {user} with id {id}")
def step_impl(context, user, id):
    from django.contrib.auth.models import User
    user = User.objects.get(username=user)
    for row in context.table:
        publisher_data = {key: (value if value != 'None' else None) for key, value in row.items()}
        publisher_data['creatorUser'] = user
        publisher_data['id'] = id
        Publisher.objects.create(**publisher_data)


@when("I edit {publisher} publisher")
def step_impl(context, publisher):
    publisher = Publisher.objects.get(name=publisher)
    id = publisher.id
    url = reverse('modifyPublisher', args=[id])
    context.browser.visit(context.get_url(url))
    if context.browser.url == context.get_url(url):
        for row in context.table:

            for heading in row.headings:
                context.browser.fill(heading, row[heading])

            context.browser.find_by_css('.button[type="submit"]').first.click()


@then('The name of {id} publisher is {value}')
def step_impl(context, id, value):
    publisher = Publisher.objects.get(id=id)
    actual_name = publisher.name

    assert actual_name == value