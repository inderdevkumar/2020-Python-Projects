import numpy as np  #pip install numpy
import matplotlib.pyplot as plt   #pip install matplotlib


data = [
    {
        "state": "Alabama",
        "Capital": "Montgomery",
        "State Flower": "Camellia",
        "population": 4908620
    },
    {
        "state": "Alaska",
        "Capital": "Juneau",
        "State Flower": "Forget Me Not",
        "population": 734002
    },
    {
        "state": "Arizona",
        "Capital": "Phoenix",
        "State Flower": "Saguaro Cactus Blossom",
        "population": 7378490
    },
    {
        "state": "Arkansas",
        "Capital": "Little Rock",
        "State Flower": "Apple Blossom",
        "population": 3039000
    },
    {
        "state": "California",
        "Capital": "Sacramento",
        "State Flower": "California Poppy",
        "population": 39937500
    },
    {
        "state": "Colorado",
        "Capital": "Denver",
        "State Flower": "White and Lavender Columbine",
        "population": 5845530
    },
    {
        "state": "Connecticut",
        "Capital": "Hartford",
        "State Flower": "Mountain Laurel",
        "population": 3563080
    },
    {
        "state": "Delaware",
        "Capital": "Dover",
        "State Flower": "Peach Blossom",
        "population": 982895
    },
    {
        "state": "Florida",
        "Capital": "Tallahassee",
        "State Flower": "Orange Blossom",
        "population": 21993000
    },
    {
        "state": "Georgia",
        "Capital": "Atlanta",
        "State Flower": "Cherokee Rose",
        "population": 10736100
    },
    {
        "state": "Hawaii",
        "Capital": "Honolulu",
        "State Flower": "Hibiscus",
        "population": 1412690
    },
    {
        "state": "Idaho",
        "Capital": "Boise",
        "State Flower": "Syringa",
        "population": 1826160
    },
    {
        "state": "Illinois",
        "Capital": "Springfield",
        "State Flower": "Purple Violet",
        "population": 12659700
    },
    {
        "state": "Indiana",
        "Capital": "Indianapolis",
        "State Flower": "Peony",
        "population": 6745350
    },
    {
        "state": "Iowa",
        "Capital": "Des Moines",
        "State Flower": "Wild Prairie Rose",
        "population": 3179850
    },
    {
        "state": "Kansas",
        "Capital": "Topeka",
        "State Flower": "Sunflower",
        "population": 2910360
    },
    {
        "state": "Kentucky",
        "Capital": "Frankfort",
        "State Flower": "Goldenrod",
        "population": 4499690
    },
    {
        "state": "Louisiana",
        "Capital": "Baton Rouge",
        "State Flower": "Magnolia",
        "population": 4645180
    },
    {
        "state": "Maine",
        "Capital": "Augusta",
        "State Flower": "White Pine Cone and Tassel",
        "population": 1345790
    },
    {
        "state": "Maryland",
        "Capital": "Annapolis",
        "State Flower": "Black-Eyed Susan",
        "population": 6083120
    },
    {
        "state": "Massachusetts",
        "Capital": "Boston",
        "State Flower": "Mayflower",
        "population": 6976600
    },
    {
        "state": "Michigan",
        "Capital": "Lansing",
        "State Flower": "Apple Blossom",
        "population": 10045000
    },
    {
        "state": "Minnesota",
        "Capital": "Saint Paul",
        "State Flower": "Pink and White Lady Slipper",
        "population": 5700670
    },
    {
        "state": "Mississippi",
        "Capital": "Jackson",
        "State Flower": "Magnolia",
        "population": 2989260
    },
    {
        "state": "Missouri",
        "Capital": "Jefferson City",
        "State Flower": "White Hawthorn Blossom",
        "population": 6169270
    },
    {
        "state": "Montana",
        "Capital": "Helena",
        "State Flower": "Bitterroot",
        "population": 1086760
    },
    {
        "state": "Nebraska",
        "Capital": "Lincoln",
        "State Flower": "Goldenrod",
        "population": 1952570
    },
    {
        "state": "Nevada",
        "Capital": "Carson City",
        "State Flower": "Sagebrush",
        "population": 3139660
    },
    {
        "state": "New Hampshire",
        "Capital": "Concord",
        "State Flower": "Purple Lilac",
        "population": 1371250
    },
    {
        "state": "New Jersey",
        "Capital": "Trenton",
        "State Flower": "Violet",
        "population": 8936570
    },
    {
        "state": "New Mexico",
        "Capital": "Santa Fe",
        "State Flower": "Yucca Flower",
        "population": 2096640
    },
    {
        "state": "New York",
        "Capital": "Albany",
        "State Flower": "Rose",
        "population": 19440500
    },
    {
        "state": "North Carolina",
        "Capital": "Raleigh",
        "State Flower": "Dogwood",
        "population": 10611900
    },
    {
        "state": "Ohio",
        "Capital": "Columbus",
        "State Flower": "Scarlet Carnation",
        "population": 11747700
    },
    {
        "state": "Oklahoma",
        "Capital": "Oklahoma City",
        "State Flower": "Mistletoe",
        "population": 3954820
    },
    {
        "state": "Oregon",
        "Capital": "Salem",
        "State Flower": "Oregon Grape",
        "population": 4301090
    },
    {
        "state": "Pennsylvania",
        "Capital": "Harrisburg",
        "State Flower": "Mountain Laurel",
        "population": 12820900
    },
    {
        "state": "Rhode Island",
        "Capital": "Providence",
        "State Flower": "Violet",
        "population": 1056160
    },
    {
        "state": "South Carolina",
        "Capital": "Columbia",
        "State Flower": "Yellow Jessamine",
        "population": 5210100
    },
    {
        "state": "North Dakota",
        "Capital": "Bismarck",
        "State Flower": "Wild Prairie Rose",
        "population": 761723
    },
    {
        "state": "South Dakota",
        "Capital": "Pierre",
        "State Flower": "Pasque Flower",
        "population": 903027
    },
    {
        "state": "Tennessee",
        "Capital": "Nashville",
        "State Flower": "Iris",
        "population": 6897580
    },
    {
        "state": "Texas",
        "Capital": "Austin",
        "State Flower": "Bluebonnet",
        "population": 29472300
    },
    {
        "state": "Utah",
        "Capital": "Salt Lake City",
        "State Flower": "Sego Lily",
        "population": 3282120
    },
    {
        "state": "Tennessee",
        "Capital": "Nashville",
        "State Flower": "Iris",
        "population": 6897580
    },
    {
        "state": "Vermont",
        "Capital": "Montpelier",
        "State Flower": "Red Clover",
        "population": 628061
    },
    {
        "state": "Virginia",
        "Capital": "Richmond",
        "State Flower": "Dogwood",
        "population": 8626210
    },
    {
        "state": "Washington",
        "Capital": "Olympia",
        "State Flower": "Pink Rhododendron",
        "population": 7797100
    },
    {
        "state": "West Virginia",
        "Capital": "Charleston",
        "State Flower": "Rhododendron",
        "population": 1778070
    },
    {
        "state": "Wisconsin",
        "Capital": "Madison",
        "State Flower": "Wood Violet",
        "population": 5851750
    },
    {
        "state": "Wyoming",
        "Capital": "Cheyenne",
        "State Flower": "Indian Paintbrush",
        "population": 567025
    }
]



