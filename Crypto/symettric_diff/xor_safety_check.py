#find all the possible XOR result of two sets to see
#if attackers are able to figure out the secret key
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
        
def comb_sym_diff(set_list):
    #return all the possible symmetric differences of the sets in set_list
    result = []
    for i in range(len(set_list)):
        for j in range(i+1, len(set_list)):
            result.append(sym_diff(set_list[i], set_list[j]))
    return result
        
def comb_sym_diff_2(set_list1, set_list2):
    #return all the possible symmetric differences of the sets in set_list1 and set_list2
    result = []
    for i in set_list1:
        for j in set_list2:
            result.append(sym_diff(i, j))
    return result

def comb_sym_diff_wth_depth(set_list, depth):
    #return all the possible symmetric differences of the sets in set_list
    #with depth number of symmetric differences
    result = []
    for i in range(len(set_list)):
        for j in range(i+1, len(set_list)):
            result.append(sym_diff(set_list[i], set_list[j]))
    if depth == 1:
        return result
    else:
        return comb_sym_diff_wth_depth(result, depth-1)

def result_analysis(result):
    exposed = set()
    exposed_pair = set()
    for i in result:
        if len(i) == 1:
            exposed.add(frozenset(i))
        elif len(i) == 2:
            exposed_pair.add(frozenset(i))

    
    if len(exposed) == 0:
        print("No exposed element")
        if len(exposed_pair) == 0:
            print("No exposed pair")
            return None
        else:
            print(f"The exposed pairs: {exposed_pair}")
            return exposed_pair
    else:
        print(f"The exposed elements: {exposed}")
        return exposed


if __name__ == "__main__":
    set_list = [{"k2", "r"}, 
                {"k1", "M1"}, 
                {"k3", "M3"}, 
                {"k3", "r", "F1"},
                {"k1", "r", "F3"}]
    
    depth_list = []
    depth = 3
    for i in range(depth):
        print(f"The symmetric differences of the sets with depth {i+1}:")
        result = comb_sym_diff_wth_depth(set_list, i+1)
        depth_list.append(result)
        result_analysis(result)
        print()

    #every depth with original set
    for i in range(len(depth_list)):
        print(f"The symmetric differences of the sets depth {i+1} with 0:")
        result = comb_sym_diff_2(depth_list[i], set_list)
        result_analysis(result)
        print()
    

    

