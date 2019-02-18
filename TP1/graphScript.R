library(readr)
library(ggplot2)

#get the file and convert result in number
results<-read_csv("resultatFormates.csv")
results$TempsMoyen=as.numeric(results$temps)
results$taille=as.numeric(results$taille)

#Create graph for each algo with each test

### COUNTING SORT ###
counting_sort<-subset(results, algo == "counting")
series=1:3
for (i in series){ 
  temp <- counting_sort[counting_sort$serie==series[i],]
  if(is.data.frame(temp) && nrow(temp)!=0){
    titre=paste("Counting - Test constantes - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    lm = lm(TempsMoyen ~ taille, data=temp)
    with(temp, plot(taille, TempsMoyen))
    abline(lm, col="blue")
    text(0,0, coef(lm)[2], col = "blue", pos=4, offset=2)
    title(main = titre)
    dev.off()
    
    titre=paste("Counting - Test puissance - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(taille, TempsMoyen),log="xy")
    title(main = titre)
    dev.off()
    
    titre= paste("Counting - Test rapport - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(taille, TempsMoyen/taille))
    title(main = titre)
    dev.off()
  }
}

### QUICK SORT ###
quicksort_fp<-subset(results, algo == "quick")
series=1:3
for (i in 1:3){ 
  temp <- quicksort_fp[quicksort_fp$serie==series[i],]
  if(is.data.frame(temp) && nrow(temp)!=0){
    titre=paste("Quicksort - Test constantes meilleur cas-cas moyen - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    lm = lm(TempsMoyen ~ I(taille*log(taille)), data=temp)
    with(temp, plot(taille*log(taille), TempsMoyen))
    abline(lm, col="blue")
    text(0,0, coef(lm)[2], col = "blue", pos=4, offset=2)
    title(main = titre)
    dev.off()
    
    titre=paste("Quicksort - Test constantes pire cas - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    lm = lm(TempsMoyen ~ I(taille^2), data=temp)
    with(temp, plot(taille^2, TempsMoyen))
    abline(lm, col="blue")
    text(0,0, coef(lm)[2], col = "blue", pos=4, offset=2)
    title(main = titre)
    dev.off()
    
    titre=paste("Quicksort - Test puissance - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(taille, TempsMoyen,log="xy"))
    title(main = titre)
    dev.off()
    
    titre= paste("Quicksort - Test rapport meilleur cas-cas moyen - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(taille, TempsMoyen/(taille*log(taille))))
    title(main = titre)
    dev.off()
    
    titre= paste("Quicksort - Test rapport pire cas - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(taille, TempsMoyen/(taille^2)))
    title(main = titre)
    dev.off()    
  }
}

### QUICK SEUIL ###
quicksort_fp_t<-subset(results, algo == "quickSeuil")
series=1:3
for (i in series){ 
  temp <- quicksort_fp_t[quicksort_fp_t$serie==series[i],]
  if(is.data.frame(temp) && nrow(temp)!=0){
    titre=paste("Quicksort  seuil - Test constantes meilleur cas-cas moyen - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    lm = lm(TempsMoyen ~ I(taille*log(taille)), data=temp)
    with(temp, plot(taille*log(taille), TempsMoyen))
    abline(lm, col="blue")
    text(0,0, coef(lm)[2], col = "blue", pos=4, offset=2)
    title(main = titre)
    dev.off()
    
    titre=paste("Quicksort seuil - Test constantes pire cas - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    lm = lm(TempsMoyen ~ I(taille^2), data=temp)
    with(temp, plot(taille^2, TempsMoyen))
    abline(lm, col="blue")
    text(0,0, coef(lm)[2], col = "blue", pos=4, offset=2)
    title(main = titre)
    dev.off()
    
    titre=paste("Quicksort seuil - Test puissance - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(taille, TempsMoyen,log="xy"))
    title(main = titre)
    dev.off()
    
    titre= paste("Quicksort seuil - Test rapport meilleur cas-cas moyen - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(taille, TempsMoyen/(taille*log(taille))))
    title(main = titre)
    dev.off()
    
    titre= paste("Quicksort  seuil - Test rapport pire cas - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(taille, TempsMoyen/(taille^2)))
    title(main = titre)
    dev.off()    
  }
}

### QUICK RANDOM SEUIL ###
quicksort_rp<-subset(results, algo == "quickRandomSeuil")
series=1:3
for (i in series){ 
  temp <- quicksort_rp[quicksort_rp$serie==series[i],]
  if(is.data.frame(temp) && nrow(temp)!=0){
    titre=paste("quickRandomSeuil- Test constantes meilleur cas-cas moyen - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    lm = lm(TempsMoyen ~ I(taille*log(taille)), data=temp)
    with(temp, plot(taille*log(taille), TempsMoyen))
    abline(lm, col="blue")
    text(0,0, coef(lm)[2], col = "blue", pos=4, offset=2)
    title(main = titre)
    dev.off()
    
    titre=paste("quickRandomSeuil - Test constantes pire cas - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    lm = lm(TempsMoyen ~ I(taille^2), data=temp)
    with(temp, plot(taille^2, TempsMoyen))
    abline(lm, col="blue")
    text(0,0, coef(lm)[2], col = "blue", pos=4, offset=2)
    title(main = titre)
    dev.off()
    
    titre=paste("quickRandomSeuil - Test puissance - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(taille, TempsMoyen,log="xy"))
    title(main = titre)
    dev.off()
    
    titre= paste("quickRandomSeuil - Test rapport meilleur cas-cas moyen - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(taille, TempsMoyen/(taille*log(taille))))
    title(main = titre)
    dev.off()
    
    titre= paste("quickRandomSeuil - Test rapport pire cas - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(taille, TempsMoyen/(taille^2)))
    title(main = titre)
    dev.off()   
  }
}

