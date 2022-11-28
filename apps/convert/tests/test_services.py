from django.core.files.uploadedfile import SimpleUploadedFile

from apps.action.tests.factories import ActionFactory
from apps.base.utils import CustomGraphQLTestCase
from apps.conversions.tests.factories import ConversionFactory
from apps.convert.services.ConvertEngine import ConvertEngine, calculate_step_percentage


class ConvertTestCase(CustomGraphQLTestCase):
    def test_check_conversion_exists(self):
        self.assertTrue(ConvertEngine().check_conversion_exists("mkv", "mp4"))

    def test_check_conversion_does_not_exist(self):
        self.assertFalse(ConvertEngine().check_conversion_exists("mkv", "mp3"))

    def test_check_correct_file_type(self):
        self.assertTrue(ConvertEngine().check_correct_file_type("mkv", "video/x-matroska"))

    def test_check_correct_file_type_does_not_exist(self):
        self.assertFalse(ConvertEngine().check_correct_file_type("mkv", "video/mp4"))

    def test_check_file_type_supported(self):
        self.assertTrue(
            ConvertEngine().check_file_type_supported(
                SimpleUploadedFile("assignment.pdf", b"content")
            )
        )

    def test_check_file_type_supported_not(self):
        self.assertFalse(
            ConvertEngine().check_file_type_supported(
                SimpleUploadedFile("assignment.txt", b"content")
            )
        )

    def test_check_mime_type_supported(self):
        self.assertTrue(ConvertEngine().check_mime_type_supported("application/pdf"))

    def test_check_mime_type_supported_not(self):
        self.assertFalse(ConvertEngine().check_mime_type_supported("application/pd"))

    def test_calculate_step_percentage(self):
        action = ActionFactory()
        conversion = ConversionFactory()
        action.conversions.add(conversion)
        self.assertEqual(calculate_step_percentage(action.conversions.all()), 25)
