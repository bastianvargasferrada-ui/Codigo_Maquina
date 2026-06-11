beatles = []
beatles.append("John Lennon")
print(beatles)
beatles.append("Paul McCartney")
print(beatles)
beatles.append("George Harrison")
print(beatles)

for i in range(2):
    beatles.append(input("ingrese a los 2 miembros restantes: "))
    print(beatles)
del beatles[3]
print(beatles)
del beatles[3]
print(beatles)
beatles.insert(0,"ringo star")
print(beatles)

print("los favoritos son:", len(beatles))