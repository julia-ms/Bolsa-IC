# downloading imbcol
if (!require("devtools")) {
  install.packages("devtools")
}
devtools::install_github("victorhb/ImbCoL")
library("ImbCoL")

# install read xlsx
install.packages("readxl")
library("readxl")

# reading datasets
filePath <- "datasets/hispanicMaleUnst.xlsx"
dataset <- read_excel(filePath)
fileName <- basename(filePath)
numRows <- nrow(dataset)
num0 <- sum(dataset[, 1] == 0)
num1 <- sum(dataset[, 1] == 1)

sink(file = "output.txt")
print(fileName)
print(numRows)
print(num0)
print(num1)
ImbCoL::complexity(Diagnosis ~ ., dataset)
sink(file = NULL)

