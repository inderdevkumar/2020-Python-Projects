import os
import pandas as pd

log_files = os.listdir("log_files/")
for file in log_files:
    print("Log files you have are: ", file)

check = 1

def team_won():
    
    modified_content= content[:-2]
    
    list_team_player_point= []
    list_team= []
    list_player= []
    list_point= []
    
    for team_player_point in modified_content:
        
        final_team_player_point= team_player_point[:-1]
        team= final_team_player_point.split()[0]
        list_team.append(team)
        
        player= final_team_player_point.split()[1]
        list_player.append(player)
        
        point= final_team_player_point.split()[2]
        list_point.append(point)
                   
    list_team_player_point.append(list_team)
    list_team_player_point.append(list_player)
    list_team_player_point.append(list_point)
    
    df = pd.DataFrame(list_team_player_point).transpose()
    df.columns = ['Team_Name','Player_Name','Point']
    print(df)
    list_of_names = df['Player_Name'].to_list()

    
    team_frequenccy_df= df.groupby(['Team_Name']).size().reset_index(name='count')
    print(team_frequenccy_df)
    team_more_count= team_frequenccy_df['count'].max()
    team_won= team_frequenccy_df.loc[team_frequenccy_df['count'] == team_more_count, 'Team_Name'].iloc[0]
    
    print(f"{team_won} won!")

    Team1= team_frequenccy_df.iloc[0]["Team_Name"]
    scored1= team_frequenccy_df.iloc[0]["count"]
    Team2= team_frequenccy_df.iloc[1]["Team_Name"]
    scored2= team_frequenccy_df.iloc[1]["count"]

    statement1= f"{Team1} scored {scored1} points"
    statement2= f"{Team2} scored {scored2} points"
    print(statement1)
    print(statement2)

    print(f"{list_of_names[0]} scored first.")
    print(f"{list_of_names[len(list_of_names)-1]} scored last.")
    

while check:
    user_input= input("Please enter the correct log file name(Extension is required): " )
    if (user_input in log_files):
        
        path= f"log_files/{user_input}"

        file= open(path, "r")
            
        content = file.readlines()
        
        check = 0
        team_won()
    else:
        continue

 
