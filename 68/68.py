# magic 5gon
# outer ring starts with the smallest value
# so to max we would have 6, 7, 8, 9, 10 in the outer nodes
# starting with 6.
# that leaves 5,4,3,2,1 on the inner nodes.
# 6+7+8+9+10 + 2*(1+2+3+4+5) = 70 / 5 = 14
# so max case starts with 6,5,3
# then that forces 10,3,1
# aiming for max, we would like 9,1,4 to follow
# then 8,4,2 then 7,2,5
# so the solution is 6,5,3: 10,3,1: 9,1,4: 8,4,2: 7,2,5
# lol, paper and pencil solution was easy, coding will be annoying
