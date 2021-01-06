def monitor():
  mesg = ""
  try:
    temps = [50, 55, 60, 65, 70, 75]

    mesg = "Temperature OK"

    # get multiple temperature readings
    temp_readings = get_temps()
    num_readings = len(temp_readings)

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
  # return []
  # return [0, 0, 0, 0, 0]
  return [65, 55, 70] 
  # return [300, 300, 400, 500, 600, 700, 800, 900]
