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
    with open(source_path, "r") as x, open(output_path, "w") as y:
            y.writelines(x)

def Write_elements(path,text_array):
    for item in text_array:
        with open(path,"a") as f:
            f.write(item + "\n")

def Calculate_characters_in_file(path):
    with open(path, "r") as f:
        count = len(f.read())
        return count

def Calculate_lines_in_file(path):
    with open(path, "r") as f:
        text = f.readlines()
        count = len(text)
        return count


FILE_PATH = "files/source.txt"
names = ["Pepa", "Karel", "Honza"]

text = Read_file(FILE_PATH)
Write_seven_long(text,"files/sevenplus.txt")
Repost(FILE_PATH, "files/rewrite.txt")
Write_elements("files/names.txt",names)
number_of_chars = Calculate_characters_in_file("files/names.txt")
print(f"There is {number_of_chars} characters in file")
number_of_lines = Calculate_lines_in_file("files/names.txt")
print(f"There is {number_of_lines} lines in file")


