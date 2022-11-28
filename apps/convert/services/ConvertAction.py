from apps.action.models import Action
from apps.base.utils import send_progress_websocket
from apps.conversions.models import Conversion
from apps.convert.errors import ConversionNotExistingError
from apps.convert.services.FileConverter import FileConverter
from apps.converted_files.models import ConvertedFile
from apps.initial_files.constants import STATUS_CLOSED


class ConvertAction:
    def convert_action(self, action_id, conversion_id):
        # Convert object
        conversion_obj = Conversion.objects.get(id=conversion_id)
        action_obj = Action.objects.get(id=action_id)
        from_action = conversion_obj.from_action
        to_action = conversion_obj.to_action
        send_progress_websocket(
            action_obj,
            25,
            f"Starting file conversion from {from_action} to {to_action}",
            {
                "convert_id": conversion_obj.id,
                "from_action": from_action,
                "to_action": to_action,
            },
        )
        # Check if conversion is possible and initiate
        try:
            file_path = getattr(FileConverter(), f"convert_from_{from_action}_to_{to_action}")(
                conversion_obj
            )
        except ConversionNotExistingError:
            send_progress_websocket(
                action_obj,
                100,
                f"Conversion {from_action} to {to_action} does not exist.",
                {
                    "convert_id": conversion_obj.id,
                    "from_action": from_action,
                    "to_action": to_action,
                },
            )
            return False
        # Create ConversionFile
        send_progress_websocket(
            action_obj,
            50,
            f"Generating downloadable file for {from_action} to {to_action}",
            {
                "convert_id": conversion_obj.id,
                "from_action": from_action,
                "to_action": to_action,
            },
        )
        converted_file = ConvertedFile.objects.create(file=file_path)
        send_progress_websocket(
            action_obj,
            75,
            f"Saving downloadable file for {from_action} to {to_action}",
            {
                "convert_id": conversion_obj.id,
                "from_action": from_action,
                "to_action": to_action,
            },
        )
        conversion_obj.converted_file = converted_file
        send_progress_websocket(
            action_obj,
            90,
            f"Saved file conversion for {from_action} to {to_action}",
            {
                "convert_id": conversion_obj.id,
                "from_action": from_action,
                "to_action": to_action,
            },
        )
        # Mark compression file closed
        converted_file.status = STATUS_CLOSED
        converted_file.save(update_fields=["status"])
        conversion_obj.converted_file = converted_file
        conversion_obj.save(update_fields=["converted_file"])
        # File is compressed, update status to closed
        conversion_obj.initial_file.status = STATUS_CLOSED
        conversion_obj.initial_file.save(update_fields=["status"])
        return converted_file
