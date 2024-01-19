import pandas as pd
import glob as glob 
from datetime import datetime
from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt

# File paths
file_path_1 = "/Users/ardaculhaci/Desktop/cs210/project/Spotify Account Data/StreamingHistory0.json"
file_path_2 = "/Users/ardaculhaci/Desktop/cs210/project/Spotify Account Data/StreamingHistory1.json"

# List of file paths
file_paths = [file_path_1, file_path_2]

# Initialize an empty DataFrame
df = pd.DataFrame()

# Iterate through each file and concatenate the data
for file_path in file_paths:
    # Read JSON file into a DataFrame
    data = pd.read_json(file_path)

    # Concatenate the data to the existing DataFrame
    df = pd.concat([df, data], ignore_index=True)


df['endTime'] = pd.to_datetime(df['endTime'])

# Define a function to get the season based on a date
def get_season(date):
    month = date.month
    if 3 <= month <= 5:
        return 'Spring'
    elif 6 <= month <= 8:
        return 'Summer'
    elif 9 <= month <= 11:
        return 'Fall'
    else:
        return 'Winter'

# Apply the function to create a new 'season' column
df['season'] = df['endTime'].apply(get_season)

#Define a function to get the day of the week based on a date
def get_day(date):
    day = date.dayofweek
    if day == 0:
        return 'Monday'
    elif day == 1:
        return 'Tuesday'
    elif day == 2:
        return 'Wednesday'
    elif day == 3:
        return 'Thursday'
    elif day == 4:
        return 'Friday'
    elif day == 5:
        return 'Saturday'
    else:
        return 'Sunday'
    
# Apply the function to create a new 'day' column
df['day'] = df['endTime'].apply(get_day) 


# Assuming df is your DataFrame
df['endTime'] = pd.to_datetime(df['endTime'])

# Group by season and artist, and sum the milliseconds played
top_artists_seasonal = df.groupby(['season', 'artistName'])['msPlayed'].sum().reset_index()

# Sort the DataFrame to get the top artist for each season
top_artists_seasonal = top_artists_seasonal.sort_values(['season', 'msPlayed'], ascending=[True, False])

# Function to convert milliseconds to hours, minutes, seconds
def ms_to_hms(ms):
    seconds = ms // 1000
    return str(timedelta(seconds=seconds))

# Convert 'msPlayed' to hours, minutes, seconds format
top_artists_seasonal['duration'] = top_artists_seasonal['msPlayed'].apply(ms_to_hms)

# Display the result
print(top_artists_seasonal.groupby('season').head(1)[['season', 'artistName', 'duration']])

# Group by season and sum the milliseconds played
total_duration_per_season = df.groupby('season')['msPlayed'].sum().reset_index()

# Function to convert milliseconds to hours, minutes, seconds
def ms_to_hms_total(ms):
    seconds = ms // 1000
    return str(timedelta(seconds=seconds))

# Convert 'msPlayed' to hours, minutes, seconds format
total_duration_per_season['total_duration'] = total_duration_per_season['msPlayed'].apply(ms_to_hms_total)

# Display the result
print(total_duration_per_season[['season', 'total_duration']])


# Group by season and day, and sum the milliseconds played
daily_duration_per_season = df.groupby(['season', 'day'])['msPlayed'].sum().reset_index()

