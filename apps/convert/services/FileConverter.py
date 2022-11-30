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
        # Convert
        cmd = ["ebook-convert", file_name, f"{path}{file_name.replace('.epub', '.pdf')}"]
        p = subprocess.Popen(cmd)
        p.communicate()
        return f"{path}{file_name.replace('.epub', '.pdf')}"

    def convert_from_gif_to_mp4(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        from moviepy.editor import VideoFileClip

        video_clip = VideoFileClip(file_name)
        video_clip.write_videofile(f"{path}{file_name.replace('.gif', '.mp4')}")
        return f"{path}{file_name.replace('.gif', '.mp4')}"
