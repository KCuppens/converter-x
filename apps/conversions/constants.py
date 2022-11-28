FILE_TYPE_PDF = "pdf"
FILE_TYPE_DOCX = "docx"
FILE_TYPE_JPG = "jpg"
FILE_TYPE_HEIC = "heic"
FILE_TYPE_MP4 = "mp4"
FILE_TYPE_MP3 = "mp3"
FILE_TYPE_WAV = "wav"
FILE_TYPE_MKV = "mkv"
FILE_TYPE_PNG = "png"
FILE_TYPE_MOV = "mov"
FILE_TYPE_M4A = "m4a"
FILE_TYPE_GIF = "gif"
FILE_TYPE_DOC = "doc"
FILE_TYPE_PPTX = "pptx"
FILE_TYPE_EPUB = "epub"

FILE_TYPES = [
    (FILE_TYPE_PDF, "PDF"),
    (FILE_TYPE_DOCX, "docx"),
    (FILE_TYPE_JPG, "Jpg"),
    (FILE_TYPE_HEIC, "Heic"),
    (FILE_TYPE_MP4, "Mp4"),
    (FILE_TYPE_MP3, "Mp3"),
    (FILE_TYPE_WAV, "Wav"),
    (FILE_TYPE_MKV, "Mkv"),
    (FILE_TYPE_PNG, "Png"),
    (FILE_TYPE_MOV, "Mov"),
    (FILE_TYPE_M4A, "M4a"),
    (FILE_TYPE_GIF, "gif"),
    (FILE_TYPE_DOC, "doc"),
    (FILE_TYPE_PPTX, "pptx"),
    (FILE_TYPE_EPUB, "epub"),
]

STATUS_OPEN = "open"
STATUS_PENDING = "pending"
STATUS_CLOSED = "closed"

STATUSES_FILE = [
    (STATUS_OPEN, "Open"),
    (STATUS_PENDING, "Pending"),
    (STATUS_CLOSED, "Closed"),
]


CONVERT_OPTIONS = [
    "pdf_jpg",
    "jpg_pdf",
    "heic_jpg",
    "mkv_mp4",
    "mp4_mkv",
    "mp3_wav",
    "wav_mp3",
    "pdf_docx",
    "docx_pdf",
    "mp4_mp3",
    "mp3_mp4",
    "pdf_png",
    "png_pdf",
    "mov_mp4",
    "mp4_mov",
    "jpg_png",
    "png_jpg",
    "m4a_mp3",
    "mp3_m4a",
    "mp4_gif",
    "gif_mp4",
    "doc_pdf",
    "pdf_doc",
    "pptx_pdf",
    "pdf_pptx",
    "epub_pdf",
    "pdf_epub",
]

SHORTCUT_OPTIONS = {
    "heic": "image/heic",
    "mkv": "video/x-matroska",
    "wav": "audio/wav",
    "docx": "application/vnd.openxmlformats-" "officedocument.wordprocessingml.document",
    "mov": "video/quicktime",
    "jpg": "image/jpeg",
    "png": "image/png",
    "m4a": "audio/m4a",
    "mp3": "audio/mpeg",
    "mp4": "video/mp4",
    "gif": "image/gif",
    "doc": "application/msword",
    "pptx": "application/vnd.openxmlformats-" "officedocument.presentationml.presentation",
    "pdf": "application/pdf",
    "epub": "application/epub+zip",
}

SHORTCUT_OPTIONS_REVERSED = {
    "image/heic": "heic",
    "video/x-matroska": "mkv",
    "audio/wav": "wav",
    "application/vnd.openxmlformats" "-officedocument.wordprocessingml.document": "docx",
    "video/quicktime": "mov",
    "image/jpeg": "jpg",
    "image/png": "png",
    "audio/m4a": "m4a",
    "audio/mpeg": "mp3",
    "video/mp4": "mp4",
    "image/gif": "gif",
    "application/msword": "doc",
    "application/vnd.openxmlformats-" "officedocument.presentationml.presentation": "pptx",
    "application/pdf": "pdf",
    "application/epub+zip": "epub",
}

MEDIA_TYPE_DOCUMENT = "document"
MEDIA_TYPE_IMAGE = "image"
MEDIA_TYPE_AUDIO = "audio"
MEDIA_TYPE_VIDEO = "video"

MEDIA_TYPES = [
    (MEDIA_TYPE_DOCUMENT, "Document"),
    (MEDIA_TYPE_IMAGE, "Image"),
    (MEDIA_TYPE_AUDIO, "Audio"),
    (MEDIA_TYPE_VIDEO, "Video"),
]
