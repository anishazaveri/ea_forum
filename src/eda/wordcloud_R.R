library(wordcloud)
library(extrafont)
loadfonts(device = "win")

tdm <- read.csv('../../data/eaforum_scc_BOW.csv', row.names=1)

par(mfrow=c(1,1))
png(filename="../../wordclouds/eaforum_ssc_comparative.png", width=12,height=8, units='in', res=300)
comparison.cloud(tdm, colors = c("#E41A1C","#377EB8"),
                 title.size=1, max.words=400, family="Gill Sans MT", font=1)
dev.off()


pdf(file="../../wordclouds/eaforum_ssc_commonality.pdf")
commonality.cloud(tdm, random.order=FALSE,  colors = brewer.pal(4, "Set1"), max.words=400, family="Gill Sans MT", font=1)
dev.off()

