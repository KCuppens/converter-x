import requests

from apps.initial_files.utils import get_unique_file_name


def get_conversion_path(conversion_obj):
    """
    Get the path of the conversion
    """
    return f"{conversion_obj.id}/conversions/"


def download_file(url, file_name):
    from urllib.request import Request, urlopen

    print(url)
    req = Request(url=url, headers={"User-Agent": "XYZ/3.0"})
    with urlopen(req, timeout=10) as url:
        s = url.read()

    with open(file_name, "wb") as f:
        f.write(s)

    return file_name


def get_initial_file_for_conversion(conversion):
    initial_file = conversion.initial_file
    # Download file and save
    r = requests.get(initial_file.file.url)
    file_name = get_unique_file_name(initial_file.file)
    open(file_name, "wb").write(r.content)
    path = get_conversion_path(conversion)
    return file_name, path
