def monitor():
  try:

    calc_levels = [380, 495, 410, 430, 445]

    current = get_calcium_level()
    mesg = "Calcium level OK"
    
    if (current < calc_levels[0]):
      mesg = "Calcium level too low!"
    elif (current > calc_levels[4]):
      mesg = "Calcium level  too high!"
    
  except:
    print("Unexpected error")

  return mesg
  
# Functiion to simulate actual fish tank monitoring
def get_calcium_level():
  return 420