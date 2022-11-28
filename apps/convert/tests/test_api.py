# import pytest
# from django.core.files.uploadedfile import SimpleUploadedFile
# from graphene_django.utils.testing import GraphQLTestCase

# from apps.action.models import Action
# from apps.convert.models import Convert
# from apps.initial_file.models import InitialFile


# class ConvertTestCase(GraphQLTestCase):
#     @pytest.mark.django_db(transaction=True, reset_sequences=True)
#     def create_convert_obj(self):
#         action = Action.objects.create()
#         initial_file = InitialFile.objects.create(
#             file=SimpleUploadedFile("assignment.txt", b"content"),
#             s3_url="test",
#             mimetype="test",
#         )
#         convert = Convert.objects.create(initial_file=initial_file)
#         action.converts.add(convert)
#         return convert

#     def setUp(self):
#         self.convert = self.create_convert_obj()

#     def test_to_action_conversion_does_exist(self):
#         self.convert.from_action = "mkv"
#         self.convert.save(update_fields=["from_action"])
#         response = self.query(
#             """
#             mutation setConvertToTypeAction(
#                 $convertId: String!, $toAction: String!
#                 ) {
#                 setConvertToTypeAction(
#                     convertId: $convertId, toAction: $toAction
#                     ) {
#                     message,
#                     convert {
#                         toAction
#                     }
#                 }
#             }
#             """,
#             variables={"convertId": str(self.convert.id), "toAction": "mp4"},
#         )
#         assert (
#             response.json()["data"]["setConvertToTypeAction"]["message"]
#             == "To action has been set successfully."
#         )
#         assert (
#             response.json()["data"]["setConvertToTypeAction"]["convert"][
#                 "toAction"
#             ]
#             == "mp4"
#         )

#     def test_to_action_conversion_does_not_exist(self):
#         self.convert.from_action = "mkv"
#         self.convert.save(update_fields=["from_action"])
#         print(self.convert.id)
#         response = self.query(
#             """
#             mutation setConvertToTypeAction(
#                 $convertId: String!, $toAction: String!
#             ) {
#                 setConvertToTypeAction(
#                     convertId: $convertId, toAction: $toAction
#                     ) {
#                     message,
#                     convert {
#                         toAction
#                     }
#                 }
#             }
#             """,
#             variables={"convertId": str(self.convert.id), "toAction": "HFE"},
#         )
#         print(response.json())
#         assert (
#             response.json()["data"]["setConvertToTypeAction"]["message"]
#             == "This conversion does not exist yet in our system."
#         )
#         assert (
#             response.json()["data"]["setConvertToTypeAction"]["convert"][
#                 "toAction"
#             ]
#             == ""
#         )

#     def test_remove_convert(self):
#         response = self.query(
#             """
#             mutation removeConvert($convert: String!) {
#                 removeConvert(convert: $convert) {
#                     message
#                 }
#             }
#             """,
#             variables={"convert": str(self.convert.id)},
#         )
#         print(response.json())
#         assert (
#             response.json()["data"]["removeConvert"]["message"]
#             == "Convert is removed."
#         )


# class ConvertFilesTestCase(GraphQLTestCase):
#     def test_convert_action_missing_to_action(self):
#         # Create an action
#         response = self.query(
#             """
#             mutation createOrGetAction{
#                 createOrGetAction{
#                     action {
#                     id
#                     }
#                 }
#             }
#             """,
#         )
#         action_id = response.json()["data"]["createOrGetAction"]["action"][
#             "id"
#         ]
#         assert action_id
#         # Create initial files
#         action = Action.objects.filter(id=action_id).first()
#         initial_file = InitialFile.objects.create(
#             file=SimpleUploadedFile("assignment.pdf", b"content"),
#             s3_url="test",
#             mimetype="pdf",
#         )
#         convert = Convert.objects.create(
#             initial_file=initial_file, from_action="pdf"
#         )
#         action.converts.add(convert)
#         # Convert action
#         response = self.query(
#             """
#             mutation convertAction {
#                 convertAction {
#                     successes,
#                     errors,
#                     action{
#                         id
#                     }
#                 }
#             }
#             """,
#             variables={"convert": str(convert.id)},
#         )
#         assert response.json()["data"]["convertAction"]["successes"] == []
#         assert response.json()["data"]["convertAction"]["errors"] == [
#             "Please make sure your desired file type is set."
#         ]

#     def test_convert_action(self):
#         # Create an action
#         response = self.query(
#             """
#             mutation createOrGetAction{
#                 createOrGetAction{
#                     action {
#                     id
#                     }
#                 }
#             }
#             """,
#         )
#         action_id = response.json()["data"]["createOrGetAction"]["action"][
#             "id"
#         ]
#         assert action_id
#         # Create initial files
#         action = Action.objects.filter(id=action_id).first()
#         initial_file = InitialFile.objects.create(
#             file=SimpleUploadedFile("assignment.pdf", b"content"),
#             s3_url="test",
#             mimetype="pdf",
#         )
#         convert = Convert.objects.create(
#             initial_file=initial_file, from_action="pdf", to_action="jpg"
#         )
#         action.converts.add(convert)
#         # Convert action
#         response = self.query(
#             """
#             mutation convertAction {
#                 convertAction {
#                     successes,
#                     errors,
#                     action{
#                         converts{
#                             conversionFiles{
#                                 file
#                             }
#                         }
#                     }
#                 }
#             }
#             """,
#             variables={"convert": str(convert.id)},
#         )
#         print(response.json())
#         assert (
#             "We are converting"
#             in response.json()["data"]["convertAction"]["successes"][0]
#         )
#         assert response.json()["data"]["convertAction"]["errors"] == []
