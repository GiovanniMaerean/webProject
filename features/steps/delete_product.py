from behave import *
from django.urls import reverse

from steamApp.models import Product

use_step_matcher("parse")

@when("I delete {product_name} product")
def step_impl(context, product_name):
    product_name = Product.objects.get(name=product_name)
    id = product_name.id
    url = reverse('productDetails', args=[id])
    context.browser.visit(context.get_url(url))
    if context.browser.url == context.get_url(url):
        context.browser.find_by_css('.button[name="delete_button"]').first.click()