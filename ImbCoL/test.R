# testing ImbCoL library

# downloading imbcol
if (!require("devtools")) {
  install.packages("devtools")
}
devtools::install_github("victorhb/ImbCoL")
library("ImbCoL")

# package to read .arff 
install.packages('RWeka')
library(RWeka)

# dataset for tests
dataset = read.arff('Australian.arff')

ImbCoL::complexity(Species ~ ., iris)

ImbCoL::overlapping(Species ~ ., iris)
