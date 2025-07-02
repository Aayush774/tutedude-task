data1 = input("Enter text to write to the file:")
file = open("Output.txt","w")
file.write(data1)
print("Data successfully written to output.txt.\n")
file.close()

data2 = input("Enter additional text to append:")
file = open("Output.txt",'a')
file.write("\n")
file.write(data2)
print("Data successfully appended.")
file.close()

print("\nFinal content of output.txt:")

data3 = open("Output.txt", 'r')
content = data3.read()
print(content)
data3.close()

