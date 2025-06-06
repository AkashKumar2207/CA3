

import random
import time
def temperature_monitor(lower_limit, upper_limit):
  """
  Monitors the temperature and provides alerts if it goes below the lower limit or above the upper limit.

  Args:
    lower_limit: The lower limit of the temperature.
    upper_limit: The upper limit of the temperature.
  """
  while True:
    temperature = random.randint(lower_limit - 10, upper_limit + 10)
    print(f"Current temperature: {temperature}°C")

    if temperature < lower_limit:
      print("Alert: Temperature is below the lower limit!")
    elif temperature > upper_limit:
      print("Alert: Temperature is above the upper limit!")

    time.sleep(2)


if __name__ == "__main__":
  lower_limit = int(input("Enter the lower temperature limit: "))
  upper_limit = int(input("Enter the upper temperature limit: "))

  temperature_monitor(lower_limit, upper_limit)

