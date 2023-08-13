import json
from datetime import datetime

class InstanceUpdate:
    def __init__(self) -> None:
        duration_seconds = int(input("Enter the number of seconds you smoked: "))
        self.add_smoking_instance(duration_seconds)
        print("Smoking instance added!")

    def add_smoking_instance(self,duration_seconds):
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M")
        
        # Load existing JSON data from file
        with open('instances.json', 'r') as file:
            data = json.load(file)
        
        if current_date in data["smoking_instances"]:
            data["smoking_instances"][current_date].append({
                "time": current_time,
                "duration_seconds": duration_seconds
            })
        else:
            data["smoking_instances"][current_date] = [{
                "time": current_time,
                "duration_seconds": duration_seconds
            }]
        
        # Write updated JSON back to the file
        with open('instances.json', 'w') as file:
            json.dump(data, file, indent=4)

        

if __name__ == "__main__":
    InstanceUpdate()
    