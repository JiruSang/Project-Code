

install.packages("lda")
install.packages("LDAvis")
install.packages("servr")


setwd("C:\\Users\\sony\\Desktop\\LDA separate")


Q1<- readLines("all_Q4.txt") # data for Q1

Q1<-strsplit(Q1," ")




list_Q1 <- as.list(Q1) #convert to list


doc.listQ1 <- strsplit(as.character(Q1),split=" ") #words vector 


tableQ1 <- table(unlist(doc.listQ1)) #count frequence£» factor 


tableQ1 <- sort(tableQ1, decreasing = TRUE) #sorting based on frequence


vocabQ1 <- names(tableQ1) #vocabulary


get.termsQ1 <- function(x) {
  
  index <- match(x, vocabQ1) # ID
  
  index <- index[!is.na(index)] 
  
  rbind(as.integer(index - 1), as.integer(rep(1, length(index)))) } 
 


doc_Q1 <- lapply(doc.listQ1, get.termsQ1)



K <- 5 #number of topic 

G <- 1000 #literation

alpha <- 0.10

eta <- 0.02

library(lda) 

set.seed(357)

fitQ1 <- lda.collapsed.gibbs.sampler(documents = doc_Q1, K = K, vocab = vocabQ1, num.iterations = G, alpha = alpha, eta = eta, initial = NULL, burnin = 0, compute.log.likelihood = TRUE)


thetaQ1 <- t(apply(fitQ1$document_sums + alpha, 2, function(x) x/sum(x))) #documents¡ªtopic matrix
 

phiQ1 <- t(apply(t(fitQ1$topics) + eta, 2, function(x) x/sum(x))) #topic-words matrix


term.frequencyQ1 <- as.integer(tableQ1) #frequence


doc.lengthQ1 <- sapply(doc_Q1, function(x) sum(x[2, ])) #length of documents


library(LDAvis)
library(servr)

jsonQ1 <- createJSON(phi = phiQ1, theta = thetaQ1,
                     
                     doc.length = doc.lengthQ1, vocab = vocabQ1,
                     
                     term.frequency = term.frequencyQ1)#drawing

serVis(jsonQ1, out.dir = "C:\\Users\\sony\\Desktop\\Q4", open.browser = FALSE)









