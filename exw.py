fo=open("1.tex","r")
print(fo.name)
flag_eq=0
n=0
save_Str=""
#依次读取
for line in fo.readlines():
    tmp_str=line
    if "%" in line or "label" in line:
        continue
    if "\\begin{equation" in line or "\\begin{align" in line \
            or "\\begin{multline" in line:
        flag_eq=1
        continue
    if "\end{equation" in line or "\end{align" in line \
            or "\end{multline" in line:
        flag_eq=0
        n=n+1
        save_Str=save_Str+str(n)+"\n"
    if flag_eq==1:
        print(line)
        save_Str=save_Str+line

#关闭文件
fo.close()
fw=open("2.txt","w")
fw.writelines(save_Str)
print(fw.name+" ok")
fw.close()
