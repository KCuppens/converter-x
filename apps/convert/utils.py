def get_conversion_path(conversion_obj):
    """
    Get the path of the conversion
    """
    return f"{conversion_obj.id}/conversions/"


def download_file(url, file_name):
    import requests

    r = requests.get(url, stream=True)
    with open(file_name, "wb") as f:
        for chunk in r.iter_content():
            f.write(chunk)
