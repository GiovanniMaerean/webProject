from behave import *
from selenium.webdriver.common.keys import Keys

use_step_matcher("parse")


@when('I register a product data')
def step_impl(context):

    for row in context.table:
        context.browser.visit(context.get_url('createProducts'))

        if context.browser.url == context.get_url('createProducts'):
            form = context.browser.find_by_name('product_form').first
            for column, value in row.items():
                form.find_by_name(column).first.fill(value)

            context.browser.find_by_css('.button[type="submit"]').first.click()


@when('I select "{text}" from the autocomplete suggestions')
def step_impl(context, text):
    context.browser.find_by_id('id_product_name').type(Keys.ARROW_DOWN)
    context.browser.find_by_id('id_product_name').type(Keys.ENTER)



@then('There are {count:n} products')
def step_impl(context, count):
    from steamApp.models import Product
    assert count == Product.objects.count()

