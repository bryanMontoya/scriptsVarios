def make_division_by(n):
    
    def make_divisor(x):
        return x/n
        
    return make_divisor

division_by_3 = make_division_by(3)
print(division_by_3(18))