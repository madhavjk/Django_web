
def frequency(test_str):
    
    all_freq = {}
    
    for i in test_str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
            
            
    print ("Count of all characters in GeeksforGeeks is :\n "
                                        +  str(all_freq))
                                        


test_str="GeeksforGeeks"
frequency(test_str)
