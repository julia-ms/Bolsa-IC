# testing ImbCoL library

# downloading imbcol
if (!require("devtools")) {
  install.packages("devtools")
}
devtools::install_github("victorhb/ImbCoL")
library("ImbCoL")

# flower species dataset

ImbCoL::complexity(Species ~ ., iris)

ImbCoL::overlapping(Species ~ ., iris)

# package to read .arff 
install.packages('RWeka')
library(RWeka)

# datasets for tests
dataset = read.arff('Australian.arff')
#dataset = read.arff('CastMetal1.arff')
#dataset = read.arff('CostaMadre1.arff')
#dataset = read.arff('KungChi3.arff')
#dataset = read.arff('KnuggetChase3.arff')

ImbCoL::complexity(class ~ ., dataset)

