# modifier 'w' overwrite a file
file_write = open('words-write.txt', 'w')

file_write.write('banana\n')
file_write.write('melancia\n')

file_write.close()

# modifier 'a' append content to a file
fileAppend = open('words-append.txt', 'a')

fileAppend.write('banana\n')
fileAppend.write('melancia\n')

fileAppend.close()

# modifier 'r' read a file
file_write = open('words-write.txt', 'r')
fileAppend = open('words-append.txt', 'r')

# read all file
print(file_write.read())
print(fileAppend.read())

# read one line of the file
print(file_write.readline())
print(fileAppend.readline())
