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
            path = FileConverter().convert_from_gif_to_mp4(self.conversion)
            self.assertTrue(path.split(".")[-1] == "mp4")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_m4a_to_mp3(self):
        self.initial_file.file = "test_files/test_m4a.m4a"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_m4a_to_mp3(self.conversion)
            self.assertTrue(path.split(".")[-1] == "mp3")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_jpg_to_pdf(self):
        self.initial_file.file = "test_files/test_jpg.jpg"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_jpg_to_pdf(self.conversion)
            self.assertTrue(path.split(".")[-1] == "pdf")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_jpg_to_png(self):
        self.initial_file.file = "test_files/test_jpg.jpg"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_jpg_to_png(self.conversion)
            self.assertTrue(path.split(".")[-1] == "png")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_heic_to_jpg(self):
        self.initial_file.file = "test_files/test_heic.heic"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_heic_to_jpg(self.conversion)
            self.assertTrue(path.split(".")[-1] == "jpg")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_mkv_to_mp4(self):
        self.initial_file.file = "test_files/test_mkv.mkv"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_mkv_to_mp4(self.conversion)
            self.assertTrue(path.split(".")[-1] == "mp4")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_mov_to_mp4(self):
        self.initial_file.file = "test_files/test_mov.mov"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_mov_to_mp4(self.conversion)
            self.assertTrue(path.split(".")[-1] == "mp4")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_mp3_to_m4a(self):
        self.initial_file.file = "test_files/test_mp3.mp3"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_mp3_to_m4a(self.conversion)
            self.assertTrue(path.split(".")[-1] == "m4a")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_mp3_to_mp4(self):
        self.initial_file.file = "test_files/test_mp3.mp3"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_mp3_to_mp4(self.conversion)
            self.assertTrue(path.split(".")[-1] == "mp4")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_mp3_to_wav(self):
        self.initial_file.file = "test_files/test_mp3.mp3"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_mp3_to_wav(self.conversion)
            self.assertTrue(path.split(".")[-1] == "wav")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_mp4_to_gif(self):
        self.initial_file.file = "test_files/test_mp4.mp4"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_mp4_to_gif(self.conversion)
            self.assertTrue(path.split(".")[-1] == "gif")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_mp4_to_mkv(self):
        self.initial_file.file = "test_files/test_mp4.mp4"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_mp4_to_mkv(self.conversion)
            self.assertTrue(path.split(".")[-1] == "mkv")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_mp4_to_mov(self):
        self.initial_file.file = "test_files/test_mp4.mp4"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_mp4_to_mov(self.conversion)
            self.assertTrue(path.split(".")[-1] == "mov")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_pdf_to_doc(self):
        self.initial_file.file = "test_files/test_pdf.pdf"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_pdf_to_doc(self.conversion)
            self.assertTrue(path.split(".")[-1] == "doc")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_pdf_to_docx(self):
        self.initial_file.file = "test_files/test_pdf.pdf"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_pdf_to_docx(self.conversion)
            self.assertTrue(path.split(".")[-1] == "docx")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_pdf_to_epub(self):
        self.initial_file.file = "test_files/test_pdf.pdf"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_pdf_to_epub(self.conversion)
            self.assertTrue(path.split(".")[-1] == "epub")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_pdf_to_jpg(self):
        self.initial_file.file = "test_files/test_pdf.pdf"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_pdf_to_jpg(self.conversion)
            self.assertTrue(path.split(".")[-1] == "zip")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_pdf_to_png(self):
        self.initial_file.file = "test_files/test_pdf.pdf"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_pdf_to_png(self.conversion)
            self.assertTrue(path.split(".")[-1] == "zip")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_pdf_to_pptx(self):
        self.initial_file.file = "test_files/test_pdf.pdf"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_pdf_to_pptx(self.conversion)
            self.assertTrue(path.split(".")[-1] == "pptx")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_png_to_jpg(self):
        self.initial_file.file = "test_files/test_png.png"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_png_to_jpg(self.conversion)
            self.assertTrue(path.split(".")[-1] == "jpg")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))

    def test_convert_from_png_to_pdf(self):
        self.initial_file.file = "test_files/test_png.png"
        self.initial_file.save(update_fields=["file"])
        if sys.platform == "win32":
            assert True
        else:
            path = FileConverter().convert_from_png_to_pdf(self.conversion)
            self.assertTrue(path.split(".")[-1] == "pdf")
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path)
            os.remove(path)
            self.assertFalse(os.path.exists(path))
