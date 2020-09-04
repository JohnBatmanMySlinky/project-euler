##### CONSTRAINTS #####
# a * b == c
# nchar(a) + nchar(b) + nchar(c) == 9

# solutions are going to exist in this space (i think.....)
# nchar(a) %in% c(1,2)
# nchar(b) %in% c(3,4)
# !(nchar(a) == 2 & nchar(b) == 2)
# nchar(c) == 4 becase if nchar(3) then nchar(a) == 3 and nchar(b) == 3 and 100*100=10000 which is more than 9 chars



winners <- data.frame(a = rep(0,10**5),
                      b = rep(0,10**5),
                      c = rep(0,10**5))
i <- 0
for (a in 1:98){
  for (b in 123:ceiling(9786/a)){
    
    c <- a * b
    combined <- paste0(a,b,c, sep = "")
    
    test_length <- nchar(combined) == 9
    test_pandigital <- length(unique(strsplit(combined,"")[[1]])) == 9
    test_0 <- !('0' %in% strsplit(combined,"")[[1]])
    
    if (test_length & test_pandigital & test_0){
      print(paste('yee haw #',i))
      i <- i + 1
      winners[i,'a'] <- a
      winners[i,'b'] <- b
      winners[i,'c'] <- c
    } else {}
  }
}

sum(unique(winners[,'c']))
