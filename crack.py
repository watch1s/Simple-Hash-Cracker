import hashlib
import argparse
import re
import time

def detect_hash_type(hash_str):
    hash_str = hash_str.lower().strip()
    
    if not re.fullmatch(r'^[0-9a-f]+$', hash_str): #Checks (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) and  (a, b, c, d, e, f)
        return None

    length = len(hash_str)
    if length == 32:
        return 'md5'
    elif length == 40:
        return 'sha1'
    elif length == 64:
        return 'sha256'
    elif length == 128:
        return 'sha512'
    else:
        return None

def basic_rules(base_word):
    
    #Applies basic rules to essential words for more accurative detection.
    #Examples: 'password' → ['password', 'password1', 'password123', 'password!', ...]
    
    rules = [
        "abc",
        "6",
        "",
        "123",
        "1234",
        "2024",
        "2025",
        "2026",
        "!",
        "1!",
        "123!",
    ]
    return [base_word + rule for rule in rules]


def crack_hash(hash_to_crack, wordlist, hash_type=None):
    
    if hash_type is None:
        hash_type = detect_hash_type(hash_to_crack)
        if hash_type is None:
            raise ValueError("Hash type not found. Please enter what specify type you want with --type .")
        print(f"[i] Hash type: {hash_type}")
    
    
    if hash_type == 'md5':
        hash_func = hashlib.md5
    elif hash_type == 'sha1':
        hash_func = hashlib.sha1
    elif hash_type == 'sha256':
        hash_func = hashlib.sha256
    else:
        raise ValueError("Unsupported hash type")

    with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            base_password = line.strip()
            
            for candidate in basic_rules(base_password):  
                hashed = hash_func(candidate.encode()).hexdigest()
                if hashed == hash_to_crack:  
                    return candidate
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Hash Cracker with Benchmarking")
    parser.add_argument("hash", help="Hash to break")
    parser.add_argument("wordlist", help="Wordlist to use")
    parser.add_argument("--type", default=None, choices=["md5", "sha1", "sha256"])
    args = parser.parse_args()

    start_time = time.time()  

    try:
        result = crack_hash(args.hash, args.wordlist, args.type)
        elapsed = time.time() - start_time 

        if result is None:
            print("[-] Password NOT found")
        else:
            print(f"[+] Password found: {result}")
        
        print(f"Time elapsed: {elapsed:.5f} seconds")
        
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"[!] Error: {e}")
        print(f"Time elapsed before error: {elapsed:.5f} seconds")
