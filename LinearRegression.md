```python
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm #per OLS


#Linear Regression su df TOTALE
# Y = terapia intensiva; X = nuovi positivi
model = sm.OLS(df["terapia_intensiva"],df["nuovi_positivi"])
results = model.fit()
print(results.summary())
df["residui"]=results.resid
#hist residui totali
sns.distplot(df["residui"])
#scatter residui totali
df.plot(x="data", y="residui", kind="scatter")
plt.axhline(y=0, color='orange')
#autocorrelazione dei residui elevata
#-------------------------#
#OLS da LUGLIO
#Y = terapia intensiva; X = nuovi positivi
model = sm.OLS(df1["terapia_intensiva"],df1["nuovi_positivi"])
results = model.fit()
print(results.summary())
#hist residui da luglio
df["residui1"]=results.resid
#scatter residui da luglio
sns.distplot(df["residui1"])
df.plot(x="data", y="residui1", kind="scatter")
plt.axhline(y=0, linestyle=":", color="black")

#OLS da SETTEMBRE
model = sm.OLS(df2["terapia_intensiva"],df2["nuovi_positivi"])
results = model.fit()
print(results.summary())
#hist residui da settembre
df["residui1"]=results.resid
#scatter residui da settembre
sns.distplot(df["residui1"])
df.plot(x="data", y="residui", kind="scatter")

#scatter e linear reg (praticamente nessuna informazione valida):
df.plot(y="terapia_intensiva", x="nuovi_positivi", kind="scatter")
plt.grid()
sns.regplot(df["nuovi_positivi"],df["terapia_intensiva"])
sns.regplot(y="terapia_intensiva", x="nuovi_positivi", data= df1, marker="+")
sns.regplot(y="terapia_intensiva", x="nuovi_positivi", data= df2, marker="+")

#OLS Y = terapia intensiva; X = nuovi positivi + costante
X = df["nuovi_positivi"]
X = sm.add_constant(X)
model3 = sm.OLS(df["terapia_intensiva"], X)
results3 = model3.fit()
print(results3.summary())
predict_X = results3.predict()
#OLS Y = terapia intensiva; X = nuovi positivi + costante da luglio
X = df1["nuovi_positivi"]
X = sm.add_constant(X)
model4 = sm.OLS(df1["terapia_intensiva"], X)
results4 = model4.fit()
print(results4.summary())
#OLS da settembre
X = df2["nuovi_positivi"]
X = sm.add_constant(X)
model5 = sm.OLS(df2["terapia_intensiva"], X)
results5 = model5.fit()
print(results5.summary())
#OLS nuovi_pos & ICU dal 15_ago
X = df15_ago["nuovi_positivi"]
X = sm.add_constant(X)
model5 = sm.OLS(df15_ago["terapia_intensiva"], X)
results5 = model5.fit(cov_type='HC3')
print(results5.summary())

#scatterplot con differenti slopes
sns.regplot(y="terapia_intensiva", x="nuovi_positivi", data= df, marker="+", label="totale")
sns.regplot(y="terapia_intensiva", x="nuovi_positivi", data= df1, marker="x", label="da luglio")
sns.regplot(y="terapia_intensiva", x="nuovi_positivi", data= df2, marker="o", label="da settembre")
plt.legend()

#OLS nuovi_pos & ICU da settembre w/power!
Xi = p(df2["nuovi_positivi"])
Xi = sm.add_constant(Xi)
model5 = sm.OLS(df2["terapia_intensiva"], Xi)
results5 = model5.fit()
print(results5.summary())

#POLYNOMIAL
coefs = np.polyfit(df1['nuovi_positivi'], df1['terapia_intensiva'], 2)
p = np.poly1d(coefs)

#plotto assieme quadratico
sns.regplot(df1['nuovi_positivi'], df1['terapia_intensiva'], "bo",marker="x", label="linear fit da luglio")
plt.plot(df1['nuovi_positivi'], p(df1['nuovi_positivi']), "r--", label="quadratic fit da luglio")
plt.legend()

#OLS: nuovi_pos al variare dei tamponi (da luglio)
X = df1["var_tamponi"] #il vettore X sono (o è) le var esogene
X = sm.add_constant(X)
model2=sm.OLS(df1["nuovi_positivi"], X)
results2 = model2.fit()
print(results2.summary())
#OLS: nuovi_pos al variare dei tamponi (da settembre)
X= df2["var_tamponi"]
X = sm.add_constant(X)
model2=sm.OLS(df2["nuovi_positivi"], X)
results2 = model2.fit()
print(results2.summary())

#OLS: nuovi_pos al variare dei tamponi (da luglio 2021)
X_lug = df_lug["var_tamponi"] #il vettore X sono (o è) le var esogene
X_lug = sm.add_constant(X_lug)
model_lug=sm.OLS(df_lug["nuovi_positivi"], X_lug)
results_lug = model_lug.fit()
print(results_lug.summary())

fig = plt.figure()
ax = fig.add_subplot(111)
sns.regplot(df_lug["var_tamponi"], df_lug["nuovi_positivi"]) 
plt.legend(labels=["Fitted Values", "Observation"], title="R^2=0.016 and NOT stat significant")
plt.title("Correlazione fra tamponi giornalieri e nuovi positivi: nessun effetto statistico")
ax.set_xlabel("Kangemi_Edu", position=(0.,1e6), horizontalalignment="left")

#NESSUNA SIGNIFICATIVITà STATISTICA


#OLS: nuovi_pos al variare dei tamponi (da settembre)
X = df2["var_tamponi"]
X = sm.add_constant(X)
model2=sm.OLS(df2["nuovi_positivi"], X)
results2 = model2.fit()
print(results2.summary())

coefs2 = np.polyfit(df2['var_tamponi'],df2["nuovi_positivi"], 2)
p2 = np.poly1d(coefs2)

sns.regplot(df2["var_tamponi"],df2["nuovi_positivi"])
plt.plot(df2["var_tamponi"], p2(df2["var_tamponi"]))


#provo con logaritmi
X1= np.log(df2["var_tamponi"])
Y1= np.log(df2["nuovi_positivi"])
Y2=Y1.iloc[1:231]
X1 = sm.add_constant(X1)
model_opp=sm.OLS(df2["nuovi_positivi"], X1)
results_opp = model_opp.fit()
print(results_opp.summary())

sns.regplot( df["tamponi"], df["totale_positivi"], marker="x", label="tot")



```
