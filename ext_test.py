import re
filepath="/root/py3/Manuscript_Krantz_ArXiv_v4b_blackline.tex"
get1=open(filepath,"r").read()

get2=""
get3=re.findall(r"begin\{equation\}\n(.*)\nend\{equation\}",get1,re.M)#
get2=get2+'\n'.join(get3)

del1=get2.replace("\\begin{equation}","")
del2=del1.replace("\\end{equation}","")
print(get2)

