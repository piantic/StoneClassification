import os
import shutil
import numpy as np
src = 'data/Train'
dst = 'data/Test'
stones = sorted([stone for stone in os.listdir(src) if os.path.isdir(os.path.join(src, stone))]) 

ratio = 0.1

for stone in stones:
    os.makedirs(os.path.join(dst, stone), exist_ok=True)
    stone_path = os.path.join(src, stone)
    img_lists = sorted(os.listdir(stone_path))
    indices = np.random.choice(len(img_lists), int(len(img_lists)*ratio), replace=False)
    for idx in indices:
        shutil.move(os.path.join(stone_path, img_lists[idx]), os.path.join(dst, stone, img_lists[idx]))