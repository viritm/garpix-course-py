
const_air_humidity = 80

desired_temperature = input("Enter the desired air temperature: ")
curr_temperature = input("Enter current air temperature: ")
curr_air_humidity = input("Enter current air humidity: ")

if int(curr_temperature) > int(desired_temperature) and int(curr_air_humidity) < int(const_air_humidity):
    print("on")
else:
    print("off")
