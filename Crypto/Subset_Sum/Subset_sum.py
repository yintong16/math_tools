def super_increasing_sequence_verifier(sequence: list):
    sequence = sorted(sequence)
    for i in range(len(sequence)-1):
        if sequence[i]*2 > sequence[i+1]:
            return False
    return True

def subset_sum_super_increasing_sequence_solver(target: int, sequence: list):
    # Here we assume that given sequence is sorted
    X = []
    if sequence[-1] > sequence[0]:
        sequence = sequence[::-1]
    for i in sequence:
        if i <= target:
            target -= i
            X.append(1)
        else:
            X.append(0)
    if target == 0:
        return X[::-1]
    else:
        return "Solution does not exist"