import pandas as pd
def useractive(selected_user , df):
    if selected_user != "Overall":
        new_df = df[df['User'] == selected_user]

        timline = new_df.groupby(['Year' , 'Month' , 'Month_name']).count()['User_messages'].reset_index()
        t = []
        for i in range(timline.shape[0]):
            t.append(str(timline['Month_name'][i]) + "-" + str(timline['Year'][i]))

        timline['Month_year'] = t

        return timline
    else:
        

        timline = df.groupby(['Year' , 'Month' , 'Month_name']).count()['User_messages'].reset_index()
        #print(timline)
        t = []
        for i in range(timline.shape[0]):
            t.append(str(timline['Month_name'][i]) + "-" + str(timline['Year'][i]))

        timline['Month_year'] = t

        return timline

        