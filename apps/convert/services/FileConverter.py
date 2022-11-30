import subprocess

import requests

from apps.convert.utils import get_conversion_path
from apps.initial_files.utils import get_unique_file_name


class FileConverter:
    def convert_from_doc_to_pdf(self, conversion):
        initial_file = conversion.initial_file
        # Download file and save
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        path = get_conversion_path(conversion)
        # Convert
        cmd = ["libreoffice", "--convert-to", "pdf", "--outdir", path, file_name]
        p = subprocess.Popen(cmd)
        p.communicate()
        return f"{path}{file_name.replace('.doc', '.pdf')}"

    def convert_from_docx_to_pdf(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        cmd = ["libreoffice", "--convert-to", "pdf", "--outdir", path, file_name]
        p = subprocess.Popen(cmd)
        p.communicate()
        return f"{path}{file_name.replace('.docx', '.pdf')}"

    def convert_from_epub_to_pdf(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert from epub to html
        output_file = convert_from_epub_to_html(file_name, path)
        # Convert from html to pdf
        output_file = convert_from_html_to_pdf(output_file)
        return output_file


def convert_from_epub_to_html(input, output):
    import pypandoc

    pypandoc.convert_file(
        input,
        format="epub",
        to="html5",
        extra_args=["--read=epub", f"--extract-media={output}", "--wrap=none"],
        encoding="utf-8",
        outputfile=output + "/" + input.replace(".epub", ".html"),
        filters=None,
        verify_format=True,
    )
    return output + "/" + input.replace(".epub", ".html")


def convert_from_html_to_pdf(input):
    from weasyprint import HTML

    HTML(input).write_pdf(input.replace(".html", ".pdf"))
    return input.replace(".html", ".pdf")
