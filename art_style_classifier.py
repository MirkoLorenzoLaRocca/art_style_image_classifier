# I search wit the image with the greater size from the data folder using pillow and numpy
# Imports
import os
import keras

# path of the data folder
abs_path = os.path.abspath(__file__)
dir_path = os.path.dirname(abs_path)
directory = os.path.join(dir_path, 'data')

keras.utils.image_dataset_from_directory(
    directory,
    labels="inferred",
    label_mode="categorical",
    class_names=os.listdir(directory),
    color_mode="rgb",
    batch_size=32,
    image_size=(512, 512),
    shuffle=True,
    seed=123,
    validation_split=0.2,
    subset="both",
    interpolation="bilinear",
    follow_links=False,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    data_format=None,
    verbose=True,
)