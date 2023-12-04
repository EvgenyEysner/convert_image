import os
from PIL import Image

directory_in_str = str(input("Eingabe: "))
directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    filename.lower()
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
