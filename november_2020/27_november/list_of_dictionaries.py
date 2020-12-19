from operator import itemgetter


# To get list of company names
def get_company_names(list_of_dict):
    
    company_names = [ sub['Company Name'] for sub in list_of_dict ] #getting list of company name
    print("List of Company Names are: ", company_names)

#To get Dictionary of Country
def get_countries(list_of_dict):
    
    countries = [ sub['Country'] for sub in list_of_dict ] #getting list of Country name
    unique = [] 
    for item in countries: 
        if item not in unique: 
            unique.append(item) #Getting list of all unique country names
    countries_dict = { i : (unique.index(i)+1) for i in unique }  #Making dictionary from list
    print("Dictionary of Countries are: ", countries_dict)
    
#To get company names with location like city and Country given
def get_companies(location, list_of_dict):
    
    city_names = [ sub['City'] for sub in list_of_dict]  #getting list of City name
    country_names = [ sub['Country'] for sub in list_of_dict]  #getting list of Country name
    
    if ((location.get("City") in  city_names) and (location.get("Country") in  country_names)):  #Checking the condition with City and Country 
        res = [d for d in list_of_dict if d['City'] == location.get("City")]  #getting list of dictionary with condition applied
        
        company_names = [ sub['Company Name'] for sub in res ]  #Getting list of Company name
        print("List of company names with condition applied: ", company_names)
    else:
        print("None")
    

list_of_dict= [
    {
        "Company Name": "Roshan",
        "Company Moto": "Roshgan Begin Operation...",
        "City": "Kabul",
        "Country": "Afghanistan",
        "Contact": {
            "Phone Number": "+93 79 997 1333",
            "Email": "roshanca@roshna.af",
            "website": "http://www.roshan.af/"
            },
        "Social Account": {
            "Facebook": "https://www.facebook.com",
            "Twitter": "https://www.twitter.com",
            "Linkedin": "https://www.linkedin.com"
            }
        
        },
    {
        "Company Name": "Gjirafe",
        "Company Moto": "Roshgan Begin Operation...",
        "City": "Tirane",
        "Country": "Albania",
        "Contact": {
            "Phone Number": "+93 79 997 1333",
            "Email": "roshanca@roshna.af",
            "website": "http://www.roshan.af/"
            },
        "Social Account": {
            "Facebook": "https://www.facebook.com",
            "Twitter": "https://www.twitter.com",
            "Linkedin": "https://www.linkedin.com"
            }
        },
    {
        "Company Name": "Shqiperia com",
        "Company Moto": "Roshgan Begin Operation...",
        "City": "Tirane",
        "Country": "Albania",
        "Contact": {
            "Phone Number": "+93 79 997 1333",
            "Email": "roshanca@roshna.af",
            "website": "http://www.roshan.af/"
            },
        "Social Account": {
            "Facebook": "https://www.facebook.com",
            "Twitter": "https://www.twitter.com",
            "Linkedin": "https://www.linkedin.com"
            }
        }
]
get_company_names(list_of_dict)
get_countries(list_of_dict)

location= {"City": "Tirane", "Country": "Albania"}
get_companies(location, list_of_dict)
