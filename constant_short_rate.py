
from get_year_deltas import *

class constant_short_rate(object):
    """ Class for constant short rate discounting.
    
    
    Parameters
    ==========
    
    
    
    
    
    Results
    =======
    """
    
    def __init__(self, name, short_rate):
        
        self.name = name
        self.short_rate = short_rate
        if short_rate < 0:
            raise ValueError('Short rate negative.')
            
            
    def get_discount_factors(self, date_list, dtobjects=True):
        
        if dtobjects is True:
            dlist = get_year_deltas(date_list)
        else:
            dlist = np.array(date_list)
        dflist = np.exp(self.short_rate * np.sort(-dlist))
        return np.array((date_list, dflist)).T
        
        
    
    
    
    