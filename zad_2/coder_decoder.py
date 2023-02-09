#8->4->12

def code(func_input):
    func_input=str(func_input)
    func_input="00"+func_input[0]+"0"+func_input[1:4]+"0"+func_input[4:]
    func_input=[int(x) for x in func_input]
    index=1
    while index<len(func_input):
        corrector=0
        counter=index
        decounter=0
        for jindex in range(index-1, len(func_input)):
            if decounter>0:
                decounter-=1
                continue
            corrector+=func_input[jindex]
            counter-=1
            if counter == 0:
                decounter=index
                counter=index
        func_input[index-1]=corrector%2
        index*=2
    return func_input


initial=input("\nВведите исходную информацию (8 битов)")
codeini=code(initial)
res=""
res=[str(x)+res for x in codeini]
out_str=""
print(f"\nИсходная веденная информация c контрольными битами 1, 2, 4 и 8: {out_str.join(res)}") 
werror=int(input("\nВведите искаженный разряд: "))-1
initial=str(initial)
errinit=""
for jindex in range(0,len(initial)):
    if jindex==werror:
        temp=str(abs(int(initial[jindex])-1))
        errinit+=temp
        continue
    errinit+=initial[jindex]
out_str="" 
print(f"\nИскаженная в разряде {werror+1} информация: {out_str.join(errinit)}") 
errinit=out_str.join(errinit)
codeerr=code(errinit)
#Начало восстановления
index=1
corrector=-1
while index<=len(codeini):
    if codeini[index-1]!=codeerr[index-1]:
        corrector+=index
    index=index*2
if corrector>-1:
    codeerr[corrector]=abs(codeerr[corrector]-1)
index=1
result=""
for jindex in range(0, len(codeerr)):
    if jindex==index-1:
        index*=2
        continue
    result=result+str(codeerr[jindex])
print(f"\nВосстановленная информация: {result}, корректор: {corrector+1}.")