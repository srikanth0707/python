lst=list()
lst1=list()
new_file=open('pass','w')
for i in open('all.txt','r'):
    lst.append(i)
for j in open('fail.txt','r'):
    lst1.append(j)
for k in range(len(lst)):
    if lst[k] in lst1:
        lst[k]='#'+str(lst[k])
# for ln in range(len(lst)):
#     new_file.write(lst(ln))
new_file.writelines(lst)
