def get_conversion_path(conversion_obj):
    """
    Get the path of the conversion
    """
    return f"{conversion_obj.id}/conversions/"


def download_file(url, file_name):
    import urllib.request

    urllib.request.urlretrieve(url, file_name)
