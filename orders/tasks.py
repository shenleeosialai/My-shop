from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from shop.recommender import Recommender


@shared_task
def order_created(order_id):
    """Task to send an e-mail notification when an order is successfully
    created."""
    order = Order.objects.get(id=order_id)
    products = [item.product for item in order.items.all()]
    r = Recommender()
    r.products_bought(products)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
        f'You have successfully placed an order.' \
        f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent
