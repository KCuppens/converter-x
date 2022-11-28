from datetime import datetime

from apps.base.utils import send_progress_websocket
from apps.conversions.constants import CONVERT_OPTIONS, SHORTCUT_OPTIONS, SHORTCUT_OPTIONS_REVERSED
from apps.convert.errors import ConversionNotExistingError
from apps.initial_files.constants import STATUS_CLOSED


now = datetime.now()


class ConvertEngine:
    def convert(self, action_obj):
        # Initial status in websocket
        send_progress_websocket(action_obj, 0, "Initializing compression")
        # Loop through conversions
        conversions = action_obj.conversions.all()
        step = calculate_step_percentage(conversions)
        count = 0
        for conversion in conversions:
            init_file = conversion.initial_file
            # Initiate conversion
            from_action = conversion.from_action
            to_action = conversion.to_action
            try:
                conversion_file = eval(f"convert_from_{from_action}_to_{to_action}").delay()
            except ConversionNotExistingError:
                send_progress_websocket(
                    action_obj,
                    100,
                    f"Conversion {from_action} to {to_action} does not exist.",
                    {"conversion": conversion.id},
                )
                continue
            # File is compressed, update status to closed
            init_file.status = STATUS_CLOSED
            init_file.save(update_fields=["status"])
            # Mark compression file closed
            conversion_file.status = STATUS_CLOSED
            conversion_file.save(update_fields=["status"])
            # Websocket status to file completed
            send_progress_websocket(
                action_obj, count + step, "File converted", {"file": init_file.id}
            ),
            count += step
        # Update status
        send_progress_websocket(action_obj, 100, "Conversion completed.")
        return "Succesfully completed the conversion."

    def check_conversion_exists(self, from_action, to_action):
        # Check if this conversion is possible at this time
        if f"{from_action}_{to_action}" in CONVERT_OPTIONS:
            return True
        return False

    def check_correct_file_type(self, from_action, mimetype):
        # Check if directly the same
        if from_action == mimetype:
            return True
        # Check if from_action corresponds to mimetype
        elif from_action in SHORTCUT_OPTIONS and SHORTCUT_OPTIONS[from_action] == mimetype:
            return True
        return False

    def check_file_type_supported(self, file):
        # Check if we support this file type in our conversions
        file_name = file.name.split("/")[-1]
        extension = file_name.split(".")[1]
        if extension in SHORTCUT_OPTIONS:
            return True
        return False

    def check_mime_type_supported(self, mime_type):
        if mime_type in SHORTCUT_OPTIONS_REVERSED:
            return True
        return False


def calculate_step_percentage(compressions):
    return 100 / len(compressions) / 4
