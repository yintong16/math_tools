def rule_set(val):
    rule = {
        "111": "0",
        "110": "0",
        "101": "0",
        "100": "1",
        "011": "1",
        "010": "1",
        "001": "1",
        "000": "0"
    }
    return rule[val]

def parser(size):
    with open ("rule30_det.txt", "r") as f:
        with open ("parsed_rule30.txt", "w") as f2:
            for j in range(size):
                line = f.readline()
                for i in range(size):
                    f2.write(line[i])
                    if i + 1 == size:
                        f2.write("\n")
                    else:
                        f2.write(" ")
            

def run_rule30(size):
    half = size//2;
    with open ("rule30_det.txt", "r+") as f:
        f.write("0"*half + "1" + "0"*half + "\n")
        prev = "0"*half + "1" + "0"*half
        for i in range(size-1):
            new = f"{'0'}"
            for j in range(1, len(prev)-1):
                    new += rule_set(prev[j-1] + prev[j] + prev[j+1])
            new += "0"
            f.write(new + "\n")
            prev = new





if __name__ == "__main__":
    size = 11#this numner has to be odd
    parse = True
    run_rule30(size)
    if parse:
        parser(size)
    print("Rule 30 has been written to rule30_det.txt")