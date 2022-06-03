```python
df_r = df[["data", "terapia_intensiva", "nuovi_positivi", "var_tamponi", "var_deceduti",
             "ricoverati_con_sintomi", "var_osp"]].iloc[486:]       

r_real_pos = df_r["nuovi_positivi"] / lag7_pos
ma_semlogy = r_real_pos.rolling(7).mean()


fig = plt.figure()
ax = fig.add_subplot()
plt.semilogy(r_real_pos, "o", alpha=0.5, label="Positivi giornalieri rispetto la settimana precedente")
plt.semilogy(ma_semlogy, alpha=0.7, label="Media mobile a 7 giorni")
plt.axhline(y=1, linestyle="--" ,color="k", linewidth=2)
ax.set_xlabel ("@giuseppecangemi", position=(0.,1e6),horizontalalignment="left" )
plt.title(label="Incremento settimanale positivi giornalieri", fontsize=15)


#stesso calcolo con DECESSI-OSPEDALIZZAZIONI
lag7_dec = df_r["var_deceduti"].shift(7)
r_dec = df_r["var_deceduti"] - lag7_dec

MA_r_dec = r_dec.rolling(7).mean()

fig = plt.figure()
ax = fig.add_subplot()
plt.plot(r_dec,"o", alpha=0.5, label="Decessi giornalieri rispetto la settimana precedente")
plt.plot(MA_r_dec, alpha=0.7, label="Media mobile a 7 giorni")
plt.axhline(y=0, linestyle="--" ,color="k", linewidth=2)
ax.set_xlabel ("@giuseppecangemi", position=(0.,1e6),horizontalalignment="left" )
plt.title(label="Incremento settimanale decessi giornalieri", fontsize=15)
#plt.suptitle("Incremento settimanale positivi giornalieri")
#plt.title(label="Incremento settimanale positivi giornalieri")
ax.set_xticklabels(["15/07", "8/07","28/07", "17/08","6/09", "26/09","16/10", "3/11","15/10", "15/07"])
plt.legend()
plt.grid(linewidth=0.3)

#ospedalizzazioni:
lag7_osp = df_r["var_osp"].shift(7)
r_osp = df_r["var_osp"] - lag7_osp

MA_r_osp = r_osp.rolling(7).mean()    

fig = plt.figure()
ax = fig.add_subplot()
plt.plot(r_osp,"o", alpha=0.5, label="Ospedalizzazioni giornalieri rispetto la settimana precedente")
plt.plot(MA_r_osp,"orange", alpha=0.7, label="Media mobile a 7 giorni")
plt.axhline(y=0, linestyle="--" ,color="k", linewidth=2)
ax.set_xlabel ("Kangemi_Edu", position=(0.,1e6),horizontalalignment="left" )
plt.title(label="Incremento settimanale ospedalizzazioni giornalieri", fontsize=15)
#plt.suptitle("Incremento settimanale positivi giornalieri")
#plt.title(label="Incremento settimanale positivi giornalieri")
ax.set_xticklabels(["15/07", "8/07","28/07", "17/08","6/09", "26/09","16/10", "3/11","15/10", "15/07"])
plt.legend()
plt.grid(linewidth=0.3)

#TERAPIA INTENSIVA:
plt.plot(df_lug["var_icu"], "o", alpha=0.5)
plt.plot(df_lug["MA7_icu"])
plt.grid()
plt.axhline(y=0, linestyle="dashed", color="black")
plt.title("Incremento Terapia Intensiva da luglio 2021")

##########################################################################################
##########################################################################################
######Incremento settimanale principali indicatori: Positivi-Decessi-Ospedalizzazioni#####
##########################################################################################
##########################################################################################
#fig = plt.figure()
#fig, ax = fig.add_subplot()

f, axs  = plt.subplots(3)
axs[0].plot(r_pos,"o", alpha=0.5, label="$\mathbf{Positivi}$ giornalieri rispetto la settimana precedente")
axs[0].plot(MA_r,"orange", alpha=0.7, label="Media mobile a 7 giorni")
axs[0].axhline(y=0, linestyle="--" ,color="k", linewidth=2)
axs[0].set_xticklabels(["15/07", "8/07","28/07", "17/08","6/09", "26/09","16/10", "5/11","15/10", "15/07"])

axs[1].plot(r_dec,"o", alpha=0.5, label=" $\mathbf{Decessi}$ giornalieri rispetto la settimana precedente")
axs[1].plot(MA_r_dec,"orange", alpha=0.7, label="Media mobile a 7 giorni")
axs[1].axhline(y=0, linestyle="--" ,color="k", linewidth=2)
axs[1].set_xticklabels(["15/07", "8/07","28/07", "17/08","6/09", "26/09","16/10", "5/11","15/10", "15/07"])

axs[2].plot(r_osp,"o", alpha=0.5, label="$\mathbf{Ospedalizzazioni}$ giornalieri rispetto la settimana precedente")
axs[2].plot(MA_r_osp,"orange", alpha=0.7, label="Media mobile a 7 giorni")
axs[2].axhline(y=0, linestyle="--" ,color="k", linewidth=2)
axs[2].set_xlabel ("@giuseppecangemi", position=(0.,1e6),horizontalalignment="left" )
axs[2].set_xticklabels(["15/07", "8/07","28/07", "17/08","6/09", "26/09","16/10", "5/11","15/10", "15/07"])


axs[0].legend(loc="lower left")
axs[1].legend(loc="lower left")
axs[2].legend(loc="lower left")
axs[0].set_title("Incremento settimanale principali indicatori: Positivi-Decessi-Ospedalizzazioni",
                 fontsize=20)



















#CALCOLO DIFFERENTE SENZA SEMIOLOGY

df_r = df[["data", "terapia_intensiva", "nuovi_positivi", "var_tamponi", "var_deceduti",
             "ricoverati_con_sintomi", "var_osp"]].iloc[486:]       

lag7_pos = df_r["nuovi_positivi"].shift(7)
r_pos = df_r["nuovi_positivi"] - lag7_pos

MA_r = r_pos.rolling(7).mean()

fig = plt.figure()
ax = fig.add_subplot()
plt.plot(r_pos,"o", alpha=0.5, label="Positivi giornalieri rispetto la settimana precedente")
plt.plot(MA_r, alpha=0.7, label="Media mobile a 7 giorni")
plt.axhline(y=0, linestyle="--" ,color="k", linewidth=2)
ax.set_xlabel ("@giuseppecangemi", position=(0.,1e6),horizontalalignment="left" )
plt.title(label="Incremento settimanale positivi giornalieri", fontsize=15)
#plt.suptitle("Incremento settimanale positivi giornalieri")
#plt.title(label="Incremento settimanale positivi giornalieri")
ax.set_xticklabels(["15/07", "8/07","28/07", "17/08","6/09", "26/09","16/10", "5/11","15/10", "15/07"])
plt.grid(linewidth=0.3)

#######LOG
df_r = df[["data", "terapia_intensiva", "nuovi_positivi", "var_tamponi", "var_deceduti",
             "ricoverati_con_sintomi", "var_osp"]].iloc[486:]

df_r["ln_ti"] = np.log(df_r["terapia_intensiva"])
df_r["ln_pos"] = np.log(df_r["nuovi_positivi"])
df_r["ln_var_dec"] = np.log(df_r["var_deceduti"])
df_r["ln_ric"] = np.log(df_r["ricoverati_con_sintomi"])
df_r["ln_var_osp"] = np.log(df_r["var_osp"])

lag_ln_pos = df_r["ln_pos"].shift(7)
ln_r_pos = df_r["ln_pos"] - lag_ln_pos
ln_MA_r = ln_r_pos.rolling(7).mean()

fig = plt.figure()
ax = fig.add_subplot()
plt.plot(ln_r_pos,"o", alpha=0.5, label="Positivi giornalieri rispetto la settimana precedente")
plt.plot(ln_MA_r, alpha=0.7, label="Media mobile a 7 giorni")
plt.axhline(y=0, linestyle="--" ,color="k", linewidth=2)
ax.set_xlabel ("@giuseppecangemi", position=(0.,1e6),horizontalalignment="left" )
plt.title(label="Incremento settimanale positivi giornalieri", fontsize=15)
#plt.suptitle("Incremento settimanale positivi giornalieri")
#plt.title(label="Incremento settimanale positivi giornalieri")
ax.set_xticklabels(["15/07", "8/07","28/07", "17/08","6/09", "26/09","16/10", "5/11","15/10", "15/07"])
plt.grid(linewidth=0.3)



```
