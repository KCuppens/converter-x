from django.core.files.uploadedfile import SimpleUploadedFile

from apps.action.tests.factories import ActionFactory
from apps.base.utils import CustomGraphQLTestCase
from apps.conversions.models import Conversion
from apps.conversions.tests.factories import ConversionFactory
from apps.initial_files.tests.factories import InitialFileFactory


class ConversionTestCase(CustomGraphQLTestCase):
    def setUp(self):
        self.test_file = SimpleUploadedFile("assignment.jpg", b"content")
        self.action = ActionFactory()
        self.initial_file = InitialFileFactory(file=self.test_file)
        self.conversion = ConversionFactory(initial_file=self.initial_file, from_action="jpg")

    def test_set_conversion_to_action(self):
        response = self.query(
            """
            mutation setConversionToAction($conversion_id: String!, $to_action: String!) {
                setConversionToAction(conversionId: $conversion_id, toAction: $to_action) {
                    message,
                    conversion {
                        toAction
                    }
                }
            }
            """,
            variables={"conversion_id": str(self.conversion.id), "to_action": "pdf"},
        )
        self.assertResponseNoErrors(response)
        self.assertEqual(
            response.json()["data"]["setConversionToAction"]["conversion"]["toAction"], "pdf"
        )

    def test_set_conversion_to_action_no_from_action(self):
        self.conversion.from_action = ""
        self.conversion.save(update_fields=["from_action"])
        response = self.query(
            """
            mutation setConversionToAction($conversion_id: String!, $to_action: String!) {
                setConversionToAction(conversionId: $conversion_id, toAction: $to_action) {
                    message,
                    conversion {
                        toAction
                    }
                }
            }
            """,
            variables={"conversion_id": str(self.conversion.id), "to_action": "pdf"},
        )
        self.assertResponseNoErrors(response)
        self.assertEqual(
            response.json()["data"]["setConversionToAction"]["message"],
            "Please set a from action first in your conversion.",
        )

    def test_set_conversion_to_action_conversion_not_exist(self):
        response = self.query(
            """
            mutation setConversionToAction($conversion_id: String!, $to_action: String!) {
                setConversionToAction(conversionId: $conversion_id, toAction: $to_action) {
                    message,
                    conversion {
                        toAction
                    }
                }
            }
            """,
            variables={"conversion_id": str(self.conversion.id), "to_action": "mdf"},
        )
        self.assertResponseNoErrors(response)
        self.assertEqual(
            response.json()["data"]["setConversionToAction"]["message"],
            "This conversion does not exist yet in our system.",
        )

    def test_remove_conversion(self):
        response = self.query(
            """
            mutation removeConversion($conversion_id: String!) {
                removeConversion(conversionId: $conversion_id) {
                    message
                }
            }
            """,
            variables={"conversion_id": str(self.conversion.id)},
        )
        with self.assertRaises(Conversion.DoesNotExist):
            Conversion.objects.get(id=self.conversion.id)
        self.assertEqual(
            response.json()["data"]["removeConversion"]["message"], "Conversion is removed."
        )
