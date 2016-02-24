import os
import sys
import time
c_c = ""
wait_time = 0.015

try:
 rrf = open(sys.argv[1]).read()
except:
 print("Error.")
 exit()

bff = open("rrf_bf.bf","w")

for c in rrf:
 if c.lower() == "m" or c.lower() == "e" or c.lower() == "p":
  c_c = c_c + c
 if c_c == "MEEP":
  bff.write(".")
  print("Char was P. String complete.")
  print("Found MEEP, writing '.'...")
  time.sleep(wait_time)
  c_c = ""
 elif c_c == "meep":
  bff.write(",")
  print("Char was p. String complete.")
  print("Found meep, writing ','...")
  time.sleep(wait_time)
  c_c = ""
 elif c_c == "mEEP":
  bff.write("[")
  print("Char was P. String complete.")
  print("Found mEEP, writing '['...")
  time.sleep(wait_time)
  c_c = ""
 elif c_c == "MEEp":
  bff.write("]")
  print("Char was p. String complete.")
  print("Found MEEp, writing ']'...")
  c_c = ""
 elif c_c == "meeP":
  bff.write(">")
  print("Char was P. String complete.")
  print("Found meeP, writing '>'...")
  time.sleep(wait_time)
  c_c = ""
 elif c_c == "Meep":
  bff.write("<")
  print("Char was p. String complete.")
  print("Found Meep, writing '<'...")
  time.sleep(wait_time)
  c_c = ""
 elif c_c == "mEEp":
  bff.write("+")
  print("Char was P. String complete.")
  print("Found mEEp, writing '+'...")
  time.sleep(wait_time)
  c_c = ""
 elif c_c == "MeeP":
  bff.write("-")
  print("Char was p. String complete.")
  print("Found MeeP, writing '-'...")
  time.sleep(wait_time)
  c_c = ""
 else:
  if c.lower() == "m" or c.lower() == "e" or c.lower() == "p":
   print("Char was " + str(c) + ". Waiting for string completition...")
  elif c.lower() != "m" and c.lower() != "e" and c.lower() != "p" and c_c != "":
   print("Misspelled string. Aborting string completition.")
   c_c = ""
  elif c == " ":
   print("Skipping <SPACE>...")
  elif c == "\n":
   print("Skipping <ENTER>...")
  else:
   print("Skipping " + str(c) + "...")
  time.sleep(wait_time)
bff.close()
print("\nStarting Interpreter....")
print("\n++++++ INTERPRETER: ++++++\n")
try:
 os.system("python core/brfck-core.py rrf_bf.bf")
 os.remove("rrf_bf.bf")
except:
 print("I/O Error: The file has not been found")
