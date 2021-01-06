def monitor():
  mesg = ""
  try:
    max_val = 17
    min_val = 12

    current = get_alkalinity()
    mesg = "Alkalinity OK"

    if (current < min_val+1):
      mesg = "Alkalinity too low!"
    elif (current > max_val):
      mesg = "Alkalinity too high!"
    
  except:
    print("Unexpected error") 
    
  return mesg

# Function to simulate actual fish tank monitoring
def get_alkalinity():
  # return 9
  return 15
  # return 50