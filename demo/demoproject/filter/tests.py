from django.test import TestCase
from django.core.urlresolvers import reverse


class FilteredListView(TestCase):
    fixtures = ['initial_data.json']

    def test_empty_get(self):
        url = reverse('user_filter_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_order_by_get(self):
        url = reverse('user_filter_view') + '?order_by=last_login'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_query(self):
        url = reverse('user_filter_view') + '?query=doe'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['users']), 1)
