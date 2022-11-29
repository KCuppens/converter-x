import subprocess

import requests

from apps.converted_files.utils import get_converted_file_path
from apps.initial_files.utils import get_unique_file_name


class FileConverter:
    def convert_from_doc_to_pdf(self, conversion):
        initial_file = conversion.initial_file
        # Download file and save
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_converted_file_path(conversion.initial_file).replace("doc", "pdf")
        # Convert
        cmd = "libreoffice --convert-to pdf".split() + [file_name] + "--outdir".split() + [path]
        subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        return path

    def convert_from_docx_to_pdf(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_converted_file_path(conversion.initial_file).replace("docx", "pdf")
        # Convert
        cmd = "libreoffice --convert-to pdf".split() + [file_name] + "--outdir".split() + [path]
        subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        return path
