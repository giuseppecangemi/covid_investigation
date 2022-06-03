```python
import pandas as pd 

#DataFrame TOTAL al 2022-03-25:
df = pd.read_excel("/Users/giuseppecangemi/Desktop/Covid19_Sicily_ITA STATA/Covi19_Italy.xlsx")

#data manipulation
df["lag_tamp"] = df["tamponi"].shift(1)
df["var_tamponi"] = df["tamponi"] - df["lag_tamp"]

df["lag_osp"] = df["totale_ospedalizzati"].shift(1)
df["var_osp"] = df["totale_ospedalizzati"] - df["lag_osp"] #ospedalizzati giornalieri

df["lag_deceduti"] = df["deceduti"].shift(1)
df["var_deceduti"] = df["deceduti"] - df["lag_deceduti"]

#DataFrame da LUGLIO (2020) a 2022-03-25:
df1 = df[["data","terapia_intensiva","nuovi_positivi", "var_tamponi","deceduti", "var_deceduti"]].iloc[128:]
#DataFrame da SETTEMBRE a 2022-03-25:
df2 = df[["data","terapia_intensiva","nuovi_positivi", "var_tamponi", "data", "deceduti", "var_deceduti"]].iloc[190:]
#da ottobre 2020:
df3 = df[["data","terapia_intensiva","nuovi_positivi", "var_tamponi", "data", "deceduti", "var_deceduti"]].iloc[220:]
#dal15ago 2020:
df15_ago = df[["data","terapia_intensiva","nuovi_positivi", "var_tamponi","deceduti", "var_deceduti"]].iloc[173:]

#-----------------------------------------------–#
                    #2021#
                    
#DataFrame da APRILE 2021
df_apr = df[["data", "terapia_intensiva", "nuovi_positivi", "var_tamponi", "deceduti",
             "ricoverati_con_sintomi", "totale_ospedalizzati", "var_deceduti"]].iloc[402:]
#DataFrame da LUGLIO 2021
df_lug = df[["data", "terapia_intensiva", "nuovi_positivi", "var_tamponi", "deceduti",
             "ricoverati_con_sintomi", "totale_ospedalizzati", "var_deceduti"]].iloc[493:]

#data manipulation

df_apr["lag_sintomi"] = df_apr["ricoverati_con_sintomi"].shift(1)
df_apr["var_sintomi"] = df_apr["ricoverati_con_sintomi"] - df_apr["lag_sintomi"] #sintomi ric giornalieri

df_apr["lag_osp"] = df_apr["totale_ospedalizzati"].shift(1)
df_apr["var_osp"] = df_apr["totale_ospedalizzati"] - df_apr["lag_osp"] #ospedalizzati giornalieri

df_lug["lag_sintomi"] = df_lug["ricoverati_con_sintomi"].shift(1)
df_lug["var_sintomi"] = df_lug["ricoverati_con_sintomi"] - df_lug["lag_sintomi"] #sintomi ric giornalieri

df_lug["lag_osp"] = df_lug["totale_ospedalizzati"].shift(1)
df_lug["var_osp"] = df_lug["totale_ospedalizzati"] - df_lug["lag_osp"] #ospedalizzati giornalieri

#MEDIE MOBILI:
df["MA7var_tamp"] = df["var_tamponi"].rolling(7).mean()
df["MA7_pos"] = df["nuovi_positivi"].rolling(7).mean()
df["MA7_icu"] = df["terapia_intensiva"].rolling(7).mean() 
df["MA_osp"] = df["var_osp"].rolling(7).mean()
df["MA_dec"] = df["var_deceduti"].rolling(7).mean()
#df[~df.isin([np.nan, np.inf, -np.inf]).any(1)]
df_lug["MA7var_tamp"] = df_lug["var_tamponi"].rolling(7).mean()
df_lug["MA7_pos"] = df_lug["nuovi_positivi"].rolling(7).mean()
df_lug["MA7_terapia_intensiva"] = df_lug["terapia_intensiva"].rolling(7).mean() 
df_lug["MA_osp"] = df_lug["var_osp"].rolling(7).mean()
df_lug["MA_dec"] = df["var_deceduti"].rolling(7).mean()

diff_icu = df_lug["terapia_intensiva"].shift(1)
df_lug["var_icu"] = df_lug["terapia_intensiva"] - diff_icu
df_lug["MA7_icu"] = df_lug["var_icu"].rolling(7).mean()

```
