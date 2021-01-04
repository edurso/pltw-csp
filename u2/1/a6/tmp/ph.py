def monitor():
  try:
    
    ph_levels = [8.1, 8.2, 8.3]

    current = get_ph_level()
    mesg = "pH level OK"

    if (current < ph_levels[0]):
      mesg = "pH level too low!"
    elif (current > ph_levels[2]):
      mesg = "pH level too high!"
    
  except:
    print("Unexpected error")
    
  return mesg

# Functiion to simulate actual fish tank monitoring
def get_ph_level():
  return 8.2