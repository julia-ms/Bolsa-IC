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

#read xls
install.packages("readxl")
library(readxl)
#dataset = read_excel('datasets/all102.xlsx')
dataset = read_excel('datasets/intersectional-bias3.xlsx')
dataset <- dataset[, -Race]

# datasets for tests
dataset2 = read.arff('datasets/Australian.arff')
#dataset = read.arff('datasets/CastMetal1.arff')
#dataset = read.arff('datasets/CostaMadre1.arff')
#dataset = read.arff('datasets/KungChi3.arff')
datasett = read.arff('datasets/KnuggetChase3.arff')

ImbCoL::complexity(Race ~ ., dataset)
