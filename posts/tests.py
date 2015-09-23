from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.


class HomeViewTest(TestCase):

    def test_home_view(self):
        """TODO: Docstring for test_home_view.
        :returns: TODO

        """
        res = self.client(reverse('home'))
        self.assertEqual(res.status_code, 200)
