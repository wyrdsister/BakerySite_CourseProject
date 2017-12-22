from django.urls import resolve, reverse
from django.test import TestCase
from main.views import home, category
from main.models import Category

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    class CategoryTests(TestCase):
        def setUp(self):
            Category.objects.create(name='test', created='22.12.2017')

    def test_category_view_success_status_code(self):
        url = reverse('category', kwargs={'categoty_id': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_category_view_not_found_status_code(self):
        url = reverse('category', kwargs={'categoty_id': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_category_url_resolves_categoy_detail_view(self):
        view = resolve('/category/1')
        self.assertEquals(view.func, category)

# class DetailCategoryTests(TestCase):
#     def setUp(self):
#         self.category = Category.objects.create(name='test2', created='22.12.2017')
#         url = reverse('home')
#         self.response = self.client.get(url)
#
#     def test_home_view_status_code(self):
#         self.assertEquals(self.response.status_code, 200)
#
#     def test_home_url_resolves_home_view(self):
#         view = resolve('/')
#         self.assertEquals(view.func, home)
#
#     def test_home_view_contains_link_to_category_page(self):
#         category_url = reverse('category', kwargs={'category_id': self.category.id})
#         self.assertContains(self.response, 'href="{0}"'.format(category_url))
#
#     def test_category_view_contains_link_back_to_homepage(self):
#         category_url = reverse('category', kwargs={'category_id': 1})
#         response = self.client.get(category_url)
#         homepage_url = reverse('home')
#         self.assertContains(response, 'href="{0}"'.format(homepage_url))