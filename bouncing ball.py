def bouncingBall(h, bounce, window):
    if h>0 and 0<bounce<1 and window<h:
        counter=0
        while h>window:
            counter+=2
            h*=bounce
    return counter-1



print(bouncingBall(3, 0.66, 1.5))