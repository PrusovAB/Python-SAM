
X = float(input("\nШирина отреза: "))
Y = float(input("\nДлина отреза: "))
M = float(input("\nПлотность ткани: "))
#M=g/(X*Y)
#print("\nПлотность ткани: % 9.2f." % M)
g=X*Y*M/10**5
print(" \nВес ткани:% 9.3f " % g)
