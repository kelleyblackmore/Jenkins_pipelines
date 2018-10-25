print('Hello User')

def pv_f(fv,r,n):
    """Objective: estimate present value
                     fv
    formula  : pv=-------------
                   (1+r)^n
          fv: fture value
          r : discount periodic rate
          n : number of periods

    Example #1  >>>pv_f(100,0.1,1)
                   90.9090909090909
    
    Example #2: >>>pv_f(r=0.1,fv=100,n=1)
                    90.9090909090909
    """
    return fv/(1+r)**n


print(pv_f(100,0.1,1))