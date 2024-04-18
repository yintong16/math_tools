#this is an implementation of index calculus algorithm aims to solve the discrete logrithm problem
#input a generater g of a cyclic group G, a prime number p, and argument h
#output x such that g^x = h mod q
#the algorithm is based on the assumption that the factor base is small and the smoothness bound is small

def index_calc(g, p, h):
    #initialize the factor base
    factor_base = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    #initialize the smoothness bound
    B = 10
    #initialize the relation list
    relation_list = []
    #initialize the list of smooth numbers
    smooth_num = []
    #initialize the list of smooth numbers' index
    smooth_num_index = []
    #initialize the list of logarithm of smooth numbers
    smooth_num_log = []


if __name__ == "__main__":
    g = 2
    p = 23
    h = 9
    index_calc(g, p, h)


