try:
    file = open("sample.txt" , 'r')
    line1 = file.readline()
    print("Reading file content:")
    print("Line 1:",line1)
    line2 = file.readline()
    print("Line 2:",line2)
    file.close()
    
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
