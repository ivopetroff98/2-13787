
#y(x)=a*x**2+b*x+c=0
#D=b**2-4*a*c
#if D>=0 -> produljava
#if D<0 -> izvejda nqma rehsnie
#x1=(-b+sqrt(b**2-4*a*c))/(2*a)
#x2=(-b-sqrt(b**2-4*a*c))/(2*a)
#izvejda korenite
#float(input("vuvedete a: "))
#float(input("vuvedete b: "))
#float(input("vuvedete c: "))

from math import sqrt
print("y(x)=a*x^2+b*x+c")
a=[x for x in range(1,10)]
b=[x for x in range(1,10)]
c=[x for x in range(1,10)]
print ("y(x)=",a,"x**2+",b,"*x+",c)
result_nrr=[]
result=[]
def koreni(a,b,c):
    D=b**2-4*a*c
    if D<0:
        result_nrr.append([a,b,c])
    else:
        result.append([a,b,c,round((-b + sqrt(D)) / (2 * a),2),round((-b - sqrt(D)) / (2 * a),2)])

    return result


for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
          koreni(i,j,k)
print("Pri slednite parametri, nqma realni koreni:")
for ii in range(0,len(result_nrr)):
    print(result_nrr[ii])
print("Pri slednite parametri, ima realni koreni:")
for jj in range(0,len(result)):
    print(result[jj])

f= open("NRR.txt","w+")
for i in range(0,len(result_nrr)):
     f.write(str(result_nrr[i])+"\n")
f.close()
f= open("RR.txt","w+")
for i in range(0,len(result)):
     f.write(str(result[i])+"\n")
f.close()