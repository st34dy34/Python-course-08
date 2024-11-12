def Read_file(path): 
    with open(path,"r") as f:
        lines = f.readlines()
        clean_lines = [line.strip() for line in lines]
        return clean_lines

def Write_file(path,text): 
    with open(path,"w") as f:
        f.write(text)

def Append_file(path,text): 
    print(text)
    with open(path,"a") as f:
        f.write(text)


def Write_seven_long(text,path):
    with open(path, "w") as f:
        for word in text:
            if len(word) > 7:
                f.write(word)

def Repost(source_path,output_path):
    with open(source_path, "r") as x:
         with open(output_path, "w") as y:
            y.writelines(x)
   
def Add_asteriks(path):
    asteriks = "\n************"
    text = Read_file(path)
    happened = False
    index = 1
    for line in text:
        if "," in line:
            happened = True
            happend_i = index
        index += 1
    if happened == False:
        Append_file(path, asteriks)



        
                



FILE_PATH = "files/source.txt"

text = Read_file(FILE_PATH)
Write_seven_long(text,"files/sevenplus.txt")
Repost(FILE_PATH, "files/rewrite.txt")
Add_asteriks("files/asteriks.txt")
print(text)


