import datetime

from apps.base.utils import upload_file_to_media
from apps.conversions.models import Conversion
from apps.initial_files.models import InitialFile


def uploading_initial_file(file, action_obj, from_action):
    """
    Creating the InitialFile
    Assign InitialFile to Action
    """
    # Creating Conversion
    conversion_obj = Conversion.objects.create(from_action=from_action)
    filename = get_unique_file_name(file)
    path = get_initial_file_path(action_obj, conversion_obj, filename)
    # Save in S3 MediaStorage
    upload_file_to_media(path, file)
    # Creating InitialFile
    initial_file = InitialFile.objects.create(file=path)
    conversion_obj.initial_file = initial_file
    conversion_obj.save(update_fields=["initial_file"])
    # Assign Convert to Action
    action_obj.conversions.add(conversion_obj)
    return initial_file


def get_unique_file_name(file):
    file_name = file.name.split("/")[-1]
    extension = file_name.split(".")[1]
    file_name = file_name.split(".")[0]
    date_now = str(datetime.datetime.now().strftime("%m%d%Y%H%M%S"))
    unique_file_name = f"{file_name}-" f"{date_now}" f".{extension}"
    return unique_file_name


def get_initial_file_path(action_obj, conversion_obj, filename):
    """
    Get the path of the initial file
    """
    return f"{action_obj}/{conversion_obj.id}/initial_files/{filename}"
