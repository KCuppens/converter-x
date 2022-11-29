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
        self.initial_file = InitialFileFactory()
        self.conversion = ConversionFactory(initial_file=self.initial_file)

    def test_convert_from_doc_to_pdf(self):
        self.initial_file.file = "test_file.doc"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_doc_to_pdf(self.conversion)
            self.assertTrue(path.split(".")[-1] == "pdf")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            self.initial_file.delete()
            self.assertFalse(os.path.exists(path))

    def test_convert_docx_to_pdf(self):
        self.initial_file.file = "test_file.docx"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_docx_to_pdf(self.conversion)
            self.assertTrue(path.split(".")[-1] == "pdf")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            self.initial_file.delete()
            self.assertFalse(os.path.exists(path))
