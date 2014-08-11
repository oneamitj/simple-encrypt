def assign(data):
        alpha = " abcdefghijklmnopqrstuvwxyz!,.?"
        number = 0
        if type(data) == str:
            return alpha.index(data)

        elif type(data) == int:
            while(number != data):
                number = number + 1
            return alpha[number]

print "Number -> Alpha", assign(28)
print "Alpha -> Number", assign('?')
