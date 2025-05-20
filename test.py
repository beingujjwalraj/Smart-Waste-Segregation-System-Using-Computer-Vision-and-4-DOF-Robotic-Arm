import os
import shutil
from collections import defaultdict

# --- Source paths ---
source_train_img = "E-waste/train/images"
source_train_lbl = "E-waste/train/labels"
source_valid_img = "E-waste/valid/images"
source_valid_lbl = "E-waste/valid/labels"

# --- Destination paths ---
dest_base = "E-waste-mini"
dest_train_img = os.path.join(dest_base, "train/images")
dest_train_lbl = os.path.join(dest_base, "train/labels")
dest_valid_img = os.path.join(dest_base, "valid/images")
dest_valid_lbl = os.path.join(dest_base, "valid/labels")

# --- Create folders ---
for path in [dest_train_img, dest_train_lbl, dest_valid_img, dest_valid_lbl]:
    os.makedirs(path, exist_ok=True)

# --- Limits ---
max_train_per_class = 10
max_valid_per_class = 4

# --- Helper to copy image + label ---
def copy_file(img_path, lbl_path, dest_img_dir, dest_lbl_dir):
    shutil.copy(img_path, os.path.join(dest_img_dir, os.path.basename(img_path)))
    shutil.copy(lbl_path, os.path.join(dest_lbl_dir, os.path.basename(lbl_path)))

# --- Copy train images ---
train_counter = defaultdict(int)
for label_file in os.listdir(source_train_lbl):
    label_path = os.path.join(source_train_lbl, label_file)
    image_path = os.path.join(source_train_img, label_file.replace(".txt", ".jpg"))

    if not os.path.exists(image_path):
        continue  # Skip if image is missing

    with open(label_path, "r") as f:
        lines = f.readlines()
        if not lines:
            continue
        class_id = int(lines[0].split()[0])  # Take the first class (assuming single-class per image)

    if train_counter[class_id] < max_train_per_class:
        copy_file(image_path, label_path, dest_train_img, dest_train_lbl)
        train_counter[class_id] += 1

# --- Copy valid images ---
valid_counter = defaultdict(int)
for label_file in os.listdir(source_valid_lbl):
    label_path = os.path.join(source_valid_lbl, label_file)
    image_path = os.path.join(source_valid_img, label_file.replace(".txt", ".jpg"))

    if not os.path.exists(image_path):
        continue

    with open(label_path, "r") as f:
        lines = f.readlines()
        if not lines:
            continue
        class_id = int(lines[0].split()[0])

    if valid_counter[class_id] < max_valid_per_class:
        copy_file(image_path, label_path, dest_valid_img, dest_valid_lbl)
        valid_counter[class_id] += 1

# --- Summary ---
print("✅ Mini dataset created at:", dest_base)
print("📁 Training samples per class (max 10):")
for cid in sorted(train_counter): print(f"Class {cid}: {train_counter[cid]}")

print("\n📁 Validation samples per class (max 4):")
for cid in sorted(valid_counter): print(f"Class {cid}: {valid_counter[cid]}")