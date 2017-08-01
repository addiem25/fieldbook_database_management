# Set working directory
setwd("C:/Users/thomp464/Downloads/ExperimentPulling/ExperimentPulling")
dir.create("./tableFormat",showWarnings=F)

# Find file names
filenames<-list.files(pattern="*.csv")
for (filex in filenames){

  # Import data
  data<-read.delim(file=filex,header=T,sep=",")
  if(dim(data)[1]==0) {
      next
    }

  # Only keep unique plot_ids
  dataUnique<-data.frame(unique(data[,1]))
  colnames(dataUnique)<-"rid"

  # Split based on trait (splits to list)
  dataSplit<-split(data,data$parent)

  # Add traits/data as columns
  for (i in 1:length(dataSplit)) {
    temp<-dataSplit[[i]]
    temp<-data.frame(temp$rid,temp$parent,temp$userValue)
    colnames(temp)<-c("rid","parent","userValue")
    if(dim(temp)[1]==0) {
      next
    }
    traitName<-temp$parent[1]
    temp<-temp[,-2]
    temp<-aggregate(as.numeric(temp[,2],stringsAsFactors=F),
                    by=list(temp[,1]),mean)
    colnames(temp)<-c("rid", as.character(traitName))                  
    dataUnique<-merge(dataUnique,temp,by="rid",all=TRUE)
  }

  # Write data
  write.csv(dataUnique,file=paste("./tableFormat/",filex,"_tableFormat.csv",sep=""),row.names=FALSE)

}
