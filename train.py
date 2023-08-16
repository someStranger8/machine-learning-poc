
# imports
from sys import argv as params
import json
import random


# main function
def main():
  if "-m" in params:
    word = input("[*] Enter word: ")
    state = input("[*] Is the word good or bad (1/0)? ")
    percent = input("[*] Enter percent to train to: ")
    state = int(state)

    with open("model.json", "r") as f:
      model = json.loads(f.read())

    if word not in model:
      model[word] = []

      for i in range(100):
        model[word].append(1)
        model[word].append(0)

    while 1:
      for i in range(100):
        choice = random.choice(model[word])

        if choice == state:
          model[word].append(state)

        else:
          if choice not in model[word]:
            pass

          else:
            model[word].pop(model[word].index(choice))

        print("Accuracy: ", (model[word].count(state)/len(model[word]))*100,"%")

      if (model[word].count(state)/len(model[word]))*100 > int(percent):
        break

    with open("model.json", "w") as f:
      f.write(json.dumps(model))

  elif params[1] == "-f":
    with open(params[2], "r") as f:
      data = json.loads(f.read())

    percent = data["percent"]

    for word in data["data"].keys():
      state = data["data"][word]

      with open("model.json", "r") as f:
        model = json.loads(f.read())

      if word not in model:
        model[word] = []

        for i in range(100):
	        model[word].append(1)
	        model[word].append(0)

      while 1:
        for i in range(100):
          choice = random.choice(model[word])
					
          if choice == state:
						model[word].append(state)

					else:
						if choice not in model[word]:
							pass

						else:
							model[word].pop(model[word].index(choice))

	  		print("Accuracy: ", (model[word].count(state)/len(model[word]))*100,"%")

        if (model[word].count(state)/len(model[word]))*100 > int(percent):
          break

      with open("model.json", "w") as f:
        f.write(json.dumps(model))


  else:
    print("""
    Use -m for manual mode
    Use -f for a file
    """)

# run main func
if __name__ == "__main__":
  main()
