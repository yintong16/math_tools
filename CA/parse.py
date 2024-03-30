
def parser(size):
    with open ("rule30_det.txt", "r") as f:
        with open ("parsed_rule30.txt", "w") as f2:
            for j in range(201):
                line = f.readline()
                for i in range(size):
                    f2.write(line[i])
                    if i + 1 == size:
                        f2.write("\n")
                    else:
                        f2.write(" ")
            
    

if __name__ == "__main__":
    size = 11#this numner has to be odd(enforced by contruction)
    parser(size)