words = (input("Wpisz dowolną ilość słów: ")).split()

def licznik(x):
    print(x)
    print(sorted(x, key=len))
    for i in x:
        print(f"Słowo: {i}")
        print(f"Długość słowa: {len(i)}")
        
licznik(words)