from fuzzylogic.classes import Domain, Set
from fuzzylogic.functions import bounded_linear
from fuzzylogic.rules import rescale, round_partial

rating = Domain("ratings", 1, 10, res=0.1)
rating.norm = Set(bounded_linear(1,10))

weights = {"beverage": 0.3, 
           "atmosphere": 0.2, 
           "looks":0.2,
           "taste": 0.3}

def weighted_sum(weights, target):
    rsc = rescale(target._low, target._high)
    
    def f(factors):
        result = sum(r * weights[n] for n, r in factors.items())
        return round_partial(rsc(result), target._res)
    return f


r = weighted_sum(weights=weights, target=rating)

ratings = {"beverage": rating.min(int(input('beverage: '))),
           "atmosphere": rating.min(int(input('atmosphere: '))),
           "looks": rating.min(int(input('looks: '))),
            "taste": rating.min(int(input('taste: ')))}
r(ratings)
