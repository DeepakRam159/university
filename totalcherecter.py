filename = '1.txt'
file = open("1.txt",'r')
content = file.read()


print(content)
total_characters = len(content)
print(f"Total numbers of characters:{total_characters}")
file.close()
