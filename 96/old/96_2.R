rm(list = ls())

library(ggplot2)
library(tidyverse)

set.seed(1)
`%notin%` = Negate(`%in%`)

# download.file("https://projecteuler.net/project/resources/p096_sudoku.txt",
#              "number_96.txt")

# read in data into list of 50 matrices
dat <- matrix(readLines("number_96.txt", warn = F), ncol = 10, byrow = T)
sudoku <- strsplit(apply(dat[,2:10], 1, paste0, collapse = ""), split = "")
for (each in 1:50){
  sudoku[[each]] <- t(matrix(as.numeric(sudoku[[each]]), nrow = 9, ncol = 9))
}

# function to return possible numbers for a given cell for a given board and coords
possible_numbers <- function(sdk, i, x, y){
  if (sdk[[i]][x,y] == 0){
    horz <- sdk[[i]][x,]
    vert <- sdk[[i]][,y]
    TbyT <- sdk[[i]][trunc((x-1e-4)/3)*3+1:3,
                     trunc((y-1e-4)/3)*3+1:3]
    winners <- c(1:9)[1:9 %notin% c(vert, horz, TbyT)]
    
    if (winners == ""){
      print('ya fucked up')
    }
    
    if (length(winners)==1){
      return(paste0(winners))
    } else {
      return(paste0(sample(winners), collapse = ""))
    }
  } else {
    return(sdk[[i]][x,y])
  }
}

# initialize possible numbers
sudoku_possible <- sudoku
for (i in 1:50){
  for (x in 1:9){
    for (y in 1:9){
      sudoku_possible[[i]][x,y] <- possible_numbers(sudoku, i, x, y)
    }
  }
}

