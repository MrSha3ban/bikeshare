import time
import pandas as pd
import numpy as np
import os
# i used os library just to help me clearing the terminal screen and make my project looks neat
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
 # assigning the city ,month & day  lists as dicts to choose from
 
city_list={'1':'chicago','2':'new york city','3':'washington'}

month_list={'1':'january','2':'february','3':'march',
            '4':'april','5':'may','6':'june','7':'all'}

day_list={'1':'monday','2':'tuesday','3':'wednesday',
          '4':'thursday','5':'friday','6':'saturday','7':'sunday','8':'all'}

#  I created an intro  banner on the screen to use as header!

intro='''     

.______    __   __  ___  _______         _______. __    __       ___      .______       _______ 
|   _  \  |  | |  |/  / |   ____|       /       ||  |  |  |     /   \     |   _  \     |   ____|
|  |_)  | |  | |  '  /  |  |__         |   (----`|  |__|  |    /  ^  \    |  |_)  |    |  |__   
|   _  <  |  | |    <   |   __|         \   \    |   __   |   /  /_\  \   |      /     |   __|  
|  |_)  | |  | |  .  \  |  |____    .----)   |   |  |  |  |  /  _____  \  |  |\  \----.|  |____ 
|______/  |__| |__|\__\ |_______|   |_______/    |__|  |__| /__/     \__\ | _| `._____||_______|
                                                                                                           


 o__         __o        ,__o        __o           __o
 ,>/_       -\<,      _-\_<,       _`\<,_       _ \<_
(*)`(*).....O/ O.....(*)/'(*).....(*)/ (*).....(_)/(_)


'''
# the following 4 codes i use them to seperate the screen and make the progerss percentage
os.system('cls') 
print(intro)
loading=0.1
print('='*45)

# create a dataframe as a container for all the 3 files

df=pd.DataFrame()
#assign the filtered data frame container to use in my functions
fltr_df=pd.DataFrame()

start_time = time.time()

#use for loop to read csv files in a dataframe and creat one csv file 
for cities in CITY_DATA.keys() :
    
    data=pd.read_csv(CITY_DATA[cities])
    
#adding a column contain the city's name
    data['cityname']=cities

#collect all dataframes in the main dataframe (df)
    df=df.append(data)
    os.system('cls') 
    print(intro)
    loading+=33.3
    print('Please wait ! collecting data :',int(loading),'% of data is ready')
#change the type of the start & end time columns to dt and creat 3 additional columns for the start time details
#this details (numbers) i will use in filtering 
df[['Start Time', 'End Time']] = df[['Start Time', 'End Time']].apply(pd.to_datetime)   
df['start_month']=df['Start Time'].dt.month
df['start_day']=df['Start Time'].dt.weekday
df['start_hour']=df['Start Time'].dt.hour

#export the df to one csv file
df.to_csv('alldata.csv')  

os.system('cls') 
print(intro)
print('-'*40)


def get_filters():
    """
    welcome the user and Asks him to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - number of the month to filter by, or "all" to apply no month filter
        (str) day - number of the day of week to filter by, or "all" to apply no day filter
   I will use the numbers  to get the user's input to privent  errors'
    """
    os.system('cls')    
    print(intro)
    print('='*40)
    print('Hello! Let\'s explore some US bikeshare data!\n\n\n')
   
   

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
   
    city=input('please choose the city by entering its number from the list below :\n 1: chicago\n 2: new york city\n 3: washington\n \n Your choice is :    ')
     
    while (city not in city_list.keys()):
        #the error message asking to re enter the input number
        city=input('Invalid Choice! please type The number of your chois:  ')
    #use the input number to change the value of city to the name of the city
    city=city_list[city]
    
    os.system('cls')    
    print(intro)
    print('='*40)
    # use th same way TO DO: get user input for month (all, january, february, ... , june) as number using in filters
    month=input('please enter the number of the month you want to analys  :\n1:   january\n2:   february\n3:   march\n4:   april\n5:   may\n6:   june\n7:   all\n \n Your choice is :    ')
    while (month not in month_list.keys()):
        month=input('Invalid Choice! please type The number of your chois:  ')
   
    os.system('cls') 
    print(intro)
    print('='*40)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('please enter the number the day number from the list below :\n1:    monday\n2:    tuesday\n3:    wednesday\n4:    thursday\n5:    friday\n6:    saturday\n7:    sunday\n8:   all\n \n Your choice is :    ')
    while (day not in day_list.keys()):
       day=input('Invalid Choice! please type The number of your chois:  ')
      
    os.system('cls') 
    print('='*45)
    print(intro)
    #inform the user with his choices
    print('So you choose the following filters \n City: {} \n Month: {} \n Day: {} '.format(city, month_list[month],day_list[day]))
    print('='*40)
    #prepairing day and month as int to use in filters
    day=int(day)-1
    month=int(month)
    return city, month,day


