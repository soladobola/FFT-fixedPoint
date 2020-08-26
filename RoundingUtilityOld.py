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
        """ Tie breaking is away from zero """
        
        neg = 1 if value < 0 else 0
        # trim sufix added by bin function "-0b" or "0b"
        binary = bin(value)[2 + neg:]
        # extract surplus bits
        surp = int(binary[-trunc_bits:], 2)
        if surp == 0:
            # all zeros, just trunc all the bits
            return value >> trunc_bits
        
        # first calculate two possible option
        op1 = value >> trunc_bits
        op2 = op1 + 1
        
        #check who is nearer to value
        dist1 = abs((op1 << trunc_bits) - value)
        dist2 = abs((op2 << trunc_bits) - value)
        
        if dist1 < dist2:
            return op1
        elif dist1 > dist2:
            return op2
        else:
            # tie, use option which is smaller which is op1
            return op1
        
        
    def round_half_up(value, trunc_bits):
        """ Tie breaking is away from zero """
        
        neg = 1 if value < 0 else 0
        # trim sufix added by bin function "-0b" or "0b"
        binary = bin(value)[2 + neg:]
        # extract surplus bits
        surp = int(binary[-trunc_bits:], 2)
        if surp == 0:
            # all zeros, just trunc all the bits
            return value >> trunc_bits
        
        # first calculate two possible option
        op1 = value >> trunc_bits
        op2 = op1 + 1
        
        #check who is nearer to value
        dist1 = abs((op1 << trunc_bits) - value)
        dist2 = abs((op2 << trunc_bits) - value)
        
        if dist1 < dist2:
            return op1
        elif dist1 > dist2:
            return op2
        else:
            # tie, use option which is bigger
            return op2
        
    def round_half_towards_zero(value, trunc_bits):
        """ Tie breaking is away from zero """
        # extract surplus bits
        neg = 1 if value < 0 else 0
        # trim sufix added by bin function "-0b" or "0b"
        binary = bin(value)[2 + neg:]
        surp = int(binary[-trunc_bits:], 2)
        if surp == 0:
            # all zeros, just trunc all the bits
            return value >> trunc_bits
        
        # first calculate two possible option
        op1 = value >> trunc_bits
        op2 = op1 + 1
        
        #check who is nearer to value
        dist1 = abs((op1 << trunc_bits) - value)
        dist2 = abs((op2 << trunc_bits) - value)
        
        if dist1 < dist2:
            return op1
        elif dist1 > dist2:
            return op2
        else:
            # tie, use option which is closer to zero
            return op2 if abs(op1) > abs(op2) else op1    
    
        
    def round_half_away_from_zero(value, trunc_bits):
        """ Tie breaking is away from zero """
        # extract surplus bits
        neg = 1 if value < 0 else 0
        # trim sufix added by bin function "-0b" or "0b"
        binary = bin(value)[2 + neg:]
        surp = int(binary[-trunc_bits:], 2)
        if surp == 0:
            # all zeros, just trunc all the bits
            return value >> trunc_bits
        
        # first calculate two possible option
        op1 = value >> trunc_bits
        op2 = op1 + 1
        
        #check who is nearer to value
        dist1 = abs((op1 << trunc_bits) - value)
        dist2 = abs((op2 << trunc_bits) - value)
        
        if dist1 < dist2:
            return op1
        elif dist1 > dist2:
            return op2
        else:
            # tie, use option which is farest from zero
            return op1 if abs(op1) > abs(op2) else op2
    
    
        
    # same as above, just different tie rule
    def round_half_to_even(value, trunc_bits):
        """ Tie breaking is parity of number, even number wins """
        # extract surplus bits
        neg = 1 if value < 0 else 0
        # trim sufix added by bin function "-0b" or "0b"
        binary = bin(value)[2 + neg:]
        surp = int(binary[-trunc_bits:], 2)
        if surp == 0:
            # all zeros, just trunc all bits
            return value >> trunc_bits
        
        # first calculate two possible option
        op1 = value >> trunc_bits
        op2 = op1 + 1
        
        #check who is nearer to value
        dist1 = abs((op1 << trunc_bits) - value)
        dist2 = abs((op2 << trunc_bits) - value)
        
        if dist1 < dist2:
            return op1
        elif dist1 > dist2:
            return op2
        else:
            # tie, use option which is even number
            # one of options must me even
            return op1 if op1 % 2 == 0 else op2
        
    def round_half_to_odd(value, trunc_bits):
        """ Tie breaking is parity of number, even number wins """
        # extract surplus bits
        neg = 1 if value < 0 else 0
        # trim sufix added by bin function "-0b" or "0b"
        binary = bin(value)[2 + neg:]
        surp = int(binary[-trunc_bits:], 2)
        if surp == 0:
            # all zeros, just trunc all bits
            return value >> trunc_bits
        
        # first calculate two possible option
        op1 = value >> trunc_bits
        op2 = op1 + 1
        
        #check who is nearer to value
        dist1 = abs((op1 << trunc_bits) - value)
        dist2 = abs((op2 << trunc_bits) - value)
        
        if dist1 < dist2:
            return op1
        elif dist1 > dist2:
            return op2
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