import ast
import os

from PIL import Image

directory_in_str = input("Dateipfad eingeben: ").strip()
to_resize = input("Auf bestimmte Größe zuschneiden? J/N: ").strip().lower() == "j"

# --- Process the directory and ensure that it exists --- #
if not os.path.isdir(directory_in_str):
    print(f"Das Verzeichnis '{directory_in_str}' existiert nicht.")
    exit(1)


def resize_image(size, filename):
    path = os.path.join(directory_in_str, filename)
    with Image.open(path) as im:
        im.thumbnail(size, Image.Resampling.LANCZOS)
        im.save(path, "JPEG")
    print(f"Bild '{filename}' auf Größe {size} skaliert.")


for file in os.listdir(directory_in_str):
    filename = os.fsdecode(file).lower()

    if filename.endswith((".jpg", ".jpeg", ".png")):
        path = os.path.join(directory_in_str, filename)

        if to_resize:
            try:
                size = ast.literal_eval(input("Breite, Höhe in px (z.B. (800, 600)): "))
                resize_image(size, filename)
            except (ValueError, SyntaxError):
                print("Ungültige Eingabe für Größe. Bitte erneut versuchen.")
                continue

        new_filename = f"{os.path.splitext(filename)[0]}.webp"
        with Image.open(path) as img:
            img.convert("RGB").save(
                os.path.join(directory_in_str, new_filename), "webp"
            )
        print(f"Bild '{filename}' in '{new_filename}' konvertiert.")
