import random

def primary():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  for x in range(3):
    rnd= random.randint(0, last)
    print(quotes[rnd], end = '')

if __name__== "__main__":
  primary()
