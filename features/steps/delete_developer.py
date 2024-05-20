from behave import *
from django.urls import reverse

from steamApp.models import Developer

use_step_matcher("parse")

@given("Exists a developer registered by {user}")
def step_impl(context, user):
    from django.contrib.auth.models import User
    user = User.objects.get(username=user)
    for row in context.table:
        developer_data = {key: (value if value != 'None' else None) for key, value in row.items()}
        developer_data['creatorUser'] = user


        Developer.objects.create(**developer_data)


@when("I delete {developer_name} developer")
def step_impl(context, developer_name):
    developer = Developer.objects.get(name=developer_name)
    id = developer.id
    url = reverse('developerDetails', args=[id])
    context.browser.visit(context.get_url(url))
    if context.browser.url == context.get_url(url):
        context.browser.find_by_css('.button[name="delete_button"]').first.click()