import requests
class IRCTC:

    __api_key = "b198123f3727b9d622d6382283be9c4f"
    

    def __init__(self):
        user_input = input(
        """
        How do you like to proceed?
        1. Press 1 for Train Scheduleing """)

        if user_input == "1":
            self.train_schedule()
            
    
    def train_schedule(self):
        train_number = input("Enter Train Number: ")
        self.fetch_data(train_number)

    def fetch_data(self, train_number):
        base_url = "http://indianrailapi.com/api/v2/TrainSchedule/apikey/{}/TrainNumber/{}/".format(IRCTC.__api_key, train_number)
        # print(base_url)
        data = requests.get(base_url)

        data = data.json()
        
        for train in data["Route"]:
            print("{} | {} | {} | {} | {} | {} kms".format(train["SerialNo"], train["StationCode"], train["StationName"], train["ArrivalTime"], train["DepartureTime"], train["Distance"]))

t1 = IRCTC()
