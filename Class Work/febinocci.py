def febinocci(x):
    if x==0:
        return 0
    elif x==1:
        return 0
    elif x==2:
        return 1
    else:
        return febinocci(x-1)+febinocci(x-2)
    print(febinocci(10))