import sys
sys.path.append('C:/Users/Yintong Luo/Desktop/math_tools/Determinant_Calculator')
# Now you can import the file
import nxn_determinant as det


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

def cut_CA(size):
    with open ("parsed_rule30.txt", "r") as f:
        with open ("cutted.txt", "w") as f2:
        #read and write the first line
            line = f.readline()
            line = line.split()
            left, right = 0, 0
            for index, num in enumerate(line):
                if num == "1":
                    left = index - size//2
                    right = index + size//2
            for i in range(left, right+1):
                f2.write(line[i])
                if i + 1 == right+1:
                    f2.write("\n")
                else:
                    f2.write(" ")

        #write the rest of the lines
            for i in range(size-1):
                line = f.readline()
                line = line.split()
                for j in range(left, right+1):
                    f2.write(line[j])
                    if j + 1 == right+1:
                        f2.write("\n")
                    else:
                        f2.write(" ")





if __name__ == "__main__":
    size = 201#this numner has to be odd
    parse = True
    run_rule30(size)
    print("Rule 30 has been written to rule30_det.txt")
    if parse:
        parser(size)
        print("Rule 30 has been parsed and written to parsed_rule30.txt")
    
    #cut out a part of the CA
    cutted_array = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    for size in cutted_array:
        cut_CA(size)
        #calculate the determinant of the parsed rule 30
        matrix = det.construct_matrix("cutted.txt")
        determinant = det.det(matrix)
        print(f"The determinant of the matrix is: {determinant}")
        open('cutted.txt', 'w').close()
    