def showOptions():
    print("1. Display all states and it's data Alphabetically")
    print("2. Search for a specific state")
    print("3. Show Bar graph of top 5 states with highest population")
    print("4. Update overall population of specific state")
    print("5. Exit the program")



while True:
    showOptions()
    inp = int(input("Choose an option: "))


    if inp == 1:
        for state in data:
            for j in state:
                print(j + ":", state[j])
            print()
    else:
        if inp == 2:
            search = input("Enter the state you want to search: ")
            for state in data:
                if state["state"] == search:
                    for j in state:
                        print(j + ":", state[j])
                    print()
                    break
        else:
            if inp == 3:
                sorted_states = sorted(
                    data, key=lambda i: i['population'], reverse=True)
                fig = plt.figure(figsize=(10, 5))


                sorted_states_names = []
                sorted_states_populations = []


                for x in sorted_states[:5]:
                    sorted_states_names.append(x["state"])
                    sorted_states_populations.append(x["population"])


                # creating the bar plot
                plt.bar(sorted_states_names, sorted_states_populations,
                        width=0.4)
                plt.show()
            else:
                if inp == 4:
                    states_populations= 0
                    state_to_be_modified = input(
                        "Enter the state you want to update the population for: ")
                    population = int(
                        input("Enter the population you want to increase: "))
                    for state in data:
                        if state["state"] == state_to_be_modified:
                            state["population"] += population
                            states_populations= state["population"]
                            break
                    plt.bar(state_to_be_modified, states_populations,
                        width=0.4)
                    plt.show()
                else:
                    if inp == 5:
                        print("Thanks for using the program")
                        exit(0)


                    else:
                        print("Invalid choice. Please try again")
