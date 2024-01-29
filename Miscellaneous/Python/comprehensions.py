lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,0]

def main():
    dictionary = {
        key:value for (key, value) in zip(lst1, lst2)
    }
    print(dictionary)

    lst = [i**(-1) for i in range(1,10)]
    print(lst)

    lst = [int(i) for i in range(1,10) if i in lst1 and i % 2 == 0]
    print(lst)

    lst = [[i,j] for i in range(10) for j in range(5) if i % 2 == 0 and j % 2 == 1]
    print(lst)

    lst = [[[i,j],[j,g]] for i in range(5) for j in range(5) for g in range(3)]
    print(lst)

if __name__ == "__main__":
    main()


    
    
    

