import os
import shutil
from sklearn.model_selection import train_test_split

# Paths
base_dir = 'Yolo Labelled/Yolo Labelled'
image_dir = os.path.join(base_dir, 'images')
label_dir = os.path.join(base_dir, 'labels')
train_image_dir = 'dataset/images/train'
val_image_dir = 'dataset/images/val'
train_label_dir = 'dataset/labels/train'
val_label_dir = 'dataset/labels/val'

# Create directories
os.makedirs(train_image_dir, exist_ok=True)
os.makedirs(val_image_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# List images and annotations
images = [f for f in os.listdir(base_dir) if f.endswith('.JPG')]
annotations = [f.replace('.JPG', '.txt') for f in images]

# Split into train and val sets
train_images, val_images, train_annotations, val_annotations = train_test_split(images, annotations, test_size=0.2, random_state=42)

# Move files
def move_files(file_list, source_dir, target_dir):
    for file in file_list:
        shutil.move(os.path.join(source_dir, file), os.path.join(target_dir, file))

move_files(train_images, base_dir, train_image_dir)
move_files(val_images, base_dir, val_image_dir)
move_files(train_annotations, base_dir, train_label_dir)
move_files(val_annotations, base_dir, val_label_dir)
