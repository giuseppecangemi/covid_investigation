import pandas as pd 
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from time import time
import statsmodels.api as sm #per OLS
from statsmodels.sandbox.regression.predstd import wls_prediction_std #per SD intervalo di confidenza
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
from scipy import stats
import scipy as sp
from statsmodels.compat import lzip
import statsmodels.stats.api as sms


#nov2021 585

df.drop(df.index[297], inplace=True)

df_ott2020 = df[["nuovi_positivi", "var_tamponi"]].iloc[220:311]
df_nov_2021 = df[["nuovi_positivi", "var_tamponi"]].iloc[585:]

#feb (342) -> 30 apr (431)
#per vedere intermezzo che succede con vax parziale
df_feb2021 = df[["nuovi_positivi", "var_tamponi"]].iloc[342:415]


slope, intercept, r_value, p_value, std_err = stats.linregress(df_ott2020['var_tamponi'], df_ott2020['nuovi_positivi'])
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(df_nov_2021['var_tamponi'], df_nov_2021['nuovi_positivi'])
slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(df_feb2021['var_tamponi'], df_feb2021['nuovi_positivi'])

#################
#################
#MODELLI
#################
#################
###modello NOVAX ott-dic 2020###
var = (df_ott2020["var_tamponi"])
var = sm.add_constant(var)
model_novax = sm.OLS(df_ott2020["nuovi_positivi"], var)
results_novax = model_novax.fit()
print(results_novax.summary())
res_novax = results_novax.resid
#test #p-value >0.05: non rifiuto la normalità degli errori
jarque_bera_test = stats.jarque_bera(res_novax)
jarque_bera_test

###modello SìVAX ott-dic 2021### std.err robusti!
var = (df_nov_2021["var_tamponi"])
var = sm.add_constant(var)
model_sivax = sm.OLS(df_nov_2021["nuovi_positivi"], var)
results_sivax = model_sivax.fit(cov_type='HAC',cov_kwds={'maxlags':1})
print(results_sivax.summary())
res_vax = results_sivax.resid

###modello FEB-MAG 2021###
sns.regplot(df_feb2021["var_tamponi"], df_feb2021["nuovi_positivi"])

xx= df_feb2021["var_tamponi"]
xx = sm.add_constant(xx)
mm = sm.OLS(df_feb2021["nuovi_positivi"], xx).fit()
print(mm.summary())
res_vaxparziali = mm.resid

#test #p-value >0.05: non rifiuto la normalità degli errori
jb_test_vaxparziali = stats.jarque_bera(res_vaxparziali)
jb_test_vaxparziali


#####################
#####################

sns.histplot(res_novax, kde=True, label="ottobre-dicembre 2020", color="orange", alpha=0.4 )
sns.histplot(res_vax, kde=True, alpha=0.55, label="ottobre-dicembre 2021")
plt.legend()

sns.histplot(res_novax, kde=True, label="ottobre-dicembre 2020", color="orange", alpha=0.4 )
sns.histplot(res_vax, kde=True, alpha=0.60, label="ottobre-dicembre 2021")
sns.histplot(res_vaxparziali, kde=True, alpha=0.70, label="feb-mag 2021", color="indianred")
plt.legend()

np.corrcoef(df_nov_2021["nuovi_positivi"], df_nov_2021["var_tamponi"])
np.corrcoef(df_ott2020["nuovi_positivi"], df_ott2020["var_tamponi"])
np.corrcoef(res, df_nov_2021["var_tamponi"])
np.corrcoef(res1, df_ott2020["var_tamponi"])

#ANALISI RESIDUI
plt.scatter(df_nov_2021["var_tamponi"], res_vax, alpha=0.5)
plt.axhline(y=0, linestyle= "--", color="black")
plt.title("Scatter residui modello ottobre-dicembre 2021")

plt.scatter(df_ott2020["var_tamponi"], res_novax, alpha=0.5)
plt.axhline(y=0, linestyle= "--", color="black")
plt.title("Scatter residui modello ottobre-dicembre 2020")

