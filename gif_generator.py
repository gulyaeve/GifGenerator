from sys import argv
from os.path import exists

from PIL import Image

assert len(argv) > 1, "Нужно указать хотя бы один аргумент"

files = argv[1:]
for file in files:
    assert exists(file), f"Файл {file} не найден"

images = [Image.open(image) for image in files]

images[0].save(
    "out.gif",
    save_all=True,
    append_images=images[1:],
    duration=500,  # duration of each frame in milliseconds
    loop=0,  # loop forever
)
