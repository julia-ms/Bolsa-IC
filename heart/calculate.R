# downloading imbcol
if (!require("devtools")) {
  install.packages("devtools")
}
devtools::install_github("victorhb/ImbCoL")
library("ImbCoL")

# reading datasets
filePath <- "datasets/female.csv"
dataset <- read.csv(filePath)
fileName <- basename(filePath)
numRows <- nrow(dataset)
num0 <- sum(dataset$target == 0)
num1 <- sum(dataset$target == 1)

sink(file = "output.txt")
print(fileName)
print(numRows)
print(num0)
print(num1)
ImbCoL::complexity(target ~ ., dataset)
sink(file = NULL)

