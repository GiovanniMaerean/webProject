from behave import *
from django.urls import reverse

from steamApp.models import Developer

use_step_matcher("parse")


@given("Exists developer registered by {user} with id {id}")
def step_impl(context, user, id):
    from django.contrib.auth.models import User
    user = User.objects.get(username=user)
    for row in context.table:
        developer_data = {key: (value if value != 'None' else None) for key, value in row.items()}
        developer_data['creatorUser'] = user
        developer_data['id'] = id
        Developer.objects.create(**developer_data)


@when("I edit {developer} developer")
def step_impl(context, developer):
    developer = Developer.objects.get(name=developer)
    id = developer.id
    url = reverse('modifyDeveloper', args=[id])
    context.browser.visit(context.get_url(url))
    if context.browser.url == context.get_url(url):
        for row in context.table:

            for heading in row.headings:
                context.browser.fill(heading, row[heading])

            context.browser.find_by_css('.button[type="submit"]').first.click()


@then('The name of {id} developer is {value}')
def step_impl(context, id, value):
    developer = Developer.objects.get(id=id)
    actual_name = developer.name

    assert actual_name == value
