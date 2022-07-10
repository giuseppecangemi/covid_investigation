library(ggplot2)
library(devtools)
library(broom)
library(arm)
library(gvlma)
library(readxl)
library(reshape2)
library(tidyverse)
library(zoo)
library(RColorBrewer)


d <- read_excel("/Users/giuseppecangemi/Desktop/Covid19_ITA/Covi19_Italy.xlsx")
View(d)

ggplot(data=d, aes(x=t, y=nuovi_positivi)) + geom_line() + geom_point()

d1 <- d %>%
  filter(t>= 647) #from december 2021
view(d1)

lag_pos <- lag(d1$nuovi_positivi, 7)
#view(lag_pos)

d1$pos <- d1$nuovi_positivi - lag_pos
#view(pos)

d1$ma <- rollmean(d1$pos, k=7, fill=NA)
#view(d1$ma)

d1$lin_lag <- lag(d1$nuovi_positivi, 7)
d1$div <- d1$nuovi_positivi/d1$lin_lag
d1$div_ma <- rollmean(d1$div, k=7, fill=NA)

plot(d1$t, d1$div, log="y", main = "Tasso Settimanale dei casi positivi \
rispetto settimana precedente", ylab="Delta Positivi", xlab="Giorni (da dicembre 2021 ad oggi)", 
     col="black", pch=21)+ abline(h=1, lty=2) + abline(h=1.3962460, col="blue", lty=2) +
      lines(d1$t, d1$div_ma, col="red",lwd=1.5) + text(770, 1.8, "media mobile sulla linea blu:\
        tempo di raddoppio 2.1 settimane") +
          mtext("Kangemi_Edu", side=1, line=3.5, at=500) + grid() + 
            scale_y_continuous(breaks = seq(0, 1000, by=100),  limits=c(0,1000)) 
