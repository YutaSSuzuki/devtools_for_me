import pyperclip as pc
with open(r"/Users/suzukiyuuta/Desktop/read_python/for_read.txt",encoding="utf-8") as fin:
    fin_list = [line.strip() for line in fin]
    rm_identation=" ".join(fin_list)
    pc.copy(rm_identation)
