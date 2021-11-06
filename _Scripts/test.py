lyst = []
num = len(lyst)//2
print(num)
l_lyst = lyst[:num]
r_lyst = lyst[num:]
if not r_lyst:
    print("yes")
print(f"l lyst {l_lyst} \n r lyst {r_lyst}")