def load_data(city, month, day):
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - number of the month to filter by, or 7 as  "all" to apply no month filter
        (str) day - number of the day of week to filter by, or 7 as  "all" to apply no day filter
    Returns:
        fltr_df - Pandas DataFrame containing city data filtered by month and day
    """
    # the filter layers as below:
    fltr_df=df[df["cityname"]==city]
    if month !=7 :
        fltr_df=fltr_df[fltr_df["start_month"]==month]
    if day != 7:
        fltr_df=fltr_df[fltr_df["start_day"]==day]
      
    return fltr_df

def time_stats(fltr_df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('MOst common month is : ',month_list[str(fltr_df['start_month'].mode()[0])].title())

    # TO DO: display the most common day of week
    
    print('MOst common day is : ',day_list[str(fltr_df['start_day'].mode()[0]+1)].title())

    # TO DO: display the most common start hour
   
    print('MOst common hour is : ',fltr_df['start_hour'].mode()[0],': 00')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(fltr_df):
    """Displays statistics on the most popular stations and trip."""
    # i created temp Dataframe to use it in the most frequent combination section
    combination=fltr_df['Start Station']+" (To) "+fltr_df['End Station']
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start stationis : ',fltr_df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most commonly used end stationis : ',fltr_df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('Most commonly frequent combination of both start and end station : ',combination.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(fltr_df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # I created temp DataFrame tu use  in  calculations
    duration=fltr_df['End Time']-fltr_df['Start Time']
    # TO DO: display total travel time
    print('The total  travel time is',duration.sum(),'hour(s)')

    # TO DO: display mean travel time
    print('The average of travel time is',duration.mean(),'hour(s)')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(fltr_df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # I will throw this exception because if the user choose washington  the  program will cresh!
    try: 
        
      # the tow steps in one (1.TO DO: Display counts of user types)
      # (2. TO DO: Display counts of gender) i used the pivot_table in pandas.
      # first i will change the unnamed column to 'count' to be displyed in the pivot as this name
       fltr_df.rename(columns={fltr_df.columns.values[0]:'count'}, inplace=True)
       print(pd.pivot_table(fltr_df,values= 'count',index=['User Type','Gender'],aggfunc='count'))
       print('-'*20)
    except :
        print('\nThere are no data for {}'.format(city)) 
    if city == 'washington' :
        print('\nThere are no data for {}'.format(city))
    else:
        # TO DO: Display earliest, most recent, and most common year of birth
        print('earlies year of birth is : ',int(fltr_df['Birth Year'].min()))
        print('most recent  year of birth is : ',int(fltr_df['Birth Year'].max()))
        print('most common year of birth is :  ',int(fltr_df['Birth Year'].mode()[0]))
    
         
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*45)

def display_data(fltr_df):
    # creating a temp dataframe to hold the columns i need to show
    dsply_df = pd.DataFrame(fltr_df, columns = ['Start Time',	'End Time'	,'Trip Duration',	'Start Station'	,'End Station',	'User Type',	'Gender'	,'Birth Year'])
      
    # I used sample to genrate a  5 rows random sample of the data 
     # the following while loop will be excuted till the user stop entering y as an input
    while True:
        dsply_answr= input("\n\n Would you Like to see sample of the data?\n Type y then press Enter if so\n or just press Enter to continue!")
        if dsply_answr=="y":
            print(dsply_df.sample(n=5))
        else:   
           break
  
        
def main():
    while True:
        city, month, day = get_filters()
        fltr_df = load_data(city, month, day)

        time_stats(fltr_df)
        station_stats(fltr_df)
        trip_duration_stats(fltr_df)
        # i will add the city to use it in try exception.
        user_stats(fltr_df,city)
        display_data(fltr_df)
        restart = input('\nWould you like to restart? Enter y for(yes) or just press Enter for(no).\n')
        os.system('cls')    
        print(intro)
        print('='*40)
        if restart.lower() != 'y':
            break
        

if __name__ == "__main__":
	main()
    
