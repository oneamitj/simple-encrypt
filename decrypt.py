# find d_key
# 1. find det = |e_key| mod 41
# 2. find x: det*x = 1 mod 41
# 3. find Y: Y = Adj(A) mod 41
# 4. find d_key: d_key = x*Y mod 41
# Note: Adj(A) = Trans[ cofactor(A) ]





def assign(data):
        alpha = " abcdefghijklmnopqrstuvwxyz!,.?"
        number = 0
        if type(data) == str:
            return alpha.index(data)

        elif type(data) == int:
            while(number != data):
                number = number + 1
            return alpha[number]

for value in " abcdefghijklmnopqrstuvwxyz!,.?":
	print value+'->'+str(assign(value)),

