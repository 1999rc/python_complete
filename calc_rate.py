def rate_per_hour(toal_cost,hours):
    return toal_cost/hours if hours >0 else 0.0 

if __name__=='__main__':
    print(rate_per_hour(240,0))
    