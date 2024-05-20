from behave import *
from django.urls import reverse

from steamApp.models import SteamUser

use_step_matcher("parse")

@when("I delete {steamID} steam user")
def step_impl(context, steamID):
    steam_user = SteamUser.objects.get(steamID=steamID)
    id = steam_user.id
    url = reverse('steamUserDetails', args=[id])
    context.browser.visit(context.get_url(url))
    if context.browser.url == context.get_url(url):
        context.browser.find_by_css('.button[name="delete_button"]').first.click()