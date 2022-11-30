import os
import sys

from apps.action.tests.factories import ActionFactory
from apps.base.storage_backends import MediaStorage
from apps.base.utils import CustomGraphQLTestCase
from apps.conversions.tests.factories import ConversionFactory
from apps.convert.services.FileConverter import FileConverter
from apps.convert.utils import get_conversion_path
from apps.initial_files.tests.factories import InitialFileFactory


class FileConverterTestCase(CustomGraphQLTestCase):
    def setUp(self):
        self.media_storage = MediaStorage()
        self.action = ActionFactory()
        self.initial_file = InitialFileFactory()
        self.conversion = ConversionFactory(initial_file=self.initial_file)
        if not os.path.exists(get_conversion_path(self.conversion)):
            os.makedirs(get_conversion_path(self.conversion))

    def test_convert_from_doc_to_pdf(self):
        self.initial_file.file = "test_files/test_doc.doc"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_doc_to_pdf(self.conversion)
            self.assertTrue(path.split(".")[-1] == "pdf")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_docx_to_pdf(self):
        self.initial_file.file = "test_files/test_docx.docx"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_docx_to_pdf(self.conversion)
            self.assertTrue(path.split(".")[-1] == "pdf")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_epub_to_pdf(self):
        self.initial_file.file = "test_files/test_epub.epub"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_epub_to_pdf(self.conversion)
            self.assertTrue(path.split(".")[-1] == "pdf")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_gif_to_mp4(self):
        self.initial_file.file = "test_files/test_gif.gif"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_epub_to_pdf(self.conversion)
            self.assertTrue(path.split(".")[-1] == "gif")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))
