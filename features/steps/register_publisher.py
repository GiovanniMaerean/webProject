from behave import *

use_step_matcher("parse")


@when('I register a publisher data')
def step_impl(context):

    for row in context.table:
        context.browser.visit(context.get_url('createPublisher'))

        if context.browser.url == context.get_url('createPublisher'):
            for heading in row.headings:
                context.browser.fill(heading, row[heading])

            context.browser.find_by_css('.button[type="submit"]').first.click()


@then('There are {count:n} publisher')
def step_impl(context, count):
    from steamApp.models import Publisher
    assert count == Publisher.objects.count()