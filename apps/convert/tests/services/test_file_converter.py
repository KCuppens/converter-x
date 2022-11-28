import os
import sys

from apps.action.tests.factories import ActionFactory
from apps.base.storage_backends import MediaStorage
from apps.base.utils import CustomGraphQLTestCase
from apps.conversions.tests.factories import ConversionFactory
from apps.convert.services.FileConverter import FileConverter
from apps.initial_files.tests.factories import InitialFileFactory


class FileConverterTestCase(CustomGraphQLTestCase):
    def setUp(self):
        self.media_storage = MediaStorage()
        self.action = ActionFactory()
        self.initial_file = InitialFileFactory(file="test_file.png")
        self.conversion = ConversionFactory(initial_file=self.initial_file)

    def test_convert_from_doc_to_pdf(self):
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_doc_to_pdf(self.conversion)
            self.assertTrue(path)
            self.assertTrue(self.media_storage.exists(path))
            self.initial_file.delete()
            if os.path.exists(path):
                os.remove(path)
            self.assertFalse(self.media_storage.exists(path))
