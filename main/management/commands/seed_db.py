from django.core.management import BaseCommand
import faker, faker_commerce, random

from main.models import Product, Order, OrderItem
fk = faker.Faker()
fk.add_provider(faker_commerce.Provider)
class Command(BaseCommand):
    help = "Populate database with dummy data"
    def handle(self, *args, **options):
        self.set_orders()
    
    def set_products(self):
        for i in range(10):
            product = Product.objects.create(
                name=fk.ecommerce_name(),
                price=random.randint(10, 1000),
                description=fk.paragraph()
            )
            product.save()
            self.stdout.write(f'Product {product.name} created')
    
    def set_orders(self):
        for i in range(10):
            order = Order.objects.create(
                customer_name=fk.name()
            )
            order.save()
            for x in range(random.randint(3, 10)):
                products = Product.objects.order_by('?')
                order_item = OrderItem.objects.create(
                    product=products[x],
                    order=order,
                    quantity=random.randint(1, 10)
                )
                order_item.save()
            self.stdout.write(f'Order {order.order_id} created with {order.items.count()}')

            