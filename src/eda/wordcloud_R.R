library(readr)
library(tm)
library(dplyr)
library(xtable)

ssc <- read_file("../../data/ssc/ssc_for_Rwordcloud.txt")
eaf <- read_file("../../data/ea_forum/eaforum_for_Rwordcloud.txt")

docs <- Corpus(VectorSource(sotu$speechtext)) %>%
  tm_map(removePunctuation) %>%
  tm_map(removeNumbers) %>%
  tm_map(tolower)  %>%
  tm_map(removeWords, stopwords("english")) %>%
  tm_map(stripWhitespace) %>%
  tm_map(PlainTextDocument)

tdm <- TermDocumentMatrix(docs) %>%
  as.matrix()
colnames(tdm) <- c("Bush","Obama")
