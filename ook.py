import os
import sys
import time
c_c = ""
wait_time = 0.015

try:
 okf = open(sys.argv[1]).read()
except:
 print("Error.")
 exit()
bff = open("okf_bf.bf","w")


for c in okf:
 if c.lower() == "o" or c.lower() == "k" or c == "." or c == "?" or c == "!":
  c_c = c_c + c
 if c_c == "Ook!Ook.":
  bff.write(".")
  print("Command was Ook! Ook. String complete.")
  print("Found Ook! Ook., writing '.'...")
  time.sleep(wait_time)
  c_c = ""
 elif c_c == "Ook.Ook!":
  bff.write(",")
  print("Command was Ook. Ook! String complete.")
  print("Found Ook. Ook!, writing ','...")
  time.sleep(wait_time)
  c_c = ""
 elif c_c == "Ook!Ook?":
  bff.write("[")
  print("Command was Ook! Ook? String complete.")
  print("Found Ook! Ook?, writing '['...")
  time.sleep(wait_time)
  c_c = ""
 elif c_c == "Ook?Ook!":
  bff.write("]")
  print("Command was Ook? Ook! String complete.")
  print("Found Ook? Ook!, writing ']'...")
  c_c = ""
 elif c_c == "Ook.Ook?":
  bff.write(">")
  print("Command was Ook. Ook? String complete.")
  print("Found Ook. Ook?, writing '>'...")
  time.sleep(wait_time)
  c_c = ""
 elif c_c == "Ook?Ook.":
  bff.write("<")
  print("Command was Ook? Ook. String complete.")
  print("Found Meep, writing '<'...")
  time.sleep(wait_time)
  c_c = ""
 elif c_c == "Ook.Ook.":
  bff.write("+")
  print("Command was Ook. Ook. String complete.")
  print("Found Ook. Ook., writing '+'...")
  time.sleep(wait_time)
  c_c = ""
 elif c_c == "Ook!Ook!":
  bff.write("-")
  print("Command was Ook! Ook! String complete.")
  print("Found Ook! Ook!, writing '-'...")
  time.sleep(wait_time)
  c_c = ""
 else:
  if c == "." or c == "?" or c == "!" or c.lower == "o" or c.lower == "k":
   print("Part was Ook" + str(c) + ". Waiting for string completition...")
  elif c.lower() != "o" and c.lower() != "k" and c != "!" and c.lower() != "?" and c.lower != "." and c != " " and c_c != "":
   print("Misspelled command. Aborting command completition.")
#   c_c = ""
  elif c == " ":
   print("Skipping <SPACE>...")
  elif c == "\n":
   print("Skipping <ENTER>...")
  elif c.lower() == "o" or c.lower() == "k":
   print("Recognized " + str(c))
  else:
   print("Skipping " + str(c) + "...")
  time.sleep(wait_time)
bff.close()
print("\nStarting Interpreter....")
print("\n++++++ INTERPRETER: ++++++\n")
try:
 os.system("python core/brfck-core.py okf_bf.bf")
 os.remove("okf_bf.bf")
except:
 print("I/O Error: The file has not been found")
