password = 26**8 # all lower case
time = password / 100e9 #1 billion hashes per second
print (f'{time} secs')

password = 52**8 # all lower case and upper case
time = password / 100e9 #1 billion hashes per second
print (f'{time/60} mins')

password = 62**8 # all lower case and upper case and !"£$%^&*()"
time = password / 100e9 #1 billion hashes per second
print (f'{time/60} mins')

password = 72**8 # all lower case and upper case and !"£$%^&*()"@:~#';/?
time = password / 100e9 #1 billion hashes per second
print (f'{time/60} mins')

