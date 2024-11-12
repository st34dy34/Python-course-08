def Read_file(path): 
    with open(path,"r") as f:
        lines = f.readlines()
        clean_lines = [line.strip() for line in lines]
        return clean_lines

def Write_seven_long(text,path):
    with open(path, "w") as f:
        for word in text:
            if len(word) > 7:
                f.write(word)

def Repost(source_path,path):
    with open(source_path, "r") as x:
         with open(path, "w") as y:
            y.writelines(x)
   

FILE_PATH = "files/source.txt"

text = Read_file(FILE_PATH)
Write_seven_long(text,"files/sevenplus.txt")
Repost(FILE_PATH, "files/rewrite.txt")
print(text)


