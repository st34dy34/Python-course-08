def Read_file(path): 
    with open(path,"r") as f:
        lines = f.readlines()
        clean_lines = [line.strip() for line in lines]
        return clean_lines

def Write_seven_long(text,path):
    with open(path, "w") as f:
        for word in text:
            print(len(word),word)
            if len(word) > 7:
                f.write(word)


FILE_PATH = "files/source.txt"

text = Read_file(FILE_PATH)
Write_seven_long(text,"files/sevenplus.txt")

print(text)


