library(readr)
library(ggplot2)

#get the file and convert result in number
results<-read_csv("results.csv")
results$QuickSort=as.numeric(results$QuickSort)
result&CountingSort= as.numeric(result&CountingSort)
result&QuickSort_Rand_Pivot = as.numeric(results$QuickSort_Rand_Pivot)
result&QuickSort_Seuil_Exp =as.numeric(QuickSort_Seuil_Exp)
result&TempsMoyen = as.numeric(results$TempsMoyen) # a rajouter dans le excel

#Create graph for each algo with each test

### Counting sort ###
counting_sort<-subset(results, Taille == 1000)
series=1:3
for (i in series){ 
    #get time in coloumn counting sort and verify is not null
  temp <- counting_sort[counting_sort$Exemplaire_ID==series[i],]
  if(is.data.frame(temp) && nrow(temp)!=0){
    titre=paste("Counting sort- Test constantes - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    lm = lm(TempsMoyen ~ N, data=temp)
    with(temp, plot(N, TempsMoyen))
    abline(lm, col="blue")
    text(0,0, coef(lm)[2], col = "blue", pos=4, offset=2)
    title(main = titre)
    dev.off()

    titre=paste("Counting sort - Test puissance - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(N, TempsMoyen),log="xy")
    title(main = titre)
    dev.off()
    
    titre= paste("Counting sort - Test rapport - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(N, TempsMoyen/N))
    title(main = titre)
    dev.off()
  }
}

### QUICK SORT ###
quicksort_fp<-subset(results, Taille == 1000)
series=1:3
for (i in 1:3){ 
  temp <- QuickSort[QuickSort$serie==series[i],]
  if(is.data.frame(temp) && nrow(temp)!=0){
    titre=paste("QuickSort - Test constantes meilleur cas-cas moyen - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    lm = lm(TempsMoyen ~ I(N*log(N)), data=temp)
    with(temp, plot(N*log(N), TempsMoyen))
    abline(lm, col="blue")
    text(0,0, coef(lm)[2], col = "blue", pos=4, offset=2)
    title(main = titre)
    dev.off()
    
    titre=paste("QuickSort - Test constantes pire cas - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    lm = lm(TempsMoyen ~ I(N^2), data=temp)
    with(temp, plot(N^2, TempsMoyen))
    abline(lm, col="blue")
    text(0,0, coef(lm)[2], col = "blue", pos=4, offset=2)
    title(main = titre)
    dev.off()
    
    titre=paste("Quicksort - Test puissance - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(N, TempsMoyen,log="xy"))
    title(main = titre)
    dev.off()
    
    titre= paste("Quicksort - Test rapport meilleur cas-cas moyen - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(N, TempsMoyen/(N*log(N))))
    title(main = titre)
    dev.off()
    
    titre= paste("Quicksort - Test rapport pire cas - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(N, TempsMoyen/(N^2)))
    title(main = titre)
    dev.off()    
  }
}

### QuickSort_Seuil_Exp ###
quicksort_fp_t<-subset(results, Taille == 1000)
series=1:3
for (i in series){ 
  temp <- QuickSort_Seuil_Exp[QuickSort_Seuil_Exp$serie==series[i],]
  if(is.data.frame(temp) && nrow(temp)!=0){
    titre=paste("QuickSort_Seuil_Exp - Test constantes meilleur cas-cas moyen - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    lm = lm(TempsMoyen ~ I(N*log(N)), data=temp)
    with(temp, plot(N*log(N), TempsMoyen))
    abline(lm, col="blue")
    text(0,0, coef(lm)[2], col = "blue", pos=4, offset=2)
    title(main = titre)
    dev.off()
    
    titre=paste("QuickSort_Seuil_Exp - Test constantes pire cas - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    lm = lm(TempsMoyen ~ I(N^2), data=temp)
    with(temp, plot(N^2, TempsMoyen))
    abline(lm, col="blue")
    text(0,0, coef(lm)[2], col = "blue", pos=4, offset=2)
    title(main = titre)
    dev.off()
    
    titre=paste("QuickSort_Seuil_Exp - Test puissance - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(N, TempsMoyen,log="xy"))
    title(main = titre)
    dev.off()
    
    titre= paste("QuickSort_Seuil_Exp - Test rapport meilleur cas-cas moyen - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(N, TempsMoyen/(N*log(N))))
    title(main = titre)
    dev.off()
    
    titre= paste("QuickSort_Seuil_Exp - Test rapport pire cas - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(N, TempsMoyen/(N^2)))
    title(main = titre)
    dev.off()    
  }
}

### QuickSort_Rand_Pivot-Seuil_ExpP ###
quicksort_rp<-subset(results, Taille == 1000)
series=1:3
for (i in series){ 
  temp <- QuickSort_Rand_Pivot[QuickSort_Rand_Pivot$serie==series[i],]
  if(is.data.frame(temp) && nrow(temp)!=0){
    titre=paste("QuickSort_Rand_Pivot-Seuil_Exp - Test constantes meilleur cas-cas moyen - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    lm = lm(TempsMoyen ~ I(N*log(N)), data=temp)
    with(temp, plot(N*log(N), TempsMoyen))
    abline(lm, col="blue")
    text(0,0, coef(lm)[2], col = "blue", pos=4, offset=2)
    title(main = titre)
    dev.off()
    
    titre=paste("QuickSort_Rand_Pivot-Seuil_Exp - Test constantes pire cas - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    lm = lm(TempsMoyen ~ I(N^2), data=temp)
    with(temp, plot(N^2, TempsMoyen))
    abline(lm, col="blue")
    text(0,0, coef(lm)[2], col = "blue", pos=4, offset=2)
    title(main = titre)
    dev.off()
    
    titre=paste("QuickSort_Rand_Pivot-Seuil_Exp - Test puissance - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(N, TempsMoyen,log="xy"))
    title(main = titre)
    dev.off()
    
    titre= paste("QuickSort_Rand_Pivot-Seuil_Exp - Test rapport meilleur cas-cas moyen - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(N, TempsMoyen/(N*log(N))))
    title(main = titre)
    dev.off()
    
    titre= paste("QuickSort_Rand_Pivot-Seuil_Exp - Test rapport pire cas - S",i,sep='')
    jpeg(paste(getwd(),"/results/",titre,'.jpg',sep=''))
    with(temp, plot(N, TempsMoyen/(N^2)))
    title(main = titre)
    dev.off()   
  }
}

}