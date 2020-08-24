rm(list = ls())

`%notin%` = Negate(`%in%`)

# download.file("https://projecteuler.net/project/resources/p096_sudoku.txt",
#               "number_96.txt")

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

# check if given board, cell are OK, return bool
ok <- function(sdk, i, x, y){
  vert <- sdk[[i]][x,]
  horz <- sdk[[i]][,y]
  TbyT <- sdk[[i]][trunc((x-1e-4)/3)*3+1:3,trunc((y-1e-4)/3)*3+1:3]
  
  vert_test <- all(sort(vert) == 1:9)
  horz_test <- all(sort(horz) == 1:9)
  TbyT_test <- all(sort(TbyT) == 1:9)
  
  return(vert_test & horz_test & TbyT_test)
}
# an actually correct sudoku board
# sdk <- list(matrix(c(4,8,3,9,2,1,6,5,7,
#                      9,6,7,3,4,5,8,2,1,
#                      2,5,1,8,7,6,4,9,3,
#                      5,4,8,1,3,2,9,7,6,
#                      7,2,9,5,6,4,1,3,8,
#                      1,3,6,7,9,8,2,4,5,
#                      3,7,2,6,8,9,5,1,4,
#                      8,1,4,2,5,3,7,6,9,
#                      6,9,5,4,1,7,3,8,2), nrow = 9, ncol = 9))
# i <- 1; x <- 1; y <- 1


# fill sudoku_possible with possible numbers
sudoku_possible <- sudoku
for (i in 1:50){
  for (x in 1:9){
    for (y in 1:9){
      sudoku_possible[[i]][x,y] <- possible_numbers(sudoku, i, x, y)
    }
  }
}



# pick off easy answers
sudoku_output <- sudoku
for (i in 1:50){
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
  print(paste0("Pre-Brute Round: ", i," Completed Tiles:",count_of_1s_post))
}

