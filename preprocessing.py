import re
import pandas as pd

def preprocessing(data):
    patter = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s' #re patter form rex101.com
    
    message = re.split(patter , data)[1:] #here ther some bank space that why we start from [1:]
    #print(message)
    dates = re.findall(patter , data)
    #print(dates)

    df = pd.DataFrame({
    "Date" : dates,
    "User_messages" : message 
    })

    df['Date'] = pd.to_datetime(df['Date'] , format="%d/%m/%Y, %H:%M - ")

    User_name = []
    MessageOfUser = []
    for i  in df['User_messages']:
        regular = re.split("([\w\W]+?):\s" , i)
        if regular[1:]:
            User_name.append(regular[1])
            MessageOfUser.append(regular[2])
        else :
            User_name.append('Group Notification')
            MessageOfUser.append(regular[0])

    df['User_messages'] = MessageOfUser
    df['User'] = User_name
    
    df['Day'] = df['Date'].dt.day
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    df['Hours'] = df['Date'].dt.hour
    df['Minute'] = df['Date'].dt.minute
    df['Month_name'] = df['Date'].dt.month_name()
    df.drop(['Date'] , axis=1 , inplace=True)

    return df
