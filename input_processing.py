# input_processing.py
# Riley Martel, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted
class SensorError(ValueError):
    pass
    

# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:
    # Contains 3 vars which are trafficlight, pedestrian and, vehicle
    # trafficlight can be "green", "red", and "yellow"
    # pedestrian can be "yes" or "no"
    # vehicle can be "yes" or "no"

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.trafficlight = "green"
        self.pedestrian = "no"
        self.vehicle = "no"
        self.quit = False
    

    # Replace these comments with your function commenting
    def update_status(self, update_in): # You may decide how to implement the arguments for this function
        
        value_correct = False
        while not value_correct:
            value = input("What change has been identified?: ")
            match update_in:
                case "1": #changing the trafficlight status
                    if value == "red" or value == "green" or value == "yellow":
                        value_correct = True
                        self.trafficlight = value
                    else:
                        print("\nInvalid status, please try again\n")
                case "2": #changing the pedestrian status
                    if value == "yes" or value == "no":
                        value_correct = True
                        self.pedestrian = value
                    else:
                        print("\nInvalid status, please try again\n")
                case "3": #changing the vehicle status
                    if value == "yes" or value == "no":
                        value_correct = True
                        self.vehicle = value
                    else:
                        print("\nInvalid status, please try again\n")
    
    def status(self):
        if self.pedestrian == "yes" or self.vehicle == "yes" or self.trafficlight == "red":
            return "\nSTOP"
        elif self.trafficlight == "green":
            return "\nProceed"
        elif self.trafficlight == "yellow":
            return "\nCaution"

        



# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    print("Are changes detected in the vision input?\n")
    error = True
    while error:
        value = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program:" )    
        try:
            if value == "0" or value == "1" or value == "2" or value == "3":
                error = False
                
            else:
                raise SensorError("[Inavlid menu item selection]")
        except SensorError:
            print("Inavlid menu item selection, please try again")
            error = True

    if value != "0":    
        sensor.update_status(value)
        print(sensor.status() + "\n")
    else:
        sensor.quit = True

    




# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    vision = Sensor()
    while not vision.quit:
        print_message(vision)





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

