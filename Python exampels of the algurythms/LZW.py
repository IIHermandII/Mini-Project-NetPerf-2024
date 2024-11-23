def encoding(s1):
    print("Encoding")
    table = {chr(i): i for i in range(256)}
    
    p = s1[0]
    code = 256
    output_code = []
    print("String\tOutput_Code\tAddition")

    for i in range(len(s1)):
        if i != len(s1) - 1:
            c = s1[i + 1]
        else:
            c = ""
        
        if p + c in table:
            p += c
        else:
            print(f"{p}\t{table[p]}\t\t{p + c}\t{code}")
            output_code.append(table[p])
            table[p + c] = code
            code += 1
            p = c
            
    print(f"{p}\t{table[p]}")
    output_code.append(table[p])
    return output_code

def decoding(op):
    print("\nDecoding")
    table = {i: chr(i) for i in range(256)}
    
    old = op[0]
    s = table[old]
    c = s[0]
    print(s)
    count = 256

    for i in range(len(op) - 1):
        n = op[i + 1]
        if n not in table:
            s = table[old] + c
        else:
            s = table[n]
        
        print(s)
        c = s[0]
        table[count] = table[old] + c
        count += 1
        old = n

def main():
    s = "WYS*WYGWYS*WYSWYSG"
    output_code = encoding(s)
    print("Output Codes are:", ' '.join(map(str, output_code)))
    decoding(output_code)

if __name__ == "__main__":
    main()
    #https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/
