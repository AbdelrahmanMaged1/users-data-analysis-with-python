import requests
import json
import pandas as pd

total= 0
skip= 0
limit= 26 
dfs_list= []
page= 0

while True:
    # I intentionally paginated with limit= 26 
    url = f'https://dummyjson.com/users?limit={limit}&skip={skip}'
    response= requests.get(url)

    # reading users data as dicts/objects
    data= response.json()['users']

    # appending data to dfs_list as pandas dataframe to combine them later into one dataframe using concat()
    dfs_list.append(pd.DataFrame(data))

    # updating the total & skip variables to get the next page/batch of data
    total = response.json()['total']
    skip += limit 

    # break condition to break the loop when we reach the end (skip = total) after reading all the data
    if skip >= total:
        break
    # every 26 users/dicts (limit value) we read is considered as one page
    print(page)
    page+=1

# combining all the dataframes we've read into one df using concat()
users= pd.concat(dfs_list)

print(users)

# saving the data as a csv file
users.to_csv('users.csv', index= False)

print('\nData is saved to "users.csv".')
