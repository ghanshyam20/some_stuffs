try:
    file=open("random23.txt","r")
    print(file.read())
    file.close()


except FileNotFoundError:
    print("Error:File not found sorry user")
    
