import ast
import os

from PIL import Image

directory_in_str = str(input("Dateipfand eingeben: "))
to_resize = str(input("Auf bestimmte größe zuschneiden? J/N: ")).lower()

directory = os.fsencode(directory_in_str)


def resize_image(size, filename):
    path = directory_in_str + "/" + filename
    im = Image.open(path)
    im.thumbnail(size, Image.Resampling.LANCZOS)
    im.save(path, "JPEG")


for file in os.listdir(directory):
    filename = os.fsdecode(file)
    filename.lower()
    if to_resize == "j":
        size = ast.literal_eval(input("Breite, Höhe in .px: "))
        resize_image(size, filename)

    if (
        filename.endswith(".jpg")
        or filename.endswith(".png")
        or filename.endswith(".jpeg")
    ):
        path = directory_in_str + "/" + filename
        new_file = filename.rsplit(".", 1)

        Image.open(path).convert("RGB").save(
            directory_in_str + "/" + new_file[0] + ".webp", "webp"
        )
