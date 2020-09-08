import os
import shutil
import hashlib
import cv2 as cv
import numpy as np
import pandas as pd
from tqdm import tqdm
stones = ['chalcopyrite', 'etc', 'go', 'po']
for stone in stones:
    ROOT = stone
    filenames = sorted(os.listdir(ROOT))
    files = []
    hashes = []
    for file in tqdm(filenames):
        img = cv.imread(os.path.join(ROOT, file))
        # print(type(img))
        if type(img) == type(None):continue
        files.append(file)
        md5 = hashlib.md5()
        md5.update(img.tostring())
        hashes.append(md5.hexdigest())

    dic = {
        "filename": files,
        "hash": hashes
    }

    df = pd.DataFrame(dic)

    df.to_csv(f"./{ROOT}.csv", index=False)