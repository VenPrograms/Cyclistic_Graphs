import pandas as pd
import matplotlib.pyplot as plt     

df = pd.read_csv('United_Tables_New.csv', encoding='utf-8', low_memory=False)


# Display the first few rows of the DataFrame

#print(df.info())
#print(df.describe())

#fd = df[df['ride_dur_in_seconds'] < 0]
#print(df['end_station_name'].isnull().sum())

#print(df.groupby(['usertype', 'day_of_week'])['ride_dur_in_seconds'].mean())

#print(df.groupby('usertype').size())


#fig, axes = plt.subplots(1, 2, figsize=(12, 5))


#mf = df[df['usertype'] == 'member']

#mf.groupby('day_of_week')['ride_dur_in_seconds'].mean().plot(kind='bar', ax=axes[0])
#plt.title('Number of Rides by Day of Week for Members')
#plt.xlabel('Day of Week')
#plt.ylabel('Number of Rides')



#cf = df[df['usertype'] == 'casual']

#cf.groupby('day_of_week')['ride_dur_in_seconds'].mean().plot(kind='bar', ax=axes[1])
#plt.title('Number of Rides by Day of Week for Members')
#plt.xlabel('Day of Week')
#plt.ylabel('Number of Rides')

#plt.tight_layout()
#plt.show()



#plt.plot(df[['day_of_week'], df['value']])








'''

#The below plots the average ride duration for members and casual users by day of the week

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

day_order = [1, 2, 3, 4, 5, 6, 7]

day_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


member_avg = df[df['usertype'] == 'member'].groupby('day_of_week')['ride_dur_in_seconds'].mean().reindex(day_order)

casual_avg = df[df['usertype'] == 'casual'].groupby('day_of_week')['ride_dur_in_seconds'].mean().reindex(day_order)



member_avg.plot(kind='bar', ax=axes[0], color='blue')
axes[0].set_title('Member Avg Ride Duration')
axes[0].set_xlabel('Day of Week')
axes[0].set_ylabel('Seconds')
axes[0].set_xticks(range(len(day_labels)))
axes[0].set_xticklabels(day_labels, rotation=45)

casual_avg.plot(kind='bar', ax=axes[1], color='orange')
axes[1].set_title('Casual Avg Ride Duration')
axes[1].set_xlabel('Day of Week')
axes[1].set_ylabel('Seconds')
axes[1].set_xticks(range(len(day_labels)))
axes[1].set_xticklabels(day_labels, rotation=45)

plt.tight_layout()
plt.show()


'''




''' 

#The below plots the count of rides for members and casual users by day of the week

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

day_order = [1, 2, 3, 4, 5, 6, 7]

day_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


member_avg = df[df['usertype'] == 'member'].groupby('day_of_week')['ride_dur_in_seconds'].count().reindex(day_order)

casual_avg = df[df['usertype'] == 'casual'].groupby('day_of_week')['ride_dur_in_seconds'].count().reindex(day_order)



member_avg.plot(kind='bar', ax=axes[0], color='green')
axes[0].set_title('Member Ride Count')
axes[0].set_xlabel('Day of Week')
axes[0].set_ylabel('Count')
axes[0].set_xticks(range(len(day_labels)))
axes[0].set_xticklabels(day_labels, rotation=45)

casual_avg.plot(kind='bar', ax=axes[1], color='purple')
axes[1].set_title('Casual Ride Count')
axes[1].set_xlabel('Day of Week')
axes[1].set_ylabel('Count')
axes[1].set_xticks(range(len(day_labels)))
axes[1].set_xticklabels(day_labels, rotation=45)

plt.tight_layout()
plt.show()


''' 



'''

# The below plots the average ride duration for members and casual users by user type

avg_dur_by_usertype = df.groupby('usertype')['ride_dur_in_seconds'].mean()
avg_dur_by_usertype.plot(kind='bar', color=['brown', 'purple'])
plt.title('Average Ride Duration by User Type')
plt.show()

'''


'''

# The below plots the number of rides based on gender for casual and member users

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

casuals = df[df['usertype'] == 'casual'].copy()
casuals['gender'] = casuals['gender'].fillna('Unknown')

num_rides_by_gender_casuals = casuals.groupby('gender')['ride_dur_in_seconds'].count()

num_rides_by_gender_casuals.plot(kind='bar', ax=axes[0], color='orange')


members = df[df['usertype'] == 'member'].copy() #THe copy part is important to avoid undefined behavior
members['gender'] = members['gender'].fillna('Unknown')

num_rides_by_gender_members = members.groupby('gender')['ride_dur_in_seconds'].count()

num_rides_by_gender_members.plot(kind='bar', ax=axes[1], color='blue')

axes[0].set_title('Number of Rides by casuals')
axes[0].set_xlabel('gender')
axes[0].set_ylabel('Number of Rides')

axes[1].set_title('Number of Rides by members')
axes[1].set_xlabel('gender')
axes[1].set_ylabel('Number of Rides')

plt.tight_layout()
plt.show()


'''

mf = df[df['usertype'] == 'member']
cf = df[df['usertype'] == 'casual']
''' 

mf['start_hour'] = pd.to_datetime(mf['start_time']).dt.hour
plt.hist(mf['start_hour'], bins=24, color='teal', edgecolor='black')
plt.title('Member Ride Start Hours')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Rides')
plt.show()
'''



cf['start_hour'] = pd.to_datetime(cf['start_time']).dt.hour
plt.hist(cf['start_hour'], bins=24, color='lavender', edgecolor='black')
plt.title('Casual Ride Start Hours')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Rides')
plt.show()





''' 
 
member_avg = df[df['usertype'] == 'member']


plt.plot(member_avg[['day_of_week', 'ride_dur_in_seconds']].groupby('day_of_week').mean())
plt.ylim(bottom=0)
plt.show()

'''