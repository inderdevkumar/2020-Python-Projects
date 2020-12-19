import pandas as pd

candidate_df= pd.read_csv("HR Response.txt")
candidate_response_list = candidate_df.values.tolist()
candidate_response_dict= candidate_df.set_index('Candidate').T.to_dict('list')
print(candidate_response_dict)
answer_values= candidate_response_dict.values()

desired_df= pd.read_csv("Desired_response.txt")
desired_response_list = desired_df.values.tolist()
desired_output_list= desired_response_list[0][1:]
#desired_response_dict= desired_df.set_index('Response').T.to_dict('list')
print(desired_output_list)

count= 0
#for candidate, answer in candidate_response_dict.items():  
for ans in answer_values:
    print(ans)
    for desired_ans in desired_output_list:
        if ans == desired_ans:
            count= count + 1
            
    print(f"{candidate_response_dict.keys()} has total desired response {count} ")
