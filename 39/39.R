# p is perimeter of a right triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120
# 
# {20, 48, 52}, {24, 45, 51}, {30, 40, 50}
# 
# for which value of p <= 1000 is the number of solutions maximized

# P = a + b + c
# a^2 + b^2 = c^2

# a < P/3
# substitute gives me (p^2-2pa)/(2p-2a) = b so b must be integer
ptm <- proc.time()

P <- 1000
answers <- matrix(0,P,1)
for (p in 1:P){ # loop thru p's
  for (a in 1:(p/3)){ # we know a < p/3 so loop a
    if(a!=p){ # so no div/0
      if(((p^2-2*p*a) / (2*p-2*a)) %% 2 == 0){ # if b is integer, we have a winner
        answers[p] <- answers[p] + 1 # count winners for each p
      } 
    }
  }
}
which(answers == max(answers),answers) # which p gives us max answers

proc.time() - ptm
      