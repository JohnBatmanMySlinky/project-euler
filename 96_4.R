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
    
    if (length(winners)==1){
      return(paste0(winners))
    } else {
      return(paste0(sample(winners), collapse = ""))
    }
  } else {
    return(sdk[[i]][x,y])
  }
}

unique_solution <- function(sdk,i,x,y){
  if (nchar(sdk[[i]][x,y])>1){
    z <- strsplit(sdk[[i]][x,y],"")[[1]]
    
    x_possible <- sdk[[i]][x,-y]
    x_possible <- paste0(x_possible,collapse = "")
    x_possible <- strsplit(x_possible,"")[[1]]
    
    y_possible <- sdk[[i]][-x,y]
    y_possible <- paste0(y_possible,collapse = "")
    y_possible <- strsplit(y_possible,"")[[1]]
    
    x_index <- trunc((x-.5)/3)*3+1:3
    y_index <- trunc((y-.5)/3)*3+1:3
    
    TbyT_x <- sdk[[i]][x_index,
                       y_index[y_index != y]]
    TbyT_y <- sdk[[i]][x_index[x_index != x],
                       y_index]
    TbyT <- paste0(TbyT_x, TbyT_y, collapse = "")
    TbyT <- strsplit(TbyT, "")[[1]]
    
    z <- z[z %notin% x_possible | z %notin% y_possible | z %notin% TbyT]
    z <- paste0(z,collapse = "")
    
    if(nchar(z)==0){
      return(sdk[[i]][x,y])
    } else{
      return(z)
    }
  } else {
    return(sdk[[i]][x,y])
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
        sdk_possible[[i]][x,y] <- unique_solution(sdk_possible, i, x, y)
      }
    }
    
    count_of_1s_post <- sum(nchar(sdk_possible[[i]])==1)
  }
  
  return(list(sdk_output[[i]],
              sdk_possible[[i]]))
}


# initialize possible numbers for each board
sudoku_possible <- sudoku
for (i in 1:50){
  for (x in 1:9){
    for (y in 1:9){
      sudoku_possible[[i]][x,y] <- possible_numbers(sudoku, i, x, y)
    }
  }
}



# Run easy answers once
sudoku_output <- sudoku
for (i in 1:50){
  easy_answers_results <- easy_answers(sudoku_output,
                                       sudoku_possible,
                                       i)
  sudoku_output[[i]] <- easy_answers_results[[1]]
  sudoku_possible[[i]] <- easy_answers_results[[2]]
  
  print(paste("Board: ", i,
              "Tiles: ", sum(nchar(sudoku_possible[[i]])==1)))
}


# for boards not solved, time to start guessing!
for (i in 6){
  
  # this builds the board of guesses to run through
  guess_filter <- nchar(sudoku_possible[[i]])>1
  for (outer in 1:length(sudoku_possible[[i]][guess_filter])){
    big_grid <- list()
    for (inner in 1:length(sudoku_possible[[i]][guess_filter][1:outer])){
      big_grid[[inner]] <- strsplit(sudoku_possible[[i]][guess_filter][inner]   ,"")[[1]]
    }
  big_grid <- expand.grid(big_grid)
  sudoku_possible_guess <- sudoku_possible
  sudoku_output_guess <- sudoku_possible
  
  # load results into sudoku_possible_guess and run easy_answers and check if it works
  for (n in 1:nrow(big_grid)){
    for (c in 1:ncol(big_grid)){
      sudoku_possible_guess[[i]][guess_filter][c] <- as.character(big_grid[n,c])
      ##################
      ###Update Board###
      ##################
      
      #################
      ###Check Board###
      #################
    }
    browser()
    guess_results <- easy_answers(sudoku_possible_guess,
                                  sudoku_output_guess,
                                  i)
    print(guess_results[[2]])
    if(sum(nchar(guess_results[[2]])==1)==81){
      print('holy shit it worked!')
    }
  }
  
  }
}
  
  # for each row and column load in big_grid into sudoku_possible_guess[[i]]


big_grid


