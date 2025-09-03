import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def percent_others(df):
    #Calculate fraction of Nintendo and other games among all games
    general_count=df['Publisher'].count()
    nintendo_count=df['Publisher'].value_counts().get('Nintendo',0)/general_count
    other_games_count=1-nintendo_count
    return (nintendo_count,other_games_count)
def best(df):
    #Create a dictionary, where key is year and value is a list that contains maximum score of each year and appropriate game
    df_copy=df.copy()
    df_copy.dropna(subset=['Release Date'],inplace=True)
    df_copy['Year']=df_copy['Release Date'].dt.year
    game_years=dict()
    for _,row in df_copy.iterrows():
        if not (row['Year'] in game_years and row['Total Score'] <= game_years[row['Year']][0]):
            game_years[row['Year']]=[row['Total Score'],row['Game']]
    return game_years

def fill_na(df):
    #Fill NA with essential values
    cols = ['VGChartz Score', 'Critic Score', 'User Score']
    for index, row in df.iterrows():
        # Check count of NaN
        nan_count = row[cols].isna().sum()
        #If count of NaN is 1
        if nan_count == 1:
            nan_col = [col for col in cols if pd.isna(row[col])][0]
            # Find columns with NaN
            non_nan_cols = [col for col in cols if col != nan_col]
            # Calculate average two non-NaN columns
            mean_value = row[non_nan_cols].mean()
            # Replace NaN to average
            df.loc[index, nan_col] = round(mean_value,1)
        #If count of NaN is 2
        elif nan_count == 2:
            # Find columns without NaN
            non_nan_col = [col for col in cols if not pd.isna(row[col])][0]
            # Find column with NaN
            nan_cols = [col for col in cols if pd.isna(row[col])]
            non_nan_value = row[non_nan_col]
            # Replace all NaN to value from non-NaN column
            for col in nan_cols:
                df.loc[index, col] = round(non_nan_value,1)
    
def average(df):
    #Create an array with average score of each game
    cols = ['VGChartz Score', 'Critic Score', 'User Score']
    #Array with average scores
    mean=np.array([])
    for _,row in df.iterrows():
        temp=np.array([row[col] for col in cols])
        mean=np.append(mean,temp.mean())
    #All numbers have one number after point
    mean=np.round(mean,decimals=1)
    return mean


#Read data from csv
values=pd.read_csv('Nintendo Switch Games.csv',encoding='latin-1') 
df=pd.DataFrame(values)

#Convert data to date
df['Release Date']=pd.to_datetime(df['Release Date'])
df['Last Update']=pd.to_datetime(df['Last Update'])

#Remove all rows if no score in all three columns of score('VGChartz Score','Critic Score','User Score')
df.dropna(how='all',subset=['VGChartz Score','Critic Score','User Score'],inplace=True)

#I need delete this text, because it is in names of games
df=df.replace("\r\nRead the review","",regex=True)
#Fill NA with essential values
fill_na(df)
mean_score=average(df)

#Add new column with total score of each game
df.insert(8,'Total Score',mean_score)


#Print main statistics values of total score
min=df['Total Score'].min()
max=df['Total Score'].max()
mean=df['Total Score'].mean()
median=df['Total Score'].median()
mode=df['Total Score'].mode()
std=df['Total Score'].std()
var=df['Total Score'].var()
print(f"Min: {round(min,2)}")
print(f"Max: {round(max,2)}")
print(f"Mean: {round(mean,2)}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standard deviation: {round(std,2)}")
print(f"Variance: {round(var,2)}")


#Preparing data for histogram
best_games=best(df)
years=best_games.keys()
scores=[]
games=[]
for year in best_games:
    scores.append(best_games[year][0])
    games.append(best_games[year][1])
#Create a histogram
fig1=plt.figure(figsize=(40,40))
ax1=fig1.add_subplot(1,1,1)
bars=ax1.bar(years,scores,width=0.5)
i=0
for bar in bars:
    yval=bar.get_height()
    xval=bar.get_x()
    width=bar.get_width()/2
    plt.text(xval+width,yval+0.4,games[i],ha='center',va='bottom',fontsize=12)
    i+=1
plt.grid(True)
plt.xlabel('Years')
plt.ylabel('Scores')
#Save the histogram
plt.savefig('test1.png')

#Preparing data for a pie diagram
sizes=percent_others(df)
categories=('Nintendo','Other')
colors=('Red','Grey')

#Create the pie diagram
fig2=plt.figure()
ax2=fig2.add_subplot(1,1,1)
ax2.pie(sizes,labels=categories,colors=colors,autopct='%1.1f%%')
#Save the pie diagram
plt.savefig('test2.png')
#Display the diagrams
plt.show()
#Save update csv file
df.to_csv('update_nintendo_switch.csv')
