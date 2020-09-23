import os
import shutil
import numpy as np
root = './Stone'
train = './Train'
test = './Test'
stones = sorted([stone for stone in os.listdir(root) if os.path.isdir(os.path.join(root, stone))]) 

ratio = 0.2

for stone in stones:
    if stone == "chalcopyrite":
        target = "chalcopyrite"
    else:
        target = "etc"
    
    stone_path = os.path.join(root, stone)
    stone_img_lists = sorted(os.listdir(stone_path))
    
    train_stone_path = os.path.join(train, target)
    test_stone_path = os.path.join(test, target)

    threshold = int(len(stone_img_lists)*ratio)

    for img in stone_img_lists[:threshold]:
        shutil.move(os.path.join(stone_path, img), os.path.join(test_stone_path, img))

    for img in stone_img_lists[threshold:]:
        shutil.move(os.path.join(stone_path, img), os.path.join(train_stone_path, img))