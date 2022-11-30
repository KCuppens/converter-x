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

    def convert_from_m4a_to_mp3(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        from pydub import AudioSegment

        sound = AudioSegment.from_file(file_name)
        sound.export(f"{path}{file_name.replace('.m4a', '.mp3')}")
        return f"{path}{file_name.replace('.m4a', '.mp3')}"

    def convert_from_jpg_to_pdf(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        from PIL import Image

        image = Image.open(file_name)
        image_convert = image.convert("RGB")
        image_convert.save(f"{path}{file_name.replace('.jpg', '.pdf')}")
        return f"{path}{file_name.replace('.jpg', '.pdf')}"

    def convert_from_jpg_to_png(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        from PIL import Image

        image = Image.open(file_name)
        image = image.convert("RGB")
        image.save(f"{path}{file_name.replace('.jpg', '.png')}")
        return f"{path}{file_name.replace('.jpg', '.png')}"

    def convert_from_heic_to_jpg(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        import pyheif
        from PIL import Image

        heif_file = pyheif.read_heif(file_name)
        data = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        data.save(f"{path}{file_name.replace('.heic', '.jpg')}")
        return f"{path}{file_name.replace('.heic', '.jpg')}"

    def convert_from_mkv_to_mp4(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        cmd = [
            "ffmpeg",
            "-i",
            file_name,
            "-codec",
            "copy",
            f"{path}{file_name.replace('.mkv', '.mp4')}",
        ]
        p = subprocess.Popen(cmd)
        p.communicate()
        return f"{path}{file_name.replace('.mkv', '.mp4')}"

    def convert_from_mov_to_mp4(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        cmd = ["ffmpeg", "-i", file_name, f"{path}{file_name.replace('.mov', '.mp4')}"]
        p = subprocess.Popen(cmd)
        p.communicate()
        return f"{path}{file_name.replace('.mov', '.mp4')}"
