from datetime import datetime

from apps.conversions.constants import CONVERT_OPTIONS, SHORTCUT_OPTIONS, SHORTCUT_OPTIONS_REVERSED
from apps.convert.tasks import convert_action


now = datetime.now()


class ConvertEngine:
    def convert(self, action_obj, conversion_obj):
        # Initiate conversion
        convert_action.delay(action_obj.id, conversion_obj.id)

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
