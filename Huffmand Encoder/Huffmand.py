import numpy
import heapq # A Huffman Tree Node 
import re

class node: 
	def __init__(self, freq, symbol, left=None, right=None): 
		self.freq = freq 

		self.symbol = symbol 
 
		self.left = left 
 
		self.right = right 

		self.huff = '' 

	def __lt__(self, nxt): 
		return self.freq < nxt.freq 

def HOFFMAND(EntropyList):
    char = []
    freq = []
    nodes = []
    for i in EntropyList:
        char.append(i[0])
        freq.append(i[1])

    for x in range(len(char)): 
        heapq.heappush(nodes, node(freq[x], char[x])) 

    while len(nodes) > 1: 
        left = heapq.heappop(nodes) 
        right = heapq.heappop(nodes)  
        left.huff = 0
        right.huff = 1
        newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right) 

        heapq.heappush(nodes, newNode) 
    sum = EvalueateHuffmand(EntropyList, nodes[0])
    return sum

def EvalueateHuffmand(EntropyList, node, val=''): 
    total = 0
    newVal = val + str(node.huff) 

    if(node.left): 
        total += EvalueateHuffmand(EntropyList, node.left, newVal) 
    if(node.right): 
        total += EvalueateHuffmand(EntropyList, node.right, newVal) 

    if(not node.left and not node.right): 
        #print(f"{node.symbol} -> {newVal}") 
        for i in EntropyList:
            if i[0] == node.symbol: 
                val = i[1] * len(newVal)
                total += val
    return total

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
    EntropyList = sorted(EntropyList,key=lambda x: x[1])
    return Hx, EntropyList

def main():
    print("Huffman")
    Data = Get_MobyDick_Data("W") # C = carakters W = Words
    print("Working On Entropy Calculations ...")
    Hx, EntropyList = Entropy(Data)
    print(f"Entropy: {Hx:.4f}")
    print("Working on HUFFMAND Algorithm ...")
    sum = HOFFMAND(EntropyList)
    print("Huffman Codes: can be shown in [def EvalueateHuffmand]")
    print("Algorithm Entropy : " + str(sum) + f" Entropy: {Hx:.4f}" )

if __name__ == "__main__":
    main()