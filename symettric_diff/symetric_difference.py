#find all the possible XOR result of two sets
#to see if attackers are able to figure out the secret key
#this is built upon the fact that the group ({0,1}^n, XOR)
#is isomorphic to the group (P(S), Δ) where S = {1,2,...,n}
#P() is the power set of S and Δ is the symmetric difference
#Detailed proof can be seen https://accu.org/journals/overload/20/109/lewin_1915/

def sym_diff(A, B):
    return set(A-B).union(set(B-A))

def sym_diff_sets(set_list):
    if len(set_list) == 1:
        return set_list[0]
    elif len(set_list) == 2:
        return sym_diff(set_list[0], set_list[1])
    else:
        return sym_diff(set_list[0], sym_diff_sets(set_list[1:]))
    

        

if __name__ == "__main__":
    set_list = [{1,2,3,4,5}, 
                {1,2,3,4,6}, 
                {1,2,3,4,7}, 
                {1,2,3,4,8}]
    sym_diff(set_list)