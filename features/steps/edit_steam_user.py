from behave import *
from django.urls import reverse

from steamApp.models import SteamUser

use_step_matcher("parse")


@given("Exists steam user registered by {user}")
def step_impl(context, user):
    from django.contrib.auth.models import User
    user = User.objects.get(username=user)
    for row in context.table:
        steam_user_data = {key: (value if value != 'None' else None) for key, value in row.items()}
        steam_user_data['creatorUser'] = user
        SteamUser.objects.create(**steam_user_data)


@when("I edit {steamID} steam user")
def step_impl(context, steamID):
    steam_user = SteamUser.objects.get(steamID=steamID)
    id = steam_user.id
    url = reverse('modifySteamUser', args=[id])
    context.browser.visit(context.get_url(url))
    if context.browser.url == context.get_url(url):
        for row in context.table:

            for heading in row.headings:
                context.browser.fill(heading, row[heading])

            context.browser.find_by_css('.button[type="submit"]').first.click()


@then('The name of {steamID} steam user is {value}')
def step_impl(context, steamID, value):
    steam_user = SteamUser.objects.get(steamID=steamID)
    actual_name = steam_user.realName

    assert actual_name == value
