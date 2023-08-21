l1=[1,2,3,4,5]
l2=["21","erqawd","earth","3123",31]

print(l1)
print(l2)

l2[0]=l1[0]

print(l2)

if "earth" in l2:
    print("YES")



word=input("-> ")
find=input("find:")
letters=[]

for i in range(len(word)):
    try:
        letters.append(word.index(find,i,i+1))
    except:
        pass



print(letters)
# thinking= "hmmok"
# try:
#     print(thinking.index("m"))
# except:
#     pass
#
