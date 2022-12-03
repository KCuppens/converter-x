import subprocess

from pdf2docx import parse

from apps.convert.utils import get_initial_file_for_conversion


class FileConverter:
    def convert_from_doc_to_pdf(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        # Convert
        cmd = ["soffice", "--convert-to", "pdf", "--outdir", path, file_name]
        p = subprocess.Popen(cmd)
        p.communicate()
        return f"{path}{file_name.replace('.doc', '.pdf')}"

    def convert_from_docx_to_pdf(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        # Convert
        cmd = ["soffice", "--convert-to", "pdf", "--outdir", path, file_name]
        p = subprocess.Popen(cmd)
        p.communicate()
        return f"{path}{file_name.replace('.docx', '.pdf')}"

    def convert_from_epub_to_pdf(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.epub', '.pdf')}"
        # Convert
        cmd = ["ebook-convert", file_name, output]
        p = subprocess.Popen(cmd)
        p.communicate()
        return output

    def convert_from_gif_to_mp4(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.gif', '.mp4')}"
        # Convert
        from moviepy.editor import VideoFileClip

        video_clip = VideoFileClip(file_name)
        video_clip.write_videofile(output)
        return output

    def convert_from_m4a_to_mp3(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.m4a', '.mp3')}"
        # Convert
        from pydub import AudioSegment

        sound = AudioSegment.from_file(file_name)
        sound.export(output)
        return output

    def convert_from_jpg_to_pdf(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.jpg', '.pdf')}"
        # Convert
        from PIL import Image

        image = Image.open(file_name)
        image_convert = image.convert("RGB")
        image_convert.save(output)
        return output

    def convert_from_jpg_to_png(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.jpg', '.png')}"
        # Convert
        from PIL import Image

        image = Image.open(file_name)
        image = image.convert("RGB")
        image.save(output)
        return output

    def convert_from_heic_to_jpg(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.heic', '.jpg')}"
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
        data.save(output)
        return output

    def convert_from_mkv_to_mp4(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.mkv', '.mp4')}"
        # Convert
        cmd = ["ffmpeg", "-i", file_name, "-codec", "copy", output]
        p = subprocess.Popen(cmd)
        p.communicate()
        return output

    def convert_from_mov_to_mp4(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.mov', '.mp4')}"
        # Convert
        cmd = ["ffmpeg", "-i", file_name, output]
        p = subprocess.Popen(cmd)
        p.communicate()
        return output

    def convert_from_mp3_to_m4a(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.mp3', '.m4a')}"
        # Convert
        from pydub import AudioSegment

        sound = AudioSegment.from_file(file_name)
        sound.export(output)
        return output

    def convert_from_mp3_to_mp4(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.mp3', '.mp4')}"
        # Convert
        cmd = ["ffmpeg", "-i", file_name, "-acodec", "copy", output]
        p = subprocess.Popen(cmd)
        p.communicate()
        return output

    def convert_from_mp3_to_wav(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.mp3', '.wav')}"
        # Convert
        from pydub import AudioSegment

        sound = AudioSegment.from_mp3(file_name)
        sound.export(output)
        return output

    def convert_from_mp4_to_gif(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.mp4', '.gif')}"
        # Convert
        from moviepy.editor import VideoFileClip

        video_clip = VideoFileClip(file_name)
        video_clip.write_gif(output)
        return output

    def convert_from_mp4_to_mkv(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.mp4', '.mkv')}"
        # Convert
        cmd = [
            "ffmpeg",
            "-i",
            file_name,
            "-codec",
            "copy",
            output,
        ]
        p = subprocess.Popen(cmd)
        p.communicate()
        return output

    def convert_from_mp4_to_mov(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.mp4', '.mov')}"
        # Convert
        cmd = [
            "ffmpeg",
            "-i",
            file_name,
            "-acodec",
            "copy",
            "-vcodec",
            "copy",
            output,
        ]
        p = subprocess.Popen(cmd)
        p.communicate()
        return output

    def convert_from_pdf_to_epub(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.pdf', '.epub')}"
        # Convert
        cmd = ["ebook-convert", file_name, output]
        p = subprocess.Popen(cmd)
        p.communicate()
        return output

    def convert_from_pdf_to_doc(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.pdf', '.doc')}"
        # Convert
        from pdf2docx import parse

        parse(file_name, output)
        return output

    def convert_from_pdf_to_docx(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.pdf', '.docx')}"
        # Convert
        parse(file_name, output)
        return output

    def convert_from_pdf_to_jpg(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
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
        file_name, path = get_initial_file_for_conversion(conversion)
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
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.pdf', '.pptx')}"
        # Convert
        cmd = ["pdf2pptx", file_name, "-o", output]
        p = subprocess.Popen(cmd)
        p.communicate()
        return output

    def convert_from_png_to_jpg(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.png', '.jpg')}"
        # Convert
        from PIL import Image

        image = Image.open(file_name)
        image.save(output)
        return output

    def convert_from_png_to_pdf(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.png', '.pdf')}"
        # Convert
        from PIL import Image

        image = Image.open(file_name)
        image = image.convert("RGB")
        image.save(output)
        return output

    def convert_from_pptx_to_pdf(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        # Convert

        cmd = ["soffice", "--convert-to", "pdf", "--outdir", path, file_name]
        p = subprocess.Popen(cmd)
        p.communicate()
        return f"{path}{file_name.replace('.pptx', '.pdf')}"

    def convert_from_wav_to_mp3(self, conversion):
        initial_file = conversion.initial_file
        r = requests.get(initial_file.file.url)
        file_name = get_unique_file_name(initial_file.file)
        open(file_name, "wb").write(r.content)
        # Get conversion path
        path = get_conversion_path(conversion)
        # Convert
        from pydub import AudioSegment

        sound = AudioSegment.from_mp3(file_name)
        sound.export(f"{path}{file_name.replace('.wav', '.mp3')}")
        return f"{path}{file_name.replace('.wav', '.mp3')}"

    def convert_from_wav_to_mp3(self, conversion):
        file_name, path = get_initial_file_for_conversion(conversion)
        output = f"{path}{file_name.replace('.wav', '.mp3')}"
        # Convert
        from pydub import AudioSegment

        sound = AudioSegment.from_mp3(file_name)
        sound.export(output)
        return output
