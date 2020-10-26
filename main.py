print(' You have 10 guesses to guess the Secret Number')
secretNumber = 127
for i in range(10):
  try:
    userInput = int(input('Guess the Secret Number: '))
  except ValueError:
    print('Not A Valid Entry! ')
  if userInput == secretNumber:
    print('I am out of the loop ')
    print('You guessed correctly ')
    break
  if userInput < secretNumber:
    print('Guess Higher ')
  if userInput > secretNumber:
    print('Guess Lower ')
  if i == 9:
    print('You Are Out Of Guesses!!! ')