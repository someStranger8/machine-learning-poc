
# imports
import json
import random
from sys import argv as params

def load():
  global model

  with open("model.json", "r") as f:
    model = json.loads(f.read())

def main():
  if params[1] == "-f":
    pass

  elif params[1] == "-s":
    print("Type quit, exit, or q to quit")

    while 1:
      l = 0
      s = input("[*] Enter a word, phrase or setence: ")

      if s in ["quit","exit","q"]:
        break

      else:
        for i in model:
          if i in s:
            choice = random.choice(model[i])

            if choice:
              l+=1

            else:
              l-=1

        if l > 0:
          print("good")

        elif l < 0:
          print("bad")

        else:
          print("neutral")

  else:
    print("""
    Use -s for shell mode
    Use -f to read a file
    """)


if __name__ == "__main__":
  load()
  main()
