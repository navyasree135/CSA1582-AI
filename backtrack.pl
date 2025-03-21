likes(john,pixxa).
likes(mary,toast).
likes(x,y):- likes(y,x), x\=y.
query(x,y):- likes(x,y).
