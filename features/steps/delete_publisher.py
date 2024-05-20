from behave import *
from django.urls import reverse

from steamApp.models import Publisher

use_step_matcher("parse")

@given("Exists a publisher registered by {user}")
def step_impl(context, user):
    from django.contrib.auth.models import User
    user = User.objects.get(username=user)
    for row in context.table:
        publisher_data = {key: (value if value != 'None' else None) for key, value in row.items()}
        publisher_data['creatorUser'] = user


        Publisher.objects.create(**publisher_data)


@when("I delete {publisher_name} publisher")
def step_impl(context, publisher_name):
    publisher = Publisher.objects.get(name=publisher_name)
    id = publisher.id
    url = reverse('publisherDetails', args=[id])
    context.browser.visit(context.get_url(url))
    if context.browser.url == context.get_url(url):
        context.browser.find_by_css('.button[name="delete_button"]').first.click()