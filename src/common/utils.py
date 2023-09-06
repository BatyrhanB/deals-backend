import sys
import requests
from io import BytesIO
from uuid import uuid4
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


def compress_image(
    uploaded_image: InMemoryUploadedFile,
    thumbnail: tuple = (1024, 1024),
    quality: int = 50,
    is_url: bool = False,
):
    image_format: str = uploaded_image.name.split(".")[-1].upper()
    if image_format == "SVG":
        return uploaded_image

    tmp_image = (
        Image.open(requests.get(uploaded_image, stream=True).raw)
        if is_url
        else Image.open(uploaded_image)
    )
    tmp_image = tmp_image.convert("RGBA")
    output_io_stream = BytesIO()
    tmp_image.thumbnail(thumbnail)
    tmp_image.save(output_io_stream, format="WEBP", quality=quality)
    output_io_stream.seek(0)
    uploaded_image = InMemoryUploadedFile(
        output_io_stream,
        "ImageField",
        f"{uuid4()}.webp",
        f"image/webp",
        sys.getsizeof(output_io_stream),
        None,
    )
    tmp_image.close()
    return uploaded_image
