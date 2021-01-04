def monitor():
  try:

    val1 = 1250
    val2 = 1350

    mag_levels = list(range(val1, val2, 10))

    current = get_magnesium_level()
    mesg = "Magnesium level OK"

    num_levels = len(mag_levels)
    if (current < mag_levels[0]):
      mesg = "Magnesium level too low!"
    elif (current > mag_levels[num_levels]):
      mesg = "Magnesium level too high!"
    
  except:
    print("Unexpected error")

  return mesg

# Function to simulate actual fish tank monitoring
def get_magnesium_level():
  return 1300
