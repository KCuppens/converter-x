import pytest

from apps.base.utils import CustomGraphQLTestCase
from apps.pages.tests.factories import PageFactory


class PageTestCase(CustomGraphQLTestCase):
    @pytest.mark.django_db(transaction=True, reset_sequences=True)
    def create_page(self):
        return PageFactory()

    def setUp(self):
        self.page = self.create_page()

    def test_get_filter_blogs(self):
        response = self.query(
            """
            query getPage($key_name: String) {
                getPage(keyName: $key_name){
                    keyName,
                    title,
                    content
                }
            }
            """,
            variables={"key_name": self.page.key_name},
        )
        self.assertEqual(response.json()["data"]["getPage"]["keyName"], self.page.key_name)
        self.assertEqual(response.json()["data"]["getPage"]["title"], self.page.title)
        self.assertEqual(response.json()["data"]["getPage"]["content"], self.page.content)
