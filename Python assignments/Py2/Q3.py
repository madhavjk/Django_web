import math
from collections import Counter

class func:
    

    
    
    def __init__(self, n, n_num):
        self.n = n
        self.n_num = n_num
    
    def math(self):
        l =[]
        
        n_num = (self.n_num).sort()
        
        #median
        
        median = self.n_num[n//2]
        
        l.append(median)
        
        
        #Mean
        
        get_sum = sum(self.n_num)
        mean = get_sum / n
        
        l.append(mean)
        
        #mode
        
        data = Counter(self.n_num)
        get_mode = dict(data)
        mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
        
        if len(mode) == n:
            get_mode = "None"
        else:
            get_mode =  mode
        
        l.append(get_mode)
        
        
        return print(l)
        
n_num =  list(map(int, input("Enter a multiple value: ").split()))
n=len(n_num)
a=func(n,n_num)
a.math()
        
        
        
        
        
