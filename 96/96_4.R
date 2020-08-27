rm(list = ls())
ptm <- proc.time()

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

update_board <- function(sdk, i, x, y){
  z <- sdk[[i]][x,y]
  x_idx <- c(1:9)[1:9 %notin% x]
  y_idx <- c(1:9)[1:9 %notin% y]
  TbyT_x <- trunc((x-.5)/3)*3+1:3
  TbyT_y <- trunc((y-.5)/3)*3+1:3
  
  if (nchar(z)==1){
    # update x to remove any z's
    for (a in x_idx){
      old <- strsplit(sdk[[i]][a,y],"")[[1]]
      new <- old[old %notin% z]
      sdk[[i]][a,y] <- paste0(new, collapse = "")
    }
    # update y to remove any z's
    for (a in y_idx){
      old <- strsplit(sdk[[i]][x,a],"")[[1]]
      new <- old[old %notin% z]
      sdk[[i]][x,a] <- paste0(new, collapse = "")
    }
    # update TbyT to remove any z's
    for (a in TbyT_x){
      for (b in TbyT_y){
        if(!(a == x & b == y)){
          old <- strsplit(sdk[[i]][a,b],"")[[1]]
          new <- old[old %notin% z]
          sdk[[i]][a,b] <- paste0(new, collapse = "")
        }
      }
    }
  }
  return(sdk[[i]])
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

lookup_matrix <- matrix(apply(expand.grid(1:9,1:9),1,paste,collapse = ""), nrow = 9, ncol = 9)

# for boards not solved, time to start guessing!
for (i in 1:50){
  stop <-  FALSE
  guess_number <- 0
  if(sum(nchar(sudoku_possible[[i]])==1)<81){
    # this builds the board of guesses to run through
    guess_filter <- nchar(sudoku_possible[[i]])>1
    for (outer in 1:length(sudoku_possible[[i]][guess_filter])){
      big_grid <- list()
      for (inner in 1:length(sudoku_possible[[i]][guess_filter][1:outer])){
        big_grid[[inner]] <- strsplit(sudoku_possible[[i]][guess_filter][inner]   ,"")[[1]]
      }
    big_grid <- expand.grid(big_grid)
  
    
    # load results into sudoku_possible_guess and run easy_answers and check if it works
    for (n in 1:nrow(big_grid)){
      sudoku_possible_guess <- sudoku_possible
      sudoku_output_guess <- sudoku_output
      guess_number <- guess_number + 1
      for (c in 1:ncol(big_grid)){
        sudoku_possible_guess[[i]][guess_filter][c] <- as.character(big_grid[n,c])
        
        ##################
        ###Update Board###
        ##################
        x_tmp <- as.numeric(strsplit(lookup_matrix[guess_filter][c], "")[[1]][1])
        y_tmp <- as.numeric(strsplit(lookup_matrix[guess_filter][c], "")[[1]][2])
        sudoku_possible_guess[[i]] <- update_board(sudoku_possible_guess, i, x_tmp, y_tmp)
        if(sum(sudoku_possible_guess[[i]]=="")>0){
          break
        }
      }
      guess_results <- easy_answers(sudoku_output_guess,
                                    sudoku_possible_guess,
                                    i)
      
      if(sum(nchar(guess_results[[2]])==1)==81){
        #browser()
        
        stop <-  TRUE
        sudoku_possible[[i]] <- guess_results[[2]]
        sudoku_output[[i]] <- guess_results[[1]]
        print(paste("Board: ", i,"Guess Number: ", guess_number))
        break
      }
    }
    if(stop){break}
    }
  }
}

euler <- 0
for (each in sudoku_output){
  euler <- euler + as.numeric(paste0(each[1,1],each[1,2],each[1,3], collapse = ""))
}
euler
proc.time()-ptm