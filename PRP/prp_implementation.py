from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import secrets
from typing import Callable

class PRP:
    def __init__(self, key: bytes):
        """Initialize PRP with a key"""
        self.key = key
        # AES is a common choice for PRP
        self.block_size = algorithms.AES.block_size // 8  # Convert bits to bytes

    def evaluate(self, input_block: bytes) -> bytes:
        """Forward PRP evaluation (encryption)"""
        if len(input_block) != self.block_size:
            raise ValueError(f"Input must be exactly {self.block_size} bytes")
        
        cipher = Cipher(algorithms.AES(self.key), modes.ECB())
        encryptor = cipher.encryptor()
        return encryptor.update(input_block) + encryptor.finalize()

    def inverse(self, output_block: bytes) -> bytes:
        """Inverse PRP evaluation (decryption)"""
        if len(output_block) != self.block_size:
            raise ValueError(f"Input must be exactly {self.block_size} bytes")
        
        cipher = Cipher(algorithms.AES(self.key), modes.ECB())
        decryptor = cipher.decryptor()
        return decryptor.update(output_block) + decryptor.finalize()

# Example usage and testing
def test_prp():
    # Generate random key
    key = secrets.token_bytes(32) # 256-bit key
    prp = PRP(key)

    # Test input
    input_block = secrets.token_bytes(16) # 128-bit block
    
    # Forward evaluation
    output = prp.evaluate(input_block)
    
    # Inverse evaluation
    recovered = prp.inverse(output)
    
    # Verify permutation properties
    print(f"Original input: {input_block.hex()}")
    print(f"PRP output:     {output.hex()}")
    print(f"Recovered:      {recovered.hex()}")
    print(f"Permutation property holds: {input_block == recovered}")

    # Different inputs give different outputs
    input2 = secrets.token_bytes(16)
    output2 = prp.evaluate(input2)
    print(f"Different inputs give different outputs: {output != output2}")

# Feistel network implementation (for educational purposes)
def feistel_network(rounds: int, round_function: Callable) -> PRP:
    """
    Construct a PRP using Feistel network
    """
    class FeistelPRP:
        def __init__(self):
            self.rounds = rounds
            self.F = round_function
        
        def evaluate(self, input_block: bytes) -> bytes:
            # Split input into left and right halves
            n = len(input_block) // 2
            L = input_block[:n]
            R = input_block[n:]
            
            # Feistel rounds
            for i in range(self.rounds):
                L, R = R, bytes(a ^ b for a, b in zip(L, self.F(R)))
            
            return R + L  # Swap last time
            
        def inverse(self, output_block: bytes) -> bytes:
            # Similar to evaluate but reverse round order
            n = len(output_block) // 2
            L = output_block[:n]
            R = output_block[n:]
            
            for i in range(self.rounds - 1, -1, -1):
                R, L = L, bytes(a ^ b for a, b in zip(R, self.F(L)))
                
            return R + L

    return FeistelPRP()

# Example round function for Feistel network
def example_round_function(key: bytes) -> Callable:
    from cryptography.hazmat.primitives import hmac, hashes
    
    def F(input_block: bytes) -> bytes:
        h = hmac.HMAC(key, hashes.SHA256())
        h.update(input_block)
        return h.finalize()[:len(input_block)]  # Truncate to match input length
        
    return F


test_prp()

def find_cycle():
    # Generate random key
    key = secrets.token_bytes(32) # 256-bit key
    prp = PRP(key)

    # Test input
    input_block = secrets.token_bytes(16) # 128-bit block
    

    output = prp.evaluate(input_block)
    counter = 0
    while(output != input_block):
        counter += 1
        output = prp.evaluate(output)
    print(counter)

find_cycle()# takes forever to run, need a smaller key size