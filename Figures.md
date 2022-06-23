```python
#GRAPH:ICU-nuovi_pos-movingaverage (tot.)
fig, ax = plt.subplots()
plt.plot(df["data"], df["terapia_intensiva"], color = "r", label="ICU")
plt.bar(df["data"], df["nuovi_positivi"], label="nuovi positivi")
plt.plot(df["data"],df["MA7_pos"], "--", label="Media mobile a 7 giorni dei nuovi positivi", color="orange")
#plt.plot(df["data"], df["MA_osp"], ".", label ="MA osp")
plt.legend()
ax.set_xticklabels([]) #per non mostrare l'asse x



#completa anche medie mobili icu
fig = plt.figure()
ax = fig.add_subplot(111)
plt.bar(df["data"], df["nuovi_positivi"], label="nuovi positivi")
plt.plot(df["MA7_pos"], "-.", color="black", label="media mobile 7gg nuovi positivi")
plt.plot(df["MA7_icu"], "--", color="r", label="media mobile 7gg ICU")
plt.plot(df["terapia_intensiva"], color="orange",label="ICU")
ax.set_xlabel("Kangemi_Edu", position=(0.,1e6), horizontalalignment="left")
ax.set_xticklabels([]) #per non mostrare l'asse x
plt.legend()

#con max posti letto
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(df["data"], df["terapia_intensiva"], color = "r", label="ICU")
ax.bar(df["data"], df["nuovi_positivi"], label="nuovi positivi")
plt.axhline(y=5293, color="k", label="max capienza TI (5293)-Asse SX")
ax2 = ax.twinx()
ax2.plot(df["data"],df["ricoverati_con_sintomi"], "--", label="ricoverati con sintomi-Asse DX", color="orange")
plt.axhline(y=37960, color="k", label="max capienza posti letto (37960)-Asse DX")
fig.legend(loc=1, bbox_to_anchor=(1,1), bbox_transform=ax.transAxes)
ax.set_xticklabels([]) #per non mostrare l'asse x



#RICOVERATI CON SINTOMI 
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(df["data"], df["ricoverati_con_sintomi"], label="ricoverati con sintomi-Asse SX")
ax2 = ax.twinx()
ax2.plot(df["terapia_intensiva"], color="red", label="terapia intensiva-Asse DX")
ax.set_xticklabels([]) #per non mostrare l'asse x
ax2.grid()
fig.legend(loc=1, bbox_to_anchor=(1,1), bbox_transform=ax.transAxes)

#6:26
#223:244
dff = pd.read_excel("/Users/giuseppecangemi/Desktop/Covid19_Sicily_ITA STATA/Covi19_Italy.xlsx").iloc[6:26]
dzz = pd.read_excel("/Users/giuseppecangemi/Desktop/Covid19_Sicily_ITA STATA/Covi19_Italy.xlsx").iloc[223:244]

fig = plt.figure()
ax = fig.add_subplot()
sns.regplot(dff["ricoverati_con_sintomi"], dff["terapia_intensiva"], label="1-21 Marzo")
sns.regplot(dzz["ricoverati_con_sintomi"], dzz["terapia_intensiva"], label="4-24 Ottobre")
plt.grid()
plt.legend()
ax.set_xlabel("Kangemi_Edu", position=(0.,1e6), horizontalalignment="left")
```
