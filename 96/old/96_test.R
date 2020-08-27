###################################################
###################################################
test <- sudoku_possible[[6]]

guess_filter <- nchar(test)>1
test[guess_filter]

for (outer in 1:length(test[guess_filter])){
  big_grid <- list()
  for (each in 1:length(test[guess_filter][1:outer])){
    big_grid[[each]] <- strsplit(test[guess_filter][each]   ,"")[[1]]
  }
  
  big_grid <- expand.grid(big_grid)
  print(apply())
  print(big_grid)
  browser()
}