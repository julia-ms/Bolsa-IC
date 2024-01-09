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
#dataset = read.arff('datasets/Australian.arff')
#dataset = read.arff('datasets/CastMetal1.arff')
#dataset = read.arff('datasets/CostaMadre1.arff')
#dataset = read.arff('datasets/KungChi3.arff')
dataset = read.arff('datasets/KnuggetChase3.arff')

ImbCoL::overlapping(class ~ ., dataset)

