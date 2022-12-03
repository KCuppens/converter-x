import subprocess

import requests
from pdf2docx import parse

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

    def convert_from_mp3_to_m4a(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        from pydub import AudioSegment

        sound = AudioSegment.from_file(file_name)
        sound.export(f"{path}{file_name.replace('.mp3', '.m4a')}")
        return f"{path}{file_name.replace('.mp3', '.m4a')}"

    def convert_from_mp3_to_mp4(self, conversion):
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
            "-acodec",
            "copy",
            f"{path}{file_name.replace('.mp3', '.mp4')}",
        ]
        p = subprocess.Popen(cmd)
        p.communicate()
        return f"{path}{file_name.replace('.mp3', '.mp4')}"

    def convert_from_mp3_to_wav(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        from pydub import AudioSegment

        sound = AudioSegment.from_mp3(file_name)
        sound.export(f"{path}{file_name.replace('.mp3', '.wav')}")
        return f"{path}{file_name.replace('.mp3', '.wav')}"

    def convert_from_mp4_to_gif(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        from moviepy.editor import VideoFileClip

        video_clip = VideoFileClip(file_name)
        video_clip.write_gif(f"{path}{file_name.replace('.mp4', '.gif')}")
        return f"{path}{file_name.replace('.mp4', '.gif')}"

    def convert_from_mp4_to_mkv(self, conversion):
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
            f"{path}{file_name.replace('.mp4', '.mkv')}",
        ]
        p = subprocess.Popen(cmd)
        p.communicate()
        return f"{path}{file_name.replace('.mp4', '.mkv')}"

    def convert_from_mp4_to_mov(self, conversion):
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
            "-acodec",
            "copy",
            "-vcodec",
            "copy",
            f"{path}{file_name.replace('.mp4', '.mov')}",
        ]
        p = subprocess.Popen(cmd)
        p.communicate()
        return f"{path}{file_name.replace('.mp4', '.mov')}"

    def convert_from_pdf_to_epub(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        cmd = ["ebook-convert", file_name, f"{path}{file_name.replace('.pdf', '.epub')}"]
        p = subprocess.Popen(cmd)
        p.communicate()
        return f"{path}{file_name.replace('.pdf', '.epub')}"

    def convert_from_pdf_to_doc(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        from pdf2docx import parse

        parse(file_name, f"{path}{file_name.replace('.pdf', '.doc')}")
        return f"{path}{file_name.replace('.pdf', '.doc')}"

    def convert_from_pdf_to_docx(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        parse(file_name, f"{path}{file_name.replace('.pdf', '.docx')}")
        return f"{path}{file_name.replace('.pdf', '.docx')}"

    def convert_from_pdf_to_jpg(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        from pdf2image import convert_from_path

        image = convert_from_path(file_name)
        images_zip = []
        count = 0
        for page in range(len(image)):
            image[page].save(f"{path}{file_name.replace('.pdf', f'{count}.jpg')}")
            images_zip.append(f"{path}{file_name.replace('.pdf', f'{count}.jpg')}")
            count += 1
        # Zip it
        from zipfile import ZipFile

        zip_file = ZipFile(f"{path}images.zip", "w")
        for image in images_zip:
            zip_file.write(image)
        zip_file.close()
        return f"{path}images.zip"

    def convert_from_pdf_to_png(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        import fitz

        doc = fitz.open(file_name)
        page_count = doc.page_count
        images_zip = []
        for page in range(page_count):
            page = doc.load_page(page)
            pix = page.get_pixmap()
            output = f"{path}{file_name.replace('.pdf', f'_{page}.png')}"
            pix.save(output)
            images_zip.append(output)
        # Zip it
        from zipfile import ZipFile

        zip_file = ZipFile(f"{path}images.zip", "w")
        for image in images_zip:
            zip_file.write(image)
        zip_file.close()
        return f"{path}images.zip"

    def convert_from_pdf_to_pptx(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        cmd = ["pdf2pptx", file_name, "-o", f"{path}{file_name.replace('.pdf', '.pptx')}"]
        p = subprocess.Popen(cmd)
        p.communicate()
        return f"{path}{file_name.replace('.pdf', '.pptx')}"
