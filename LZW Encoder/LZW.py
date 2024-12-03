import sys
import re

def Get_MobyDick_Data(WordsOrCaraktors):
    MobyDickDataArray=[]
    # We wish the data array to be in Caraktors
    if WordsOrCaraktors == "C":
        print("Character Chosen")
        try:
            with open("Novel\\Moby Dick.txt", "r", encoding="utf-8") as f:
                for x in f:
                    x = list(x)   
                    MobyDickDataArray.extend(x)
        except UnicodeDecodeError as e:
            print(f"Error reading the file: {e}")
    # We wish the data array to be in Words
    else:
        print("Words Chosen")
        try:
            with open("Novel\\Moby Dick.txt", "r", encoding="utf-8") as f:
                for x in f:
                    x = re.findall(r'[A-Za-z]+|[^A-Za-z]+', x)
                    MobyDickDataArray.extend(x)
        except UnicodeDecodeError as e:
            print(f"Error reading the file: {e}")

    return MobyDickDataArray

def LZW_Homebrew(Alphabet, Data):
    list = Alphabet
    Novel = Data
    i = 0
    j = 0
    code = []
    while 1:
        j = i
        while 1:
            lzw = ''.join(Novel[j:i+1]) 
            if lzw not in list:
                list.append(lzw)
                code.append(list.index(lzw[:-1]))
                
                j = i
                break
            i += 1
            if lzw == ''.join(Novel[j:]):
                code.append(list.index(lzw))
                break
        # print("----------")    
        # print(list)
        # print(i)
        # print("----------")
        print(round((i/(len(Novel)-1))*100, 3), "\t %\r", end="")
        if i >= len(Novel)-1:
            break
    code.append(0)
    #print(code)
    f = open("Homebrew LZW.txt","w")
    f.write(str(code))
    f.close()

def LZW(Alphabet, Data):
    # Initialize the dictionary with the given Alphabet (with 1-based indexing)
    dictionary = {symbol: idx for idx, symbol in enumerate(Alphabet, start=1)}
    next_code = len(dictionary) + 1  # The next available code to add to the dictionary
    i = 0
    code = []
    n = len(Data)

    while i < n:
        substring = Data[i]
        
        while i + 1 < n and substring + Data[i + 1] in dictionary:
            i += 1
            substring += Data[i]
        
        code.append(dictionary[substring])
        
        if i + 1 < n:
            dictionary[substring + Data[i + 1]] = next_code
            next_code += 1
        i += 1
        
        # if i % (n // 100) == 0:
        #     print(round((i / (n - 1)) * 100, 3), "%\r", end="")
    code.append(0)
    f = open("Optimized LZW.txt","w")
    f.write(str(code))
    f.close()

def main():
    Test = 0
    #-------------Test tools for both algurythms----------
    if Test:
        AlphabetHOMB = ["#","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        AlphabetOPTZ = AlphabetHOMB
        #         0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23
        Novel = ["T","O","B","E","O","R","N","O","T","T","O","B","E","O","R","T","O","B","E","O","R","N","O","T"]
    else:
        Data = Get_MobyDick_Data("W")
        Novel = [item.replace("\n", "Φ") for item in Data] # we cant use \n so we use Φ
        AlphabetOPTZ = sorted(set(Novel))
        Novel.append("")
        AlphabetHOMB = sorted(set(Novel))

    #-------------THE OPTIMIZED LZW ALGURYTHM-------------
    print("working on OPtimized LZW: ...")
    LZW(AlphabetOPTZ,Novel)
    
    #-------------THE ORIGINAL LZW ALGURYTHM--------------
    print("working on HOMEBREW LZW: you need to turn on manuly")
    # if Test != 1:
    #LZW_Homebrew(AlphabetHOMB,Novel)

if __name__ == "__main__":
    main()