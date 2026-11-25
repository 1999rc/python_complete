

def rate_per_hour(total_cost,hours):
    return total_cost/hours if hours >0 else 0.0 

# fix/zero-hour-bug
if __name__=='__main__':
    print(rate_per_hour(240,0))
