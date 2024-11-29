import numpy
import heapq # A Huffman Tree Node 

class node: 
	def __init__(self, freq, symbol, left=None, right=None): 
		# frequency of symbol 
		self.freq = freq 

		# symbol name (character) 
		self.symbol = symbol 

		# node left of current node 
		self.left = left 

		# node right of current node 
		self.right = right 

		# tree direction (0/1) 
		self.huff = '' 

	def __lt__(self, nxt): 
		return self.freq < nxt.freq 

def EvalueateHuffmand(EntropyList, node, val=''): 
    total = 0
	# huffman code for current node 
    newVal = val + str(node.huff) 

    # if node is not an edge node 
    # then traverse inside it 
    if(node.left): 
        total += EvalueateHuffmand(EntropyList, node.left, newVal) 
    if(node.right): 
        total += EvalueateHuffmand(EntropyList, node.right, newVal) 

        # if node is edge node then 
        # display its huffman code 
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
    EntropyList = sorted(EntropyList,key=lambda x: x[1])
    return Hx, EntropyList

def main():
    print("Huffman")
    # Get data from Moby Dick as characters
    Data = Get_MobyDick_Data("C")
    # Calculate entropy
    Hx, EntropyList = Entropy(Data)
    print(f"Entropy: {Hx:.4f}")
    
    # Verify the number of unique symbols
    #print(f"Number of unique symbols: {len(EntropyList)}")
    
    # Generate Huffman codes
    print("Working on HUFFMAND Algurythm ...")
    char = []
    freq = []
    nodes = []
    for i in EntropyList:
        char.append(i[0])
        freq.append(i[1])

    for x in range(len(char)): 
        heapq.heappush(nodes, node(freq[x], char[x])) 

    while len(nodes) > 1: 
        # sort all the nodes in ascending order 
        # based on their frequency 
        left = heapq.heappop(nodes) 
        right = heapq.heappop(nodes) 
        # assign directional value to these nodes 
        left.huff = 0
        right.huff = 1
        # combine the 2 smallest nodes to create 
        # new node as their parent 
        newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right) 

        heapq.heappush(nodes, newNode) 
    sum = EvalueateHuffmand(EntropyList, nodes[0])
    print("Huffmand Codes:")
    print("Algurythm entrop : " + str(sum) + f" Entropy: {Hx:.4f}" )
# Huffman Tree is ready! 

if __name__ == "__main__":
    main()