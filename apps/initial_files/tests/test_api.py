from django.core.files.uploadedfile import SimpleUploadedFile

from graphene_file_upload.django.testing import GraphQLFileUploadTestCase

from apps.action.models import Action
from apps.base.storage_backends import MediaStorage


class InitialFileTestCase(GraphQLFileUploadTestCase):
    def test_upload_file_to_initial_files(self):
        test_file = SimpleUploadedFile("assignment.jpg", b"content")
        response = self.file_query(
            """
            mutation uploadToInitialFiles($file: Upload!, $from_action: String!) {
                uploadToInitialFiles(file: $file, fromAction: $from_action) {
                    message,
                    action {
                        id
                    }
                }
            }
            """,
            op_name="uploadToInitialFiles",
            files={"file": test_file},
            variables={"from_action": "jpg"},
        )
        print(response.json())
        self.assertResponseNoErrors(response)
        self.assertTrue(response.json()["data"]["uploadToInitialFiles"]["action"]["id"])
        action_obj = Action.objects.get(
            id=response.json()["data"]["uploadToInitialFiles"]["action"]["id"]
        )
        conversion_obj = action_obj.conversions.first()
        media_storage = MediaStorage()
        media_storage.delete(conversion_obj.initial_file.file.name)
        self.assertFalse(media_storage.exists(conversion_obj.initial_file.file.name))

    def test_upload_file_to_initial_files_unsupported(self):
        test_file = SimpleUploadedFile("assignment.txt", b"content")
        response = self.file_query(
            """
            mutation uploadToInitialFiles($file: Upload!, $from_action: String!) {
                uploadToInitialFiles(file: $file, fromAction: $from_action) {
                    message,
                    action {
                        id
                    }
                }
            }
            """,
            op_name="uploadToInitialFiles",
            files={"file": test_file},
            variables={"from_action": "txt"},
        )
        print(response.json())
        self.assertEqual(
            response.json()["data"]["uploadToInitialFiles"]["message"],
            "This file type is not yet suppported for conversion. We will hurry to add.",
        )

    def test_upload_file_to_initial_files_uncorrect(self):
        test_file = SimpleUploadedFile("assignment.jpg", b"content")
        response = self.file_query(
            """
            mutation uploadToInitialFiles($file: Upload!, $from_action: String!) {
                uploadToInitialFiles(file: $file, fromAction: $from_action) {
                    message,
                    action {
                        id
                    }
                }
            }
            """,
            op_name="uploadToInitialFiles",
            files={"file": test_file},
            variables={"from_action": "txt"},
        )
        print(response.json())
        self.assertEqual(
            response.json()["data"]["uploadToInitialFiles"]["message"],
            "This is not the correct file type. Please upload a txt file.",
        )
