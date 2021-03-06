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
    
    #if (i == 3 & x == 1 & y == 1){browser()}
    
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

easy_answers <- function(sdk_output, sdk_possible, i){
  count_of_1s_post <- 1
  count_of_1s_pre <- 0
  while (count_of_1s_post > count_of_1s_pre){
    count_of_1s_pre <- sum(nchar(sdk_possible[[i]])==1)
    
    index_dumb <- nchar(sdk_possible[[i]]) == 1
    sdk_output[[i]][index_dumb] <- as.numeric(sdk_possible[[i]][index_dumb])
    
    for (x in 1:9){
      for (y in 1:9){
        sdk_possible[[i]][x,y] <- possible_numbers(sdk_output, i, x, y)
      }
    } 
    count_of_1s_post <- sum(nchar(sdk_possible[[i]])==1)
  }
  
  return(list(sdk_output[[i]],
              sdk_possible[[i]]))
}


unique_solution <- function(sdk,i,x,y){
  z <- sdk[[i]][x,y]
  if (nchar(z)>1){
    x <- sdk[[i]][x,!y]
    x <- strsplit(x,"")[[1]]
    
    y <- sdk[[i]][y,!x]
    y <- strsplit(y,"")[[1]]
    
    x_index <- trunc((x-.5)/3)*3+1:3
    y_index <- trunc((y-.5)/3)*3+1:3
    TbyT <- sdk[[i]][]
  }
}


# let the solve begin
sudoku_output <- sudoku
for (i in 1:50){
  loop <- 0
  improve_pre <- 0
  improve_post <- 1
  while (sum(nchar(sudoku_possible[[i]])==1) < 81 & loop < 20){
    
    loop <- loop + 1
    
    # easy answer loop
    easy_answers_results <- easy_answers(sudoku_output,
                                         sudoku_possible,
                                         i)
    sudoku_output[[i]] <- easy_answers_results[[1]]
    sudoku_possible[[i]] <- easy_answers_results[[2]]
  }
print(paste("Board: ", i,
            "Tiles: ", sum(nchar(sudoku_possible[[i]])==1)))
}

sudoku_possible[[2]]
