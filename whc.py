fo = open("1.tex", "r")
print (fo.name)
flag_begin =0
flag_label =0
tmp_str = ""
save_Str = ""
for line in fo.readlines():                          #依次读取每行  
    
                              
    if "\begin" in line:
        flag_label = 1
        flag_label = 0
    if "\label" in line:
        flag_label = 0
        flag_label = 1
        save_Str =  save_Str + tmp_str
    tmp_str =  line
 
# 关闭文件
fo.close()
fw = open("2.txt","w")
fw.writelines(save_Str)
fw.close()