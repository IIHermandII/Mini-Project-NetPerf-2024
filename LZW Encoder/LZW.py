LZWList = [['#', 0],['A', 1],['B', 2],['C', 3],['D', 4],['E', 5],['F', 6],['G', 7],['H', 8],['I', 9],['J', 10],['K', 11],['L', 12],['M', 13],['N', 14],['O', 15],['P', 16],['Q', 17],['R', 18],['S', 19],['T', 20],['U', 21],['V', 22],['W', 23],['X', 24],['Y', 25],['Z', 26]]
Novel = ["T","O","B","E","O","R","N","O","T","T","O","B","E","O","R","T","O","B","E","O","R","N","O","T"]
#         0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23

import sys

def Get_MobyDick_Data(WordsOrCaraktors):
    MobyDickDataArray=[]
    # We wish the data array to be in Caraktors
    if WordsOrCaraktors == "C":
        print("C")
        try:
            with open("Novel\\Moby Dick.txt", "r", encoding="utf-8") as f:
                for x in f:
                    x = list(x)   # You can still print the lines if you need to debug
                    MobyDickDataArray.extend(x)
        except UnicodeDecodeError as e:
            print(f"Error reading the file: {e}")
    # We wish the data array to be in Words
    else:
        print("Words chousen")
        try:
            with open("Novel\\Moby Dick.txt", "r", encoding="utf-8") as f:
                for x in f:
                    x = x.split()   # You can still print the lines if you need to debug
                    MobyDickDataArray.extend(x)
        except UnicodeDecodeError as e:
            print(f"Error reading the file: {e}")

    return MobyDickDataArray

def LZW_Homebrew(Alphabet, Data):
    #list = ["#","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
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
        # print(list[27:])
        # print(i)
        # print("----------")
        print(round((i/(len(Novel)-1))*100,3),"\t %\r",end="")
        if i >= len(Novel)-1:
            break
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
        # Start with the current character
        substring = Data[i]
        
        # Expand the substring as long as it exists in the dictionary
        while i + 1 < n and substring + Data[i + 1] in dictionary:
            i += 1
            substring += Data[i]
        
        # Output the code for the current substring
        code.append(dictionary[substring])
        
        # Add the new substring to the dictionary, if not already present
        if i + 1 < n:
            dictionary[substring + Data[i + 1]] = next_code
            next_code += 1
        
        # Move to the next character
        i += 1
        
        # Print progress (every 1% of data processed)
        if i % (n // 100) == 0:
            print(round((i / (n - 1)) * 100, 3), "%\r", end="")

    # Print the final LZW encoded code
    #print(code)
    f = open("LZW with help.txt","w")
    f.write(str(code))
    f.close()






# Example usage



def LZWListExpander():
    Nr = 26  
    ElementLengthList = [2, 3]  
    for ElementLength in ElementLengthList:  
        for CarakterIndex in range(0, len(Novel), ElementLength):  
            NewElement = Novel[CarakterIndex:CarakterIndex + ElementLength]  
            if NewElement not in [item[0] for item in LZWList]:  
                Nr += 1  
                LZWList.append([NewElement, Nr])  

    print("-------------")
    print(LZWList)

def main():
    #LZWListExpander()
    #test()
    Data = Get_MobyDick_Data("C")
    PhiList = [item.replace("\n", "Φ") for item in Data] # we cant use \n so we use Φ
    
    #list = ["#","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
    list = sorted(set(PhiList))
    print("SPEED:")
    LZW(list,PhiList)
    print("HOMEBREW:")
    PhiList.append("")
    list = sorted(set(PhiList))
    LZW_Homebrew(list,PhiList)

if __name__ == "__main__":
    main()