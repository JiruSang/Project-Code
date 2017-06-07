
install.packages("lda")
install.packages("LDAvis")
install.packages("servr")


setwd("C:\\Users\\sony\\Desktop\\LDA merge")


filename<-list.files()

zz<- sapply(filename,function(x) readLines(x) ) # merge data

zz<-unlist(zz)
Q<-strsplit(zz," ")


list_Q <- as.list(Q) #convert to list


doc.listQ <- strsplit(as.character(Q),split=" ") #words vector 


tableQ <- table(unlist(doc.listQ)) #count frequence£» factor 


tableQ <- sort(tableQ, decreasing = TRUE) #sorting based on frequence


vocabQ <- names(tableQ) #vocabulary

get.termsQ <- function(x) {
  
  index <- match(x, vocabQ) # ID
  
  index <- index[!is.na(index)] 
  
  rbind(as.integer(index - 1), as.integer(rep(1, length(index)))) } 

doc_Q <- lapply(doc.listQ, get.termsQ)


K <- 9 #number of topic 

G <- 2000 #literation

alpha <- 0.10

eta <- 0.02

library(lda) 

set.seed(357)

fitQ <- lda.collapsed.gibbs.sampler(documents = doc_Q, K = K, vocab = vocabQ, num.iterations = G, alpha = alpha, eta = eta, initial = NULL, burnin = 0, compute.log.likelihood = TRUE)

thetaQ <- t(apply(fitQ$document_sums + alpha, 2, function(x) x/sum(x))) #documents¡ªtopic matrix


phiQ <- t(apply(t(fitQ$topics) + eta, 2, function(x) x/sum(x))) #topic-words matrix

term.frequencyQ <- as.integer(tableQ) #frequence


doc.lengthQ <- sapply(doc_Q, function(x) sum(x[2, ])) #length of documents


library(LDAvis)
library(servr)

jsonQ <- createJSON(phi = phiQ, theta = thetaQ,
                     
                     doc.length = doc.lengthQ, vocab = vocabQ,
                     
                     term.frequency = term.frequencyQ)#drawing

serVis(jsonQ, out.dir = "C:\\Users\\sony\\Desktop\\Qall", open.browser = FALSE)








