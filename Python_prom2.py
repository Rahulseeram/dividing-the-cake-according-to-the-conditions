N = int(input("Number of cuts: "))
Angle = list(map(int,input("Enter angles seperated by comma: ").split(",")))
def Divide_the_cake(N,Angle):
    k = []
    for i in Angle:
        if i not in k:
            k.append(i)
    l = k
    sum1 = sum(Angle)
    x = sum1
    # print(sum1)
# CASE 1 : CAKE SHOULD BE CUT INTO 'N' EQUAL PARTS.
# CASE 2 : CAKE SHOULD BE CUT INTO 'N' PARTS.
# CASE 3 : CAKE SHOULD BE CUT AND NO TWO CAKE SLICES ARE EQUAL.
    if N == len(Angle) and x==360:
        if len(l) == 1 and l[0] * 360 and len(Angle) == N:
            print("CASE 1 SATISFIED.")
        else:
            print("CASE 1 NOT SATISFIED.")
        if x == 360 and len(Angle) == N:
            print("CASE 2 SATISFIED.")
        else:
            print("CASE 2 NOT SATISFIED.")
        if k == Angle:
            print("CASE 3 SATISFIED.")
        else:
            print("CASE 3 NOT SATISFIED.")
    else:
        print("GIVE THE INPUT PROPERLY OR CHECK WEATHER THE SUM OF ANGLES IS 360.")
Divide_the_cake(N,Angle)