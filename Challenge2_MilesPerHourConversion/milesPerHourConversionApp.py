print("Welcome to the MPH to MPS Conversion App/n")
speedInMiles = float(input("What is your speed in miles per hour: ").strip())

speedInMetersPerSec = speedInMiles * 0.4474

print("Your speed in meters per second is", round(speedInMetersPerSec, 2) )
