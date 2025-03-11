p = int(input("enter a number less than 25\n"))

if p < 25 :
    for i in range(p,26) :
        print(f"Inside the loop, my variable is {i}")
else :
    print("Ereor")