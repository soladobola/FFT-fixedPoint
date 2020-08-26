import random as rnd
class Round:
    # ------------------------ Direct methods BEGIN ---------------
    # Effectively rounding down
    def round_trunc(value, trunc_bits):
        """ Truncate bits """
        return value >> trunc_bits
    
    
    def round_up(value, trunc_bits):
        """ Round up """
        last_bit = 1 << (trunc_bits - 1)
        if last_bit & value > 0:
            return (value >> trunc_bits) + 1
        else:
            return (value >> trunc_bits)
        
        
        
    def round_towards_zero(value, trunc_bits):
        if value > 0:
            return value >> trunc_bits
        else:
            # works for <=
            last_bit = 1 << (trunc_bits - 1)
            if value & last_bit > 0:
                return (value >> trunc_bits) + 1
            else:
                return value >> trunc_bits
            
            
     
    def round_away_from_zero(value, trunc_bits):
        if value > 0:
            last_bit = 1 << (trunc_bits - 1)
            if value & last_bit > 0:
                return (value >> trunc_bits) + 1
            else:
                return value >> trunc_bits        
        else:
            return value >> trunc_bits
    
    
  # ------------------------ Direct methods END ---------------
  
  
  # ------------------------ Round to nearest BEGIN -----------
     
    def round_half_down(value, trunc_bits):
        
        if trunc_bits == 0:
            return value >> trunc_bits
        op1 = value >> trunc_bits
        op2 = op1 + 1
        half = (op1 << trunc_bits) + (((op2 << trunc_bits) - (op1 << trunc_bits)) >> 1)
        if value > half:
            return op2
        if value < half:
            return op1
        else:
            return op1
        
        
        
    def round_half_up(value, trunc_bits):
        
        if trunc_bits == 0:
            return value >> trunc_bits
        op1 = value >> trunc_bits
        op2 = op1 + 1
        half = (op1 << trunc_bits) + (((op2 << trunc_bits) - (op1 << trunc_bits)) >> 1)
        if value > half:
            return op2
        if value < half:
            return op1
        else:
            return op2
        
        
        
    def round_half_towards_zero(value, trunc_bits):
        
        if trunc_bits == 0:
            return value >> trunc_bits
        op1 = value >> trunc_bits
        op2 = op1 + 1
        half = (op1 << trunc_bits) + (((op2 << trunc_bits) - (op1 << trunc_bits)) >> 1)
        if value > half:
            return op2
        if value < half:
            return op1
        else:
            return op2 if abs(op1) > abs(op2) else op1
        
        
    
        
    def round_half_away_from_zero(value, trunc_bits):
        
        if trunc_bits == 0:
            return value >> trunc_bits
        op1 = value >> trunc_bits
        op2 = op1 + 1
        half = (op1 << trunc_bits) + (((op2 << trunc_bits) - (op1 << trunc_bits)) >> 1)
        if value > half:
            return op2
        if value < half:
            return op1
        else:
            return op1 if abs(op1) > abs(op2) else op2
    
    
        
    # same as above, just different tie rule
    def round_half_to_even(value, trunc_bits):
        
        if trunc_bits == 0:
            return value >> trunc_bits
        op1 = value >> trunc_bits
        op2 = op1 + 1
        half = (op1 << trunc_bits) + (((op2 << trunc_bits) - (op1 << trunc_bits)) >> 1)
        if value > half:
            return op2
        if value < half:
            return op1
        else:
            # tie, use option which is even number
            # one of options must me even
            return op1 if op1 % 2 == 0 else op2
        
        
    def round_half_to_odd(value, trunc_bits):
        
        if trunc_bits == 0:
            return value >> trunc_bits
        op1 = value >> trunc_bits
        op2 = op1 + 1
        half = (op1 << trunc_bits) + (((op2 << trunc_bits) - (op1 << trunc_bits)) >> 1)
        if value > half:
            return op2
        if value < half:
            return op1
        else:
            # tie, use option which is even number
            # one of options must me odd
            return op2 if op1 % 2 == 0 else op1
    
    # ------------------------ Round to nearest END -----------
    
    
    # one of stochastic methods
    def random_round_up(value, trunc_bits):
        """ Random round up """
        last_bit = 1 << (trunc_bits - 1)
        if last_bit & value > 0:
            r = rnd.random()
            if r < 0.5:
                return (value >> trunc_bits) + 1
            else:
                return (value >> trunc_bits)
        else:
            return (value >> trunc_bits)
        
    
    
    def trimBinary(opt):
        if opt == 'TRUNC' or opt == "ROUND_DOWN":
            return Round.round_trunc
        elif opt == 'ROUND_UP':
            return Round.round_up
        elif opt == "ROUND_TOWARDS_ZERO":
            return Round.round_towards_zero
        elif opt == 'ROUND_AWAY_FROM_ZERO':
            return Round.round_away_from_zero
        elif opt == 'ROUND_HALF_DOWN':
            return Round.round_half_down
        elif opt == 'ROUND_HALF_UP':
            return Round.round_half_up
        elif opt == 'ROUND_HALF_TOWARDS_ZERO':
            return Round.round_half_towards_zero
        elif opt == 'ROUND_HALF_AWAY_FROM_ZERO':
            return Round.round_half_away_from_zero
        elif opt == 'ROUND_HALF_TO_EVEN':
            return Round.round_half_to_even
        elif opt == 'ROUND_HALF_TO_ODD':
            return Round.round_half_to_odd
        elif opt == 'RANDOM_ROUND_UP':
            return Round.random_round_up
        else:
            raise ValueError('Method ' + opt + " is not implemented")
        
        
        
    def test(func1, func2, iter):
        cut = []
        values = []
        for x in range(1, iter):
            values.append(rnd.randint(1, 100000))
            cut.append(rnd.randint(0, 12))
        for x in range(len(cut)):
            n1 = func1(values[x], cut[x])
            n2 = func2(values[x], cut[x])
        #string = 'oke' if n1 == n2 else 'FUCK'
        #print(str(n1) + ' - ' + str(n2) + '  value: ' + str(values[x]) +  '  bits: ' + str(cut[x]) + '  -> ' + string)
            if n1 != n2:
                raise ValueError('NOPE!!')