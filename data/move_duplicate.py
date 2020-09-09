import os
import shutil
import numpy as np
import pandas as pd
from tqdm import tqdm
# %%
root = f'/Users/jerry/git/Jerry/StoneClassification/data/Train/'
stones = [stone for stone in os.listdir(root) if os.path.isdir(os.path.join(root, stone))]
for stone in stones:
    df = pd.read_csv(os.path.join(root, f"{stone}.csv"))
    # %%

    new_df = df.drop_duplicates("hash")
    # %%
    cnt = 0
    dst_root =f'/Users/jerry/git/Jerry/StoneClassification/data/tmp/{stone}'
    os.makedirs(dst_root, exist_ok=True)
    for file in df['filename']:
        if file not in new_df['filename'].to_list():
            src = os.path.join(root, stone, file)
            dst = os.path.join(dst_root, file)
            cnt += 1
            shutil.move(src, dst)
