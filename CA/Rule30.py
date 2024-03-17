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


def run_rule30():
    with open ("rule30.txt", "r+") as f:
        f.write("0"*100 + "1" + "0"*100 + "\n")
        prev = "0"*100 + "1" + "0"*100
        for i in range(100):
            new = f"{'0'}"
            for j in range(1, len(prev)-1):
                    new += rule_set(prev[j-1] + prev[j] + prev[j+1])
            new += "0"
            f.write(new + "\n")
            prev = new





if __name__ == "__main__":
    run_rule30()