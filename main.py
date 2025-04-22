import os
from PIL import Image

# --- Input from the user --- #
directory_in_str = input("Dateipfad eingeben: ").strip()
to_resize = input("Auf bestimmte Größe zuschneiden? (J/N): ").strip().lower() == "j"
target_format_input = input("Zielformat eingeben (webp/jpg/png/gif): ").strip().lower()
delete_original = input("Originaldateien nach Konvertierung löschen? (J/N): ").strip().lower() == "j"

# --- Format check and assignment --- #
format_mapping = {
    'jpg': 'JPEG',
    'jpeg': 'JPEG',
    'png': 'PNG',
    'webp': 'WEBP',
    'gif': 'GIF'
}

if target_format_input not in format_mapping:
    print(f"Das Format '{target_format_input}' wird nicht unterstützt.")
    exit(1)

target_format = format_mapping[target_format_input]
extension_mapping = {
    'JPEG': 'jpg',
    'PNG': 'png',
    'WEBP': 'webp',
    'GIF': 'gif'
}
target_extension = extension_mapping[target_format]

# --- Resize size input --- #
size = None
if to_resize:
    try:
        size_input = input("Gewünschte Größe (Breite,Höhe in px): ").strip()
        size = tuple(map(int, size_input.replace(' ', '').split(',')))
        if len(size) != 2:
            raise ValueError
    except ValueError:
        print("Ungültige Größenangabe. Format: 800,600")
        exit(1)

# --- Directory check --- #
if not os.path.isdir(directory_in_str):
    print(f"Verzeichnis '{directory_in_str}' existiert nicht!")
    exit(1)


def process_image(filename):
    original_path = os.path.join(directory_in_str, filename)
    base_name = os.path.splitext(filename)[0]
    new_filename = f"{base_name}.{target_extension}"
    new_path = os.path.join(directory_in_str, new_filename)

    try:
        with Image.open(original_path) as img:
            # --- Resize image if needed --- #
            if size:
                img.thumbnail(size, Image.Resampling.LANCZOS)

            # --- Transparency handling for JPEG --- #
            if target_format == 'JPEG' and img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')

            # --- Saving with format-dependent parameters --- #
            save_args = {}
            if target_format in ['JPEG', 'WEBP']:
                save_args['quality'] = 85

            img.save(new_path, format=target_format, **save_args)
            print(f"Konvertiert: {filename} -> {new_filename}")

            # Original löschen
            if delete_original and original_path != new_path:
                os.remove(original_path)
                print(f"Gelöscht: {filename}")

    except Exception as e:
        print(f"Fehler bei {filename}: {str(e)}")


# Bildverarbeitung
supported_extensions = ('.jpg', '.jpeg', '.png', '.gif')
for file in os.listdir(directory_in_str):
    filename = os.fsdecode(file)
    if filename.lower().endswith(supported_extensions):
        process_image(filename)