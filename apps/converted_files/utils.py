def get_converted_file_path(initial_file_obj):
    """
    Get the path of the initial file
    """
    return initial_file_obj.file.name.replace("initial_files", "converted_files")
