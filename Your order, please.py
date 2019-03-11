def order(sentence):
  wentence=sentence.split()
  dicty={}
  for i in range(len(wentence)+1):
      for j in wentence:
          if str(i) in j:
              dicty[i]=j
  wentence=[dicty[i] for i in dicty]
  return ' '.join(wentence)