'''QUESTION - 7'''

'''Write a Python program that checks login attempts using the following sequence of PIN entries: [1111, 2222, 1234]. The correct PIN is 1234. Allow maximum 3 attempts. Stop the loop immediately when the correct PIN is entered using break. If all attempts are incorrect, display "Account Locked".'''

PIN_entries = list(map(int,input().split()))
correct_PIN = int(input())
maximum_attempts = int(input())
for i in range (maximum_attempts):
    entered_pin = PIN_entries [i]
    entries=i+1
    print("Attempt:", entries)

    if entered_pin == correct_PIN :
      print("Login Successful")
      break

    if entered_pin!= correct_PIN :
      print("Wrong PIN")
      continue
else:
   print("Account Locked")


