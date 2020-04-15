from textblob import TextBlob
import nltk  # Needed for a few TextBlob methods


def analyze_topics(sourcefile, floor=0):
  with open(sourcefile, 'r') as file:
    print("Reading file...\n")
    input = file.read().replace('\n', '').replace('.', ' ').replace(',', ' ')
    blob = TextBlob(input)
    output = blob.noun_phrases

    # Create and print tuples to chart
    returndata = []
    for term in set(output):
      termcount = output.count(term)
      if termcount > floor:
        returndata.append((term, termcount))
      else:
        pass
    return returndata

# These won't be downloaded unless they are missing.
nltk.download('brown')
nltk.download('punkt')

data = analyze_topics('topics.txt', 2)

with open('exportdata.csv', 'w') as output:
  for pair in data:
    output.write(f'{pair[0]},{pair[1]}\n')
