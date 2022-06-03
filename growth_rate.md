```python
import pandas as pd 
import numpy as np
from scipy import stats
import scipy as sp
import statsmodels.api as sm #per OLS
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
from time import time
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
from statsmodels.compat import lzip
import statsmodels.stats.api as sms

#-----------------------------------------------------–#
#----------------TASSO DI CRESCITA---------------------#
#-----------------------------------------------------–#

#ottobre:
ln_deceduti_ott = np.log(df3["deceduti"])
ln_icu_ott = np.log(df3["terapia_intensiva"])
lag_dec_ott = ln_deceduti_ott.shift(1)
lag_icu_ott = ln_icu_ott.shift(1)
dec_rate_ott = ln_deceduti_ott-lag_dec_ott
icu_rate_ott = ln_icu_ott-lag_icu_ott

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(dec_rate_ott, label="tasso di crescita deceduti da ottobre")
ax2 = ax.twinx()
ax2.plot(icu_rate_ott,color="orange",label="tasso di crescita ICU da ottobre")

#tasso crescita log positivi
ln_pos_ott = np.log(df3["nuovi_positivi"])
lag_pos_ott = ln_pos_ott.shift(1)
pos_rate_ott = ln_pos_ott-lag_pos_ott

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(pos_rate_ott, label="tasso di crescita positivi da ottobre")

#tasso crescita NONlog positivi
pos_ott = df3["nuovi_positivi"]
lag1_pos_ott = pos_ott.shift(1)
pos_rate_ott_nolog = pos_ott-lag1_pos_ott

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(pos_rate_ott_nolog, label="tasso di crescita positivi da ottobre")


#settembre:
ln_deceduti_sett = np.log(df2["deceduti"])
ln_icu_sett = np.log(df2["terapia_intensiva"])
lag_dec_sett = ln_deceduti_sett.shift(1)
lag_icu_sett = ln_icu_sett.shift(1)
dec_rate_sett = ln_deceduti_sett - lag_dec_sett
icu_rate_sett = ln_icu_sett - lag_icu_sett

#media mobile del tasso di crescita in log(settembre):
MA_icu_rate = icu_rate_sett.rolling(7).mean()
MA_dec_rate = dec_rate_sett.rolling(7).mean()
#GRAFICO TASSI DI CRESCITA DA SETTEMBRE
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(icu_rate_sett,"o:",markersize=2, color="orange", label="tasso di crescita (log) ICU da settembre-Asse SX")
ax.plot(MA_icu_rate, color="#ffa500ff", linewidth=2, label="MA(7) tasso di crescita ICU-Asse SX")
ax2 = ax.twinx()
ax2.plot(dec_rate_sett,"o:",markersize=2, label="tasso di crescita (log) deceduti da settembre-Asse DX")
ax2.plot(MA_dec_rate,"#1f77b4ff",linewidth=2, label="MA(7) tasso di crescita deceduti-Asse DX")
ax.set_xlabel("Giorni")
ax.set_xticklabels([])
ax.set_xlabel("@giuseppecangemi", position=(0.,1e6),horizontalalignment="left" )
fig.legend(loc=1, bbox_to_anchor=(0.5,1), bbox_transform=ax.transAxes)


#luglio 2021:
ln_deceduti_lug = np.log(df_lug["deceduti"])
ln_icu_lug = np.log(df_lug["terapia_intensiva"])
lag_dec_lug = ln_deceduti_lug.shift(1)
lag_icu_lug = ln_icu_lug.shift(1)
dec_rate_lug = ln_deceduti_lug - lag_dec_lug
icu_rate_lug = ln_icu_lug - lag_icu_lug

#media mobile del tasso di crescita in log(settembre):
MA_icu_rate = icu_rate_lug.rolling(7).mean()
MA_dec_rate = dec_rate_lug.rolling(7).mean()
#GRAFICO TASSI DI CRESCITA DA LUGLIO 2021
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(icu_rate_lug,"o:",markersize=2, color="orange", label="tasso di crescita (log) ICU da settembre-Asse SX")
ax.plot(MA_icu_rate, color="#ffa500ff", linewidth=2, label="MA(7) tasso di crescita ICU-Asse SX")
ax2 = ax.twinx()
ax2.plot(dec_rate_lug,"o:",markersize=2, label="tasso di crescita (log) deceduti da settembre-Asse DX")
ax2.plot(MA_dec_rate,"#1f77b4ff",linewidth=2, label="MA(7) tasso di crescita deceduti-Asse DX")
ax.set_xlabel("Giorni")
#ax.set_xticklabels([])
ax.set_xlabel("Kangemi_Edu", position=(0.,1e6),horizontalalignment="left" )
fig.legend(loc=1, bbox_to_anchor=(0.5,1), bbox_transform=ax.transAxes)

# DA LUGLIO 2021 SENZA LOG
dec = df_lug["deceduti"].shift(1)
deceduti_lug = df_lug["deceduti"]-dec

ter_lugl = df_lug["terapia_intensiva"].shift(1)
terapia_lugl = df_lug["terapia_intensiva"]-ter_lugl

MA_dec_lug = deceduti_lug.rolling(7).mean()
MA_icu_lug = terapia_lugl.rolling(7).mean()

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(deceduti_lug, "o:", alpha=0.6, markersize = 2, label="tasso di variazione deceduti da luglio 2021")
ax.plot(terapia_lugl,"o:" ,alpha=0.6, markersize = 2,label="tasso di variazione ICU da luglio 2021")
ax.plot(MA_icu_lug, "orange",linewidth=2, label="MA tasso di variazione ICU")
ax.plot(MA_dec_lug, "#069AF2",linewidth=2, label="MA tasso di variazione deceduti")
ax.set_title("Tasso di variazione (no log) ICU & Decessi da luglio 2021")
ax.set_xlabel ("Kangemi_Edu", position=(0.,1e6),horizontalalignment="left" )
ax.set_xticklabels([])
plt.axhline(y=0, color="k")
plt.legend()

#TASSO DI CRESCITA TOTALE:
ln_icu = np.log(df["terapia_intensiva"])
lag_icu = ln_icu.shift(1)
icu_rate = ln_icu - lag_icu

ln_dec = np.log(df["deceduti"])
lag_dec = ln_dec.shift(1)
dec_rate = ln_dec - lag_dec

MA_icu_rate = icu_rate.rolling(7).mean()
MA_dec_rate = dec_rate.rolling(7).mean()

dec_log = np.log(df3["deceduti"])
ter_log = np.log(df3["terapia_intensiva"])
dec_lag = dec_log.shift(1)
ter_lag = ter_log.shift(1)
tasso_var_dec = dec_log-dec_lag
tasso_var_ter = ter_log-ter_lag

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(tasso_var_ter, label="tasso di crescita (log)- Asse SX ")
ax2 = ax.twinx()
plt.plot(tasso_var_dec, color="orange", label="tasso di crescita (log)- Asse DX ")
fig.legend(loc=1, bbox_to_anchor=(0.8,1), bbox_transform=ax.transAxes)

#da settembre (senza log)
dec = df2["deceduti"].shift(1)
deceduti_sett = df2["deceduti"]-dec

dec_lugl = df1["deceduti"].shift(1)
deceduti_lugl = df1["deceduti"]-dec_lugl

ter = df2["terapia_intensiva"].shift(1)
terapia_sett = df2["terapia_intensiva"]-ter

ter_lugl = df1["terapia_intensiva"].shift(1)
terapia_lugl = df1["terapia_intensiva"]-ter_lugl


sns.regplot(terapia_sett,deceduti_sett)

terapia_sett = sm.add_constant(terapia_sett)
modelll = sm.OLS(deceduti_sett, terapia_sett, missing="drop")
res = modelll.fit()
print(res.summary())

ma_terapia_sett = terapia_sett.rolling(7).mean()
ma_deceduti_sett = deceduti_sett.rolling(7).mean()

fig = plt.figure()
ax = fig.add_subplot()
plt.plot(terapia_sett, "o:", markersize=2, label="Tasso di variazione ICU")
plt.plot(deceduti_sett, "o:", markersize=2, label="Tasso di variazione deceduti")
plt.plot(ma_terapia_sett, color="#1f77b4ff", linewidth=2, label="Media mobile sul tasso di variazione ICU")
plt.plot(ma_deceduti_sett, color="orange", linewidth=2,label="Media mobile sul tasso di variazione deceduti")
plt.axhline(y=0, linestyle="--",linewidth=1, color="k")
ax.set_xlabel("Kangemi_Edu",position=(0.,1e6), horizontalalignment="left")
ax.set_title("Tasso di crescita ICU & Deceduti")
plt.legend()


ma_terapia_lugl = terapia_lugl.rolling(7).mean()
ma_deceduti_lugl = deceduti_lugl.rolling(7).mean()

plt.plot(terapia_lugl, label="andamento ICU (da luglio)")
plt.plot(deceduti_lugl, label="andamento deceduti (da luglio)")
plt.plot(ma_terapia_lugl, label="andamento media mobile ICU (da luglio)")
plt.plot(ma_deceduti_lugl, label="andamento media mobile deceduti (da luglio)")
plt.axhline(y=0, color="k")
plt.legend()

#logaritmo tasso di crescita da 15 ago:
icu15 = (df15_ago["terapia_intensiva"])
dec15 = (df15_ago["deceduti"])
ln_icu15 = np.log(icu15)
ln_dec15 = np.log(dec15)
lag_icu15 = ln_icu15.shift(1)
lag_dec15 = ln_dec15.shift(1)
icu15_rate = ln_icu15 - lag_icu15 
dec15_rate = ln_dec15 - lag_dec15

MA_icu15 = icu15_rate.rolling(7).mean()
MA_dec15 = dec15_rate.rolling(7).mean()

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(icu15_rate, "o:",markersize=2,label="tasso di crescita log ICU-Asse SX", color="orange")
ax.plot(MA_icu15, color="orange", label="MA ICU_rate")
ax2 = ax.twinx()
ax2.plot(dec15_rate,"o:",markersize=2, label="tasso di crescita log Decessi-Asse DX")
ax2.plot(MA_dec15, color="#1f77b4ff", label="MA Decessi_rate")
fig.legend(loc=1, bbox_to_anchor=(0.8,1), bbox_transform=ax.transAxes) 
ax.set_xlabel ("Kangemi_Edu", position=(0.,1e6),horizontalalignment="left" )

#logaritmo tasso di crescita da LUGLIO 2021:
icu_lug = (df_lug["terapia_intensiva"])
dec_lug = (df_lug["deceduti"])
pos_lug = (df_lug["nuovi_positivi"])
ln_icu_lug = np.log(icu_lug)
ln_dec_lug = np.log(dec_lug)
ln_pos_lug = np.log(pos_lug)

lag_icu_lug = ln_icu_lug.shift(1)
lag_dec_lug = ln_dec_lug.shift(1)
lag_pos_lug = ln_pos_lug.shift(1)

icu_lug_rate = ln_icu_lug - lag_icu_lug
dec_lug_rate = ln_dec_lug - lag_dec_lug
pos_lug_rate = ln_pos_lug - lag_pos_lug

MA_icu_lug = icu_lug_rate.rolling(7).mean()
MA_dec_lug = dec_lug_rate.rolling(7).mean()
MA_pos_lug = pos_lug_rate.rolling(7).mean()

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(icu_lug_rate, "o:",markersize=2,label="tasso di crescita log ICU-Asse SX", color="orange")
ax.plot(MA_icu_lug, color="orange", label="MA ICU_rate")
ax2 = ax.twinx()
ax2.plot(dec_lug_rate,"o:",markersize=2, label="tasso di crescita log Decessi-Asse DX")
ax2.plot(MA_dec_lug, color="#1f77b4ff", label="MA Decessi_rate")
fig.legend(loc=1, bbox_to_anchor=(0.8,1), bbox_transform=ax.transAxes) 
ax.set_xlabel ("Kangemi_Edu", position=(0.,1e6),horizontalalignment="left" )

#tasso di crescita da luglio 2021 in log
fig= plt.figure()
ax = fig.add_subplot()
ax.plot(pos_lug_rate, "o:", markersize=2, label="Tasso di crescita log positivi daily", color="orange")
ax.plot(MA_pos_lug, color="orange", label="MA positivi daily")
plt.axhline(y=0, color="black")
fig.legend(loc=1, bbox_to_anchor=(0.8,1), bbox_transform=ax.transAxes) 
ax.set_xlabel ("Kangemi_Edu", position=(0.,1e6),horizontalalignment="left" )

#senza log: 
lag_icu15_nolog = icu15.shift(1)
lag_dec15_nolog = dec15.shift(1)
icu15_rate_nolog = icu15 - lag_icu15_nolog
dec15_rate_nolog = dec15 - lag_dec15_nolog

MA_icu15_nolog = icu15_rate_nolog.rolling(7).mean()
MA_dec15_nolog = dec15_rate_nolog.rolling(7).mean()

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(dec15_rate_nolog, "o:", markersize = 2, label="tasso di variazione deceduti dal 15 agosto")
ax.plot(icu15_rate_nolog,"o:" ,markersize = 2,label="tasso di variazione ICU dal 15 agosto")
ax.plot(MA_icu15_nolog, "#ff7f0eff", linewidth=2, label="MA tasso di variazione ICU")
ax.plot(MA_dec15_nolog,"#1f77b4ff", linewidth=2, label="MA tasso di variazione deceduti")
ax.set_title("Tasso di variazione (no log) ICU & Decessi dal 15 Agosto ad oggi")
ax.set_xlabel ("Kangemi_Edu", position=(0.,1e6),horizontalalignment="left" )
plt.legend()
```
