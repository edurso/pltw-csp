def monitor():
  try:

    temps = [50, 55, 60, 65, 70, 75]

    mesg = "Temperature OK"

    # get multiple temperature readings
    temp_readings = get_temps()
    num_readings = 0

    # sum adds up all items in list
    ave_temp = sum(temp_readings)
    ave_temp = ave_temp / num_readings

    if (ave_temp < temps[0]):
      mesg = "Average temperature too cold!"
    elif (ave_temp > temps[5]):
      mesg = "Average temperature too warm!"
    
  except:
    print("Unexpected error")

  return mesg

# Function to simulate actual fish tank monitoring
def get_temps():
  return [65, 55, 70] 
