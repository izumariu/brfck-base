import os
import sys
import time

wait_time = 0.015

if len(sys.argv) == 0:
 print("Usage: ./l33t.py <file>")
 exit()
try:
 leetf = open(sys.argv[1]).read()
except:
 print("Error.")
 exit()

bff = open("l33t_bf.bf","w")

for c in leetf:
 if c == "1":
  bff.write(".")
  print("Found 1, writing '.'...")
  time.sleep(wait_time)
 elif c == "2":
  bff.write(",")
  print("Found 2, writing ','...")
  time.sleep(wait_time)
 elif c == "3":
  bff.write("[")
  print("Found 3, writing '['...")
  time.sleep(wait_time)
 elif c == "4":
  bff.write("]")
  print("Found 3, writing ']'...")
 elif c == "5":
  bff.write(">")
  print("Found 3, writing '>'...")
  time.sleep(wait_time)
 elif c == "6":
  bff.write("<")
  print("Found 3, writing '<'...")
  time.sleep(wait_time)
 elif c == "7":
  bff.write("+")
  print("Found 3, writing '+'...")
  time.sleep(wait_time)
 elif c == "8":
  bff.write("-")
  print("Found 3, writing '-'...")
  time.sleep(wait_time)
 else:
  print("Skipping " + str(c) + "...")
  time.sleep(wait_time)

bff.close()
print("\nStarting Interpreter....\n")
print("\n++++++ INTERPRETER: ++++++\n")
os.system("python core/brfck-core.py l33t_bf.bf")
os.remove("l33t_bf.bf")
