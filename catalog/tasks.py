from celery import shared_task
from django.core.cache import cache


@shared_task
def notify_new_product(product_name):
    print(f'new product {product_name} came!!')
    return "Done"
