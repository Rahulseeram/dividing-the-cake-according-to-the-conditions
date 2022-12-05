class Inputs :
    N = int(input("NUMBER_OF _CUTS: "))
    A = input("ANGLES_IN_LIST: ")
    B = A.split(",")
    for i in range(0,len(B)):
        B[i] = int(B[i])
    def fun(self,N,B):
        self.N = N
        self.B = B
class CASE(Inputs) :
    def fun1(self):
        K = []
        for i in self.B:
            if i not in K:
                K.append(i)
        L = K  # STORING THE ANGLES WITHOUT REPETITON IN L VARIABLE
        M = 0  # M IS TAKEN TO FIND OUT THE SUM OF ALL ANGLES IN LIST
        for i in self.B :
            M = M + i
        X = M  # STORING THE SUM OF ALL ANGLES GIVEN IN THE LIST IS STORED IN X VARIABLE

        # CASE 1 : CAKE SHOULD BE CUT INTO " N " EQUAL PARTS

        # CASE 2 : CAKE SHOULD BE CUT INTO " N " PARTS

        # CASE 3 : CAKE SHOULD BE CUT AND NO TWO CAKE SLICES ARE EQUAL

        if self.N == len(self.B) and M == 360:
            if len(L) == 1 and L[0] * self.N == 360 and len(self.B) == self.N:  # FIRST CASE VERIFICATION
                print("FIRST CASE SATISFIED")
            else:
                print("FIRST CASE NOT SATISFIED")
            if X == 360 and len(self.B) == self.N:  # SECOND CASE VERIFICATION
                print("SEOND CASE SATISFIED")
            else:
                print("SECOND CASE NOT SATISFIED")
            if K == self.B:  # THIRD CASE VERIFICATION
                print("THIRD CASE SATISFIED")
            else:
                print("THIRD CASE NOT SATISFIED")
        else:
            print("GIVE THE INPUT PROPERLY OR CHECK WHEATHER THE SUM OF ANGLESIS360")
C = CASE()
C.fun1()