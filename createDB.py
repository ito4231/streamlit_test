#%%
import pandas as pd

data = {
    '名前': ['太郎', '花子', '次郎', '美紀', '健太'],
    '年齢': [25, 30, 22, 28, 35],
    '性別': ['男性', '女性', '男性', '女性', '男性'],
    '都市': ['東京', '大阪', '名古屋', '札幌', '福岡']
}

df = pd.DataFrame(data)

df
#%%
combined_df = pd.concat([df, df], ignore_index=True)
combined_df
#%%
df = combined_df
# %%
import sqlite3
with sqlite3.connect("test.db") as conn:
    df.to_sql("test",conn,if_exists="replace")

# %%
