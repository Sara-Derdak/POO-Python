def max_lg(T):
    max=len(T[0])
    ch_log=T[0]
    for x in T :
       if len(x) > max :
           max=len(x)
           ch_log=x
    return ch_log


L=['sara','bilal','souhaib','mohammed']
print("la chaine la plus longue est : ",max_lg(L))