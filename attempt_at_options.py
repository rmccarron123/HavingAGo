class Call:
    def __init__(self, asset, strike, expiry, value):
        self.asset = asset    #enter name of the asset
        self.strike = strike  #enter strike price
        self.expiry = expiry  #enter expiry date
        self.value = value    #enter value paid for option
    def payoff(S_T):
        if S_T >= strike:
            C = S_T-strike
            return C
        else:
            return 0


class BottomStraddle(Call):
    def __init__(self, asset, strike, expiry, value_call, value_put):
        super().__init__(self, asset, strike, expiry)
        self.value_call = value_call
        self.value_put = value_put

    def payoff(S_T):
        if S_T >= strike:
            B = abs(S_T-strike)
            return B
        else:
            return 0

class Bull(Call):
    def __init__(self, asset, strike_1, strike_2 expiry, value_1, value_2):
        super().__init__(type, asset, expiry)
        self.strike_1 = strike_1
        self.strike_2 = strike_2
        self.value_1 = value_1
        self.value_2 = value_2
    
    def payoff(S_T):
        if S_T >= strike_1:
            if S_T >= strike_2
                D = strike_2-strike_1
                return D
            else:
                E = S_T-strike_1
                return E
        else:
            return 0
