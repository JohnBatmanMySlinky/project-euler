fn <- function(x){
  return(1 - x + x^2 - x^3 + x^4 - x^5 + x^6 - x^7 + x^8 - x^9 + x^10)
  #return(x^3)
}
generating_function <- function(x){
  return(data.frame(x = x,y = fn(x)))
}
OP <- function(df,x,y,k){
  if(k>0){
    # build a model matrix
    vars <- paste('x',1:k, sep = "")
    for (i in 1:k){
      df[,paste('x',i, sep = "")] <- df[,x]^i
    }
    
    # do OLS
    X <- as.matrix(cbind(1,df[1:(k+1),vars]))
    Y <- as.matrix(df[1:(k+1),y])
    Beta <- solve(t(X) %*% X) %*% t(X) %*% Y 
    
    #predict
    return(as.numeric(as.matrix(cbind(1,df[(k+2),vars])) %*% Beta))
  } else (return(as.numeric(df[1,'x'])))
}

# OP is faster than lm()
# system.time(replicate(10000, lm(y~x+I(x^2)+I(x^3), data = input)))
# system.time(replicate(10000, OLS(input,'x','y',3)))

#my indexing is off by -1 from projecteuler's.....
#i get some divergence in answers above k == 7, too lazy to fix
# K <- 9
# for (k in 0:K-1){
#   print(k)
#   print(OP(generating_function(1:10), 'x', 'y', k))
# }


# Ima use lm() cause im getting some matrix erros
answers <- matrix(0,9,1)
for (k in 1:9){
  formula <- "y~1+"
  for (i in 1:k){
    if(i != k){
      formula <- paste(formula,"I(x^",i,")+",sep = "")
    } else{
      formula <- paste(formula,"I(x^",i,")", sep = "")
    }
  }
  answers[k] <- as.numeric(predict(lm(as.formula(formula), 
                                      data = generating_function(1:(k+1))),
                                   newdata = generating_function(k+2)))
}

sum(answers)+1



