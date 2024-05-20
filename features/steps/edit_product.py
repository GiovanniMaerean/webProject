from behave import *
from django.urls import reverse

from steamApp.models import Product

use_step_matcher("parse")


@given("Exists product registered by {user}")
def step_impl(context, user):
    from django.contrib.auth.models import User
    from steamApp.models import Product
    user = User.objects.get(username=user)
    for row in context.table:
        product_data = {key: (value if value != 'None' else None) for key, value in row.items()}
        product_data['creatorUser'] = user
        Product.objects.create(**product_data)


@when("I edit {product} product")
def step_impl(context, product):
    from steamApp.models import Product
    product = Product.objects.get(name=product)
    id = product.id
    url = reverse('modifyProduct', args=[id])
    context.browser.visit(context.get_url(url))
    if context.browser.url == context.get_url(url):
        for row in context.table:

            form = context.browser.find_by_name('product_form').first
            for column, value in row.items():
                form.find_by_name(column).first.fill(value)

            context.browser.find_by_css('.button[type="submit"]').first.click()


@then('The price of {product} is {value}')
def step_impl(context, product, value):
    product = Product.objects.get(name=product)
    actual_price = product.price

    assert actual_price == value
