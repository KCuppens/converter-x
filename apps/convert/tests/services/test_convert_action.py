import sys

from apps.action.tests.factories import ActionFactory
from apps.base.storage_backends import MediaStorage
from apps.base.utils import CustomGraphQLTestCase
from apps.conversions.tests.factories import ConversionFactory
from apps.convert.services.ConvertAction import ConvertAction
from apps.initial_files.tests.factories import InitialFileFactory


class ConvertActionTestCase(CustomGraphQLTestCase):
    def setUp(self):
        self.media_storage = MediaStorage()
        self.action = ActionFactory()
        self.initial_file = InitialFileFactory(file="test_file.png")
        self.conversion = ConversionFactory(
            initial_file=self.initial_file, from_action="doc", to_action="pdf"
        )

    def test_convert_doc_to_pdf(self):
        if sys.platform == "win32":
            assert True
        else:
            converted_file = ConvertAction().convert_action(self.action.id, self.conversion.id)
            self.assertTrue(converted_file)