plt.scatter(df_feb2021["var_tamponi"], res_vaxparziali, alpha=0.5)
plt.axhline(y=0, linestyle= "--", color="black")
plt.title("Scatter residui modello febbraio-maggio 2021")

##perform Bresuch-Pagan test ##sivax
names = ['Lagrange multiplier statistic', 'p-value',
        'f-value', 'f p-value']
test = sms.het_breuschpagan(results_sivax.resid, results_sivax.model.exog)

lzip(names, test)

##perform Bresuch-Pagan test ##vaxparziali ##non rifiuto omoschedasticità!
names = ['Lagrange multiplier statistic', 'p-value',
        'f-value', 'f p-value']
test_vaxparziali = sms.het_breuschpagan(mm.resid, mm.model.exog)

lzip(names, test_vaxparziali)


##############################################################################
##############################################################################
#GRAFICO SOLO OTTOBRE-DICEMBRE 2020-2021
##############################################################################
##############################################################################
ax = sns.regplot(x="var_tamponi", y="nuovi_positivi", data = df_ott2020 , scatter_kws={'alpha':0.5} ,
   line_kws = {
      'label': "y(slope)={0:.4f}x" "; R^2=0.734" "; std.err={4:2f}".format(slope, intercept, r_value, p_value, std_err)
   }, label="ottobre-dicembre 2020(NOVAX) ")
ax = sns.regplot(x="var_tamponi", y="nuovi_positivi", data=df_nov_2021, scatter_kws={'alpha':0.5} ,label="ottobre-dicembre 2021(SìVAX) ",
                 line_kws = {
                    'label': "y(slope)={0:.4f}x" "; R^2=0.494" "; std.err=0.013 ".format(slope2, intercept2, r_value2, p_value2, std_err2)
                 })

plt.legend()
plt.grid()
ax.set(xlabel="Tamponi Giornalieri", ylabel="Positivi Giornalieri")
plt.title("Regressione lineare tra Positivi Giornalieri e Tamponi Giornalieri")
#ax.set_xlabel ("giuseppecangemi", position=(0.,1e6),horizontalalignment="left" )
plt.gcf().text(0.06, 0.035, "@giuseppecangemi", fontsize=10)


##############################################################################
##############################################################################
#GRAFICO OTTOBRE-DICEMBRE 2020-2021 E FEBRAIO-MAGGIO 
##############################################################################
##############################################################################

ax = sns.regplot(x="var_tamponi", y="nuovi_positivi", data = df_ott2020 , scatter_kws={'alpha':0.5} ,
   line_kws = {
      'label': "y(slope)={0:.4f}x" "; R^2=0.734" "; std.err={4:2f}".format(slope, intercept, r_value, p_value, std_err)
   }, label="ottobre-dicembre 2020(NOVAX) ")
ax = sns.regplot(x="var_tamponi", y="nuovi_positivi", data=df_nov_2021, scatter_kws={'alpha':0.5} ,label="ottobre-dicembre 2021(SìVAX) ",
                 line_kws = {
                    'label': "y(slope)={0:.4f}x" "; R^2=0.393" "; std.err=0.004 ".format(slope2, intercept2, r_value2, p_value2, std_err2)
                 })
ax = sns.regplot(df_feb2021["var_tamponi"], df_feb2021["nuovi_positivi"], scatter_kws={'alpha':0.5} ,label="febbraio-aprile 2021 (vax parziali)",
                 line_kws = {
                    'label': "y(slope)={0:.4f}x" "; R^2=0.624" "; std.err=0.005 ".format(slope3, intercept3, r_value3, p_value3, std_err3)
                 }, color="indianred")
plt.legend()
plt.grid()
ax.set(xlabel="Tamponi Giornalieri", ylabel="Positivi Giornalieri")
plt.title("Regressione lineare tra Positivi Giornalieri e Tamponi Giornalieri")
#ax.set_xlabel ("giuseppecangemi", position=(0.,1e6),horizontalalignment="left" )
plt.gcf().text(0.06, 0.035, "@giuseppecangemi", fontsize=10)

##############################################################################
##############################################################################

