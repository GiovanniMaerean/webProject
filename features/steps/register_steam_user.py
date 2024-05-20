from behave import *
from selenium.webdriver.common.keys import Keys

use_step_matcher("parse")


@when("I register a steam user data")
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('createSteamUser'))

        if context.browser.url == context.get_url('createSteamUser'):
            for heading in row.headings:
                context.browser.fill(heading, row[heading])

            context.browser.find_by_css('.button[type="submit"]').first.click()



@then('There are {count:n} steam user')
def step_impl(context, count):
    from steamApp.models import SteamUser
    assert count == SteamUser.objects.count()