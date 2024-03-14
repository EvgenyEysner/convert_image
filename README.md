**Convert Image**

This is a small script that helps you to convert your images into a specific format.

For Linux users
```bash
. .venv/bin/activate
```
```bash
pip install pipenv
```

```bash
pipenv install
```
```bash

python main.py
```

Simply enter the path to files as string, for example:

`Eingabe: /home/user/Bilder`

Change the format here:

`directory_in_str + "/" + new_file[0] + ".webp", "webp"`

If you also need to crop the images, enter "J"