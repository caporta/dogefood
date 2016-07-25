from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Product


class ProductModelTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            sku='foo-bar-baz-quux-blu',
            name='Blue Label',
            slug='blue_label',
            description='blue label formula description',
            price='40.00',
            weight='30.00',
        )


    def test_product_creation(self):
        now = timezone.now()
        self.assertLess(self.product.created_at, now)

class ProductViewsTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            sku='foo-bar-baz-quux-grn',
            name='Green Label',
            slug='green_label',
            description='green label formula description',
            price='40.00',
            weight='30.00',
        )
        self.product2 = Product.objects.create(
            sku='foo-bar-baz-quux-yel',
            name='Yellow Label',
            slug='yellow_label',
            description='yellow label formula description',
            price='50.00',
            weight='30.00',
        )

    def test_product_list_view(self):
        resp = self.client.get(reverse('products:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.product, resp.context['products'])
        self.assertIn(self.product2, resp.context['products'])
        self.assertTemplateUsed(resp, 'base/product_list.html')
        self.assertContains(resp, self.product.name)

    def test_product_detail_view(self):
        resp = self.client.get(reverse('products:detail',
                                    kwargs={'pk': self.product.pk})
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.product, resp.context['product'])
        self.assertTemplateUsed(resp, 'base/product_detail.html')
        self.assertContains(resp, self.product.name)