# Calculate the average duration per day
daily_duration_per_season['average_duration_per_day'] = daily_duration_per_season['msPlayed'] / (len(df['day'].unique()) // len(df['season'].unique()))

# Function to convert milliseconds to hours, minutes, seconds
def ms_to_hms_average(ms):
    seconds = ms // 1000
    return str(timedelta(seconds=seconds))

# Convert 'average_duration_per_day' to hours, minutes, seconds format
daily_duration_per_season['average_duration_per_day_hms'] = daily_duration_per_season['average_duration_per_day'].apply(ms_to_hms_average)

# Display the result
print(daily_duration_per_season[['season', 'day', 'average_duration_per_day_hms']])


# Import the pandas library
# Define the file path of the Excel file
excel_file_path = "/Users/ardaculhaci/Desktop/cs210/project/spotify_genres.xlsx"

# Read the Excel file into a DataFrame
excel_df = pd.read_excel(excel_file_path)

# Ensure that the 'title' column in 'excel_df' has unique values
excel_df = excel_df.drop_duplicates(subset='title')

# Get the unique song names
unique_songs = df['trackName'].unique()

# Filter the DataFrame to include only the common songs
common_songs_df = df[df['trackName'].isin(excel_df['title'])].copy()

# Reset the index of excel_df
excel_df = excel_df.reset_index(drop=True)

# Add a new column named 'genres' to the common_songs_df DataFrame
common_songs_df.loc[:, 'genres'] = common_songs_df['trackName'].map(excel_df.set_index('title')['top genre'])

# Reset the index of common_songs_df
common_songs_df = common_songs_df.reset_index(drop=True)
common_songs_df.index += 1

# Group by season and day, and count the occurrences of each genre
music_preferences = common_songs_df.groupby(['season', 'day'])['genres'].value_counts().reset_index(name='count')

# Display the result
print(music_preferences)

#can you give me the most listened genre for each season according to the common_songs_df dataframe?
# Group by season and genre, and sum the milliseconds played
top_genres_seasonal = common_songs_df.groupby(['season', 'genres'])['msPlayed'].sum().reset_index()

print(top_genres_seasonal)

#give me the most listened song for each season according to top_genres_seasonal
# Sort the DataFrame to get the top genre for each season
top_genres_seasonal = top_genres_seasonal.sort_values(['season', 'msPlayed'], ascending=[True, False])

print(top_genres_seasonal.groupby('season').head(1)[['season', 'genres', 'msPlayed']])

# Group by day and genre, and sum the milliseconds played
top_genres_daily = music_preferences.groupby(['day', 'genres'])['count'].sum().reset_index()

# Sort the DataFrame to get the top genre for each day
top_genres_daily = top_genres_daily.sort_values(['day', 'count'], ascending=[True, False])

# Get the most listened genre for each day
most_listened_genre_per_day = top_genres_daily.groupby('day').head(1)[['day', 'genres', 'count']]

print(most_listened_genre_per_day)




# Set the 'endTime' column as the index
df.set_index('endTime', inplace=True)

# Resample data by day and count the number of songs
daily_counts = df.resample('D').size()

daily_counts.to_json(r'/Users/ardaculhaci/Desktop/cs210/project/daily_counts.json')

# Plot the time series
daily_counts.plot(figsize=(12, 6), title='Daily Song Counts over Time')
plt.xlabel('Date')
plt.ylabel('Number of Songs')
plt.show()



import seaborn as sns
import matplotlib.pyplot as plt

# Define a color palette for each season
season_colors = {'Spring': 'green', 'Summer': 'orange', 'Fall': 'brown', 'Winter': 'blue'}

# df.to_json(r'/Users/ardaculhaci/Desktop/cs210/project/songs_by_season.json')

# Countplot for season distribution with customized colors
plt.figure(figsize=(8, 6))
sns.countplot(x='season', data=df, palette=season_colors)
plt.title('Distribution of Songs by Season')
plt.show()

# Group by season and artist, and count the occurrences of each artist
top_artists_seasonal = df.groupby(['season', 'artistName']).size().reset_index(name='count')

# Sort the DataFrame to get the top 10 artists for each season
top_artists_seasonal = top_artists_seasonal.sort_values(['season', 'count'], ascending=[True, False])

# Get the top 10 artists for each season
top_10_artists_per_season = top_artists_seasonal.groupby('season').head(10)[['season', 'artistName']]

top_10_artists_per_season.to_json(r'/Users/ardaculhaci/Desktop/cs210/project/top_10_artists.json')

print(top_10_artists_per_season)


# Sort the DataFrame to get the top genre for each season
top_genres_seasonal = top_genres_seasonal.sort_values(['season', 'msPlayed'], ascending=[True, False])

# Convert milliseconds to minutes
top_genres_seasonal['msPlayed'] = top_genres_seasonal['msPlayed'] / (1000 * 60)

# Get the most listened genre for each season
top_genre_per_season = top_genres_seasonal.groupby('season').head(1)[['season', 'genres', 'msPlayed']]

# Group by season and genre, and sum the milliseconds played
top_genres_seasonal = common_songs_df.groupby(['season', 'genres'])['msPlayed'].sum().reset_index()

# Sort the DataFrame to get the top 5 genres for each season
top_5_genres_per_season = top_genres_seasonal.groupby('season').apply(lambda x: x.nlargest(5, 'msPlayed')).reset_index(drop=True)

# Pivot the data to create a stacked bar plot
stacked_data = top_5_genres_per_season.pivot(index='season', columns='genres', values='msPlayed')

# save to json
stacked_data.to_json(r'/Users/ardaculhaci/Desktop/cs210/project/stacked_data.json')

# Plot the stacked bar plot
plt.figure(figsize=(10, 6))
stacked_data.plot(kind='bar', stacked=True, colormap='viridis')
plt.title('Top Five Listened Genres per Season')
plt.xlabel('Season')
plt.ylabel('Total Listening Time (minutes)')
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


