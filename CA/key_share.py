from Rule30 import rule_set
import quantumrandom as qr

def gnerate_rand(type, len):
    rand = qr.get_data(data_type=type, array_length=len)
    return rand

def parse_random(rand):
    pre_parse = ""
    parsed = []
    for i in range(len(rand)):
        pre_parse+=str(bin(rand[i]))[2:]
    for i in range(len(pre_parse)-2):
        parsed.append(pre_parse[i:i+3])
    return parsed
    
def evolution30(parsed_rand):
    evo_key = ""
    for i in parsed_rand:
        evo_key += rule_set(i)
    return evo_key




if __name__ == "__main__":
    rand1 = gnerate_rand('uint16', 24)
    parsed_rand1 = parse_random(rand1)
    print("parsed_rand1 size:",len(parsed_rand1))
    key_evo1 = evolution30(parsed_rand1)

    rand2 = gnerate_rand('uint16', 24)
    parsed_rand2 = parse_random(rand2)
    print(len(parsed_rand2))
    key_evo2 = evolution30(parsed_rand2)

    print(key_evo1)
    print(key_evo2)
