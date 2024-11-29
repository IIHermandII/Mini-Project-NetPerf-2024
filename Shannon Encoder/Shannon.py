import numpy
import itertools
from tqdm import tqdm

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

def Entropy(Novel):
    # H(X) = sum( Pr[X=x] * log(1/(Pr[X=x])) )
    UniqueCharacters = set(Novel)
    NumberOfUniqueCharacters = len(UniqueCharacters)
   
    
    MobyDockNrOfCarakters = len(Novel)
    #print("Length of Moby Dick Array: " + str(MobyDockNrOfCarakters))
    #print("Number of unique characters: " + str(NumberOfUniqueCharacters))
    #print("Unik Carakters:")
    #print(UniqueCharacters)

    # Probability of carakter
    Hx = 0 
    EntropyList = []
    for carakter in UniqueCharacters:
        NumberOfSertantCharInNovel = Novel.count(carakter)
        ProbOfCarakter = NumberOfSertantCharInNovel/MobyDockNrOfCarakters
        Pruduct = ProbOfCarakter * numpy.log(1/ProbOfCarakter)
        Hx += Pruduct
        EntropyList.append([carakter,ProbOfCarakter])
    #     print("Number of "+ repr(carakter) + " in the Novel is: " + str(NumberOfSertantCharInNovel))
    #     print("probability of that carakter:" + "{:.8f}".format(ProbOfCarakter))
    # print("H(x) = " + str(Hx))
    EntropyList = sorted(EntropyList,key=lambda x: x[1], reverse=True)
    return Hx, EntropyList

def HaffPoint(EntropyList):
    # All proberbility summ to 1 so we ame after 0.5
    TotalProb = 0
    for i in EntropyList:
        TotalProb += i[1]
    
    SumAfter = 0
    SumBefor = 0
    HaffPoint = 0
    listNr = 0

    for i in EntropyList:
        SumAfter += i[1]
        if SumAfter >= TotalProb/2:
            HaffPoint = listNr
            SumBefor = SumAfter - i[1]
            break
        listNr += 1
    if abs(TotalProb/2 - SumAfter) <= abs(TotalProb/2 -SumBefor):
        return HaffPoint
    else:
        return HaffPoint - 1

def SHANNON(EntropyList, prefix=""):
    # Base case: only one symbol remains
    if len(EntropyList) == 1:
        symbol = EntropyList[0][0]
        return {symbol: prefix}

    # Find the splitting point
    split_idx = HaffPoint(EntropyList)

    # Split the list into two groups
    left = EntropyList[:split_idx + 1]
    right = EntropyList[split_idx + 1:]

    # Recursively assign codes to each group
    codes = {}
    codes.update(SHANNON(left, prefix + "0"))  # Assign "0" to the left group
    codes.update(SHANNON(right, prefix + "1"))  # Assign "1" to the right group

    return codes

def main():
    #Test()
    print("Shannon")
    Data = Get_MobyDick_Data("C")
    Hx, EntropyList = Entropy(Data)
    print(f"Entropy: {Hx:.4f}")
    print("Working on SHANNON Algurythm ...")
    codes = SHANNON(EntropyList)
    print("Shannon Codes:")
    ip = 0
    sum = 0
    for symbol, code in codes.items():
        #print(f"Symbol: {repr(symbol)} -> Code: {code}" + " Prob : " + str(EntropyList[ip][1]))
        sum += len(code) * EntropyList[ip][1]
        ip += 1
    print("Algurythm entrop : " + str(sum) + f" Entropy: {Hx:.4f}")

if __name__ == "__main__":
    main()