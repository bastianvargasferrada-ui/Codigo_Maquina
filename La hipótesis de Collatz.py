


c0 = int(input("ingrese un número natural: "))

pasos = 0

while c0 <= 0:
    c0 = int(input("ingrese de nuevo el número: "))
else:
        while c0 != 1:
            if c0 % 2 == 0:
                c0 = c0//2
                pasos+=1
                print(c0)
            else:
                c0 = 3 * c0 + 1
                pasos+=1
                print(c0)



            


            

            
            
        

print("número de pasos: ", pasos)

            

        
         


        

        