import random
import string

print("\nCoded By DiscordShit on Nulled.to!\n")

times = int(input("How many codes do you want to generate?: "))

file = open("codes.txt","w")

for i in range(times):
	codes = ''.join(random.sample((string.ascii_lowercase+string.ascii_uppercase+string.digits),16))
	file.write(codes)
	file.write("\n")
print("\nFinished! Make sure to like my thread :) - If you have issues with the program writing to the codes.txt file, you need to cd to the directory this python file is in. Example: C:/Users/Hackerman/Desktop/NitroGenerator/")