#NO CORR durante prima ondata!!!!
dfff = df[["nuovi_positivi", "var_tamponi"]].iloc[1:97]

sns.regplot(dfff["var_tamponi"], dfff["nuovi_positivi"])

xp = dfff["var_tamponi"]
xp = sm.add_constant(xp)
m = sm.OLS(dfff["nuovi_positivi"], xp).fit()
print(m.summary())


#Regressione 27 paesi fully vacc/death pop


a = pd.read_excel("/Users/giuseppecangemi/Desktop/Covid19_Sicily_ITA STATA/correlation_vaccination_death.xlsx")

slope, intercept, r_value, p_value, std_err = stats.linregress(a["fully"], a["formln_ott"])
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(a["at_least"], a["formln_ott"])

#da ottobre con DUE dosi
ax = sns.regplot(x="fully", y="formln_ott", data = a ,
                 line_kws = {
                    'label': "y={1:.2f} {0:.2f}x \
                    " 
                    "R^2={2:.4f}" 
                    "; std.err=8.213(adj)".format(slope, intercept, r_value, p_value, std_err)
                 })
plt.legend()
plt.grid()
plt.title("Correlazione tra popolazione totalmente vaccinata e morti per milione da Ottobre")
for i in range(a.shape[0]):
 plt.text(x=a.fully[i],y=a.formln_ott[i],s=a.Country[i])
ax.set(xlabel="% doppia dose", ylabel="morti per milione")
plt.gcf().text(0.06, 0.035, "@giuseppecangemi", fontsize=10)

##################
##################
#da ottobre con UNA dose!!!!
ax = sns.regplot(x="at_least", y="formln_ott", data = a ,
                 line_kws = {
                    'label': "y={1:.2f} {0:.2f}x \
                    " 
                    "R^2={2:.4f}" 
                    "; std.err=6.777(adj)".format(slope1, intercept1, r_value1, p_value1, std_err1)
                 })
plt.legend()
plt.grid()
plt.title("Correlazione tra popolazione totalmente vaccinata e morti per milione da Ottobre")
for i in range(a.shape[0]):
 plt.text(x=a.at_least[i],y=a.formln_ott[i],s=a.Country[i])
ax.set(xlabel="% Almeno una dose", ylabel="morti per milione")
plt.gcf().text(0.06, 0.035, "@giuseppecangemi", fontsize=10)


x = a["fully"]
x = sm.add_constant(x)
model = sm.OLS(a["formln_ott"], x).fit()
print(model.summary())
res = model.resid

sns.histplot(res, kde=True, bins=10)

sns.scatterplot(a["formln"],res)  #eterosk

names = ['Lagrange multiplier statistic', 'p-value',
        'f-value', 'f p-value']
test_vaxparziali = sms.het_breuschpagan(model.resid, model.model.exog)

lzip(names, test_vaxparziali)
###########################
###########################

x = a["fully"]
x = sm.add_constant(x)
model = sm.OLS(a["formln_ott"], x)
results = model.fit(cov_type='HAC',cov_kwds={'maxlags':1})
print(results.summary())

###########################
###########################
x = a["at_least"]
x = sm.add_constant(x)
model = sm.OLS(a["formln_ott"], x).fit()
results = model.fit
print(model.summary())
resss = model.resid
sns.distplot(resss)
sns.scatterplot(a["formln_ott"], resss) #eterosk then:
    
### W/HETEROSKEDASTICITY    
x = a["at_least"]
x = sm.add_constant(x)
model = sm.OLS(a["formln_ott"], x).fit(cov_type='HAC',cov_kwds={'maxlags':1})  
print(model.summary())  


ln_x = np.log(a["fully"])
ln_y = np.log(a["death_pop"])

x1 = ln_x
x1 = sm.add_constant(x1)
mod1 = sm.OLS(ln_y, x1).fit()
print(mod1.summary())


mod1 = sm.OLS(ln_y, x).fit()
print(mod1.summary())
r = mod1.resid

sns.histplot(r, kde=True)

ax = sns.regplot(a["fully"], y=ln_y)

