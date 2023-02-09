vecorig_y=[]
vecorig_x=[]


print('\nВведите количество точек:')
length=round(int(input()))


for index in range(0, length):
    print('\nВведите индекс точки №'+str(index+1)+':')
    vecorig_x.append(int(input()))
    print('\nВведите значение точки №'+str(index+1)+':')
    vecorig_y.append(round(float(input()), 4))
    

index=0
lines=[]
for point in vecorig_x:
    line=''.join(str(vecorig_x[index]))
    line+=' '
    line+=''.join(str(vecorig_y[index]))
    lines.append(line)
    index+=1
with open('input.txt', 'w') as ipntsfile:
    ipntsfile.write('\n'.join(lines))
ipntsfile.close


print('\nВведите апертуру:')
apperture=round(float(input()), 4)


print('\nМассив до сжатия:\n'+str(vecorig_x)+'\n'+str(vecorig_y))


veccomp_y=[]
veccomp_x=[]

#сжатие
veccomp_x.append(vecorig_x[0])
veccomp_y.append(vecorig_y[0])
for index in range(0, length-2):
    for jindex in range(index+1, length-1):
        check=float((vecorig_x[jindex]-vecorig_x[index])*(vecorig_y[jindex+1]-vecorig_y[index])/(vecorig_x[jindex+1]-vecorig_x[index]))
        check+=vecorig_y[index]
        if abs(vecorig_y[jindex]-check)>=apperture:
            if not vecorig_x[jindex] in veccomp_x:
                veccomp_x.append(vecorig_x[jindex])
                veccomp_y.append(vecorig_y[jindex])
            index=jindex-1
            break
veccomp_x.append(vecorig_x[-1])
veccomp_y.append(vecorig_y[-1])

#сортировка так как алгоритм может перепутать порядок
length=len(veccomp_x)
for index in range(0, length-1):
    if veccomp_x[index] > veccomp_x[index+1]:
        veccomp_x[index], veccomp_x[index+1] = veccomp_x[index+1], veccomp_x[index]
        veccomp_y[index], veccomp_y[index+1] = veccomp_y[index+1], veccomp_y[index]


print('\nМассив после сжатия:\n'+str(veccomp_x)+'\n'+str(veccomp_y))


index=0
lines=[]
for point in veccomp_x:
    line=''.join(str(veccomp_x[index]))
    line+=' '
    line+=''.join(str(veccomp_y[index]))
    lines.append(line)
    index+=1


with open('cpoints.txt', 'w') as cpntsfile:
    cpntsfile.write('\n'.join(lines))


cpntsfile.close

#восстановление
length=len(veccomp_x)
vecrec_x=[veccomp_x[0]]
vecrec_y=[veccomp_y[0]]
for index in range(0, length-1):
    jindex=index+1
    if(veccomp_x[jindex]-veccomp_x[index]>1):
        for zindex in range(1, veccomp_x[jindex]-veccomp_x[index]):
            y = veccomp_y[index]+(zindex*(veccomp_y[jindex]-veccomp_y[index])/(veccomp_x[jindex]-veccomp_x[index]))
            vecrec_x.append(veccomp_x[index]+zindex)
            vecrec_y.append(round(y, 4))
    vecrec_x.append(veccomp_x[jindex])
    vecrec_y.append(veccomp_y[jindex])


print('\nМассив после востановления:\n'+str(vecrec_x)+'\n'+str(vecrec_y))


index=0
lines=[]
for point in vecrec_x:
    line=''.join(str(vecrec_x[index]))
    line+=' '
    line+=''.join(str(vecrec_y[index]))
    lines.append(line)
    index+=1


with open('rpoints.txt', 'w') as rpntsfile:
    rpntsfile.write('\n'.join(lines))
rpntsfile.close