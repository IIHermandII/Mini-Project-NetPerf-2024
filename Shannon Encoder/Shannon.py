

def Get_MobyDick_Data(WordsOrCaraktors):
    MobyDickDataArray=[]
    # We wish the data array to be in Caraktors
    if WordsOrCaraktors == "Caraktors":
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

def main():
    print("Shannon")
    Data = Get_MobyDick_Data("Caraktors")
    print(Data)

if __name__ == "__main__":
    main()