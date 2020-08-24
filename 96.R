rm(list = ls())

library(tidyverse)

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
    if (length(winners)==1){
      return(paste0(winners))
    } else {
      return(paste0(sample(winners), collapse = ""))
    }
  } else {
    return(sdk[[i]][x,y])
  }
}

#check if given board, cell are OK, return bool
unique_solution <- function(sdk, i, x, y){
  if (nchar(sdk[[i]][x,y])>1){
    #horizontal
    horz <- sdk[[i]][x,]
    horz <- horz[nchar(horz) > 1]
    horz <- unlist(strsplit(horz, ""))
    horz <- horz[!(duplicated(horz) | duplicated(horz, fromLast = TRUE))]

    #vertical
    vert <- sdk[[i]][,y]
    vert <- vert[nchar(vert) > 1]
    vert <- unlist(strsplit(vert, ""))
    vert <- vert[!(duplicated(vert) | duplicated(vert, fromLast = TRUE))]

    #three by three
    TbyT <- sdk[[i]][trunc((x-1e-4)/3)*3+1:3,
                     trunc((y-1e-4)/3)*3+1:3]
    TbyT <- TbyT[nchar(TbyT) > 1]
    TbyT <- unlist(strsplit(TbyT, ""))
    TbyT <- TbyT[!(duplicated(TbyT) | duplicated(TbyT, fromLast = TRUE))]

    # final check
    check <- unlist(strsplit(sdk[[i]][x,y],""))
    
    unq_sol <- paste0(check[check %in% c(TbyT, vert, horz)], collapse ="")
    
    if (nchar(unq_sol) == 0){
      return(sdk[[i]][x,y])
    } else {
      return(unq_sol)
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


# let the solve begin
sudoku_output <- sudoku
for (i in 1:50){
  # begin smart pre-processing
  count_of_1s_post <- 1
  count_of_1s_pre <- 0
  while (count_of_1s_post > count_of_1s_pre){
    count_of_1s_pre <- sum(nchar(sudoku_possible[[i]])==1)
    
    index_dumb <- nchar(sudoku_possible[[i]]) == 1
    sudoku_output[[i]][index_dumb] <- as.numeric(sudoku_possible[[i]][index_dumb])
    
    for (x in 1:9){
      for (y in 1:9){
        sudoku_possible[[i]][x,y] <- possible_numbers(sudoku_output, i, x, y)
      }
    } 
    count_of_1s_post <- sum(nchar(sudoku_possible[[i]])==1)
  }
  
  #after the while loop check for unique solutions
  for (x in 1:9){
    for (y in 1:9){
      sudoku_possible[[i]][x,y] <- unique_solution(sudoku_possible, i, x, y)
    }
  }
  
  # begin smart pre-processing
  count_of_1s_post <- 1
  count_of_1s_pre <- 0
  while (count_of_1s_post > count_of_1s_pre){
    count_of_1s_pre <- sum(nchar(sudoku_possible[[i]])==1)
    
    index_dumb <- nchar(sudoku_possible[[i]]) == 1
    sudoku_output[[i]][index_dumb] <- as.numeric(sudoku_possible[[i]][index_dumb])
    
    for (x in 1:9){
      for (y in 1:9){
        sudoku_possible[[i]][x,y] <- possible_numbers(sudoku_output, i, x, y)
      }
    } 
    count_of_1s_post <- sum(nchar(sudoku_possible[[i]])==1)
  }
  
  
  print(paste0("Pre-Brute Round: ", i," Completed Tiles:",sum(nchar(sudoku_possible[[i]])==1)))
  
  
  # begin brute force
}


sudoku_output[[1]]
