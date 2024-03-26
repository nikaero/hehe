def sorting_hat():
  print("Hi! Welcome to Hogwarts School of Witchcraft and Wizardry")
  print("I'm your Sorting Hat, and I'm here to help you find your House")

  #####Q1
  print("Q1) Do you like Dawn or Dusk?")
  print("1) Dawn")
  print("2) Dusk")
  q1_ans = int(input("Enter your choice: "))

  Gryffindor_points = 0
  Ravenclaw_points = 0
  Hufflepuff_points = 0
  Slytherin_points = 0

  if q1_ans == 1:
    Gryffindor_points +=1
    Ravenclaw_points +=1
  elif q1_ans == 2:
    Hufflepuff_points += 1
    Slytherin_points += 1
  else:
    print("Wrong Input.")
    return

  ####Q2
  print("Q2) When I'm dead, I want people to remember me as: ")  
  print("1) The Good")
  print("2) The Great")
  print("3) The Wise")
  print("4) The Bold")
  q2_ans = int(input("Enter your choice: "))
  
  if q2_ans == 1:
    Hufflepuff_points +=2
  elif q2_ans == 2:
    Slytherin_points +=2
  elif q2_ans == 3:
    Ravenclaw_points +=2
  elif q2_ans == 4:
    Gryffindor_points +=2
  else:
    print("Wrong input.")
    return

  #####Q3
  print("Q3) Which kind of instrument most pleases your ear?")
  print("1) The Violin")
  print("2) The Trumpet")
  print("3) The Piano")
  print("4) The Drum")
  q3_ans = int(input("Enter your Choice: "))

  if q3_ans == 1:
    Slytherin_points += 4
  elif q3_ans == 2:
    Hufflepuff_points += 4
  elif q3_ans == 3:
    Ravenclaw_points += 4
  elif q3_ans == 4:
    Gryffindor_points += 4
  else:
    print("Wrong Input.")
    return

  houses = {
    "Gryffindor": Gryffindor_points,
    "Ravenclaw": Ravenclaw_points,
    "Hufflepuff": Hufflepuff_points,
    "Slytherin": Slytherin_points,
  }

  max_houses = max(houses, key=houses.get)
  print(f"Welcome to {max_houses}!")

if __name__ == "__main__":
  sorting_hat()
    
