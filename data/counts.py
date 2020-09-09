import os
import numpy as np

root = f'/Users/jerry/git/Jerry/StoneClassification/data/Train/'
stones = sorted([stone for stone in os.listdir(root) if os.path.isdir(os.path.join(root, stone))]) 

for stone in stones:
    path = os.path.join(root, stone)
    print(stone, len(os.listdir(path)))