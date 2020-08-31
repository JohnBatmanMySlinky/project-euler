rm(list = ls())

#https://en.wikipedia.org/wiki/Barycentric_coordinate_system

download.file("https://projecteuler.net/project/resources/p102_triangles.txt",
             "number_102.txt")
df <- read.delim("number_102.txt", sep = ",", header = F)
df[,'x'] <- 0
df[,'y'] <- 0
colnames(df) <- c('x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x', 'y')

df$a = ((df$y2 - df$y3)*(df$x - df$x3) + (df$x3 - df$x2)*(df$y - df$y3)) / ((df$y2 - df$y3)*(df$x1 - df$x3) + (df$x3 - df$x2)*(df$y1 - df$y3))
df$b = ((df$y3 - df$y1)*(df$x - df$x3) + (df$x1 - df$x3)*(df$y - df$y3)) / ((df$y2 - df$y3)*(df$x1 - df$x3) + (df$x3 - df$x2)*(df$y1 - df$y3))
df$c = 1 - df$a - df$b
df$answers <- 1*(df$a >0)*(df$b>0)*(df$c>0)
sum(df$answers)
