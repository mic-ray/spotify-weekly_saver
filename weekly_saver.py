import sys
# Spotipy is a python wrapper for the Spotify API
import spotipy
from authentication import authenticate

# Extract all track IDs and the playlist date from a given tracklist
def getTracks(trackList):
    # First add the playlist date
    result = [trackList[0]['added_at']]

    # Loop over tracklist
    for track in trackList:
        # Add the track ID to the result list
        result.append(track['track']['id'])

    return result

# Save the current Weekly Mix to a new playlist
def saveWeekly():

    # Get tracklist from the Weekly Mix playlist
    weeklyTrackList = sp.user_playlist_tracks(user, weeklyPl['id'])

    # Get Track IDs
    weeklyTracks = getTracks(weeklyTrackList['items'])

    # Create new playlist
    weekly = sp.user_playlist_create(user, f'Weekly Mix {weeklyTracks[0].split("T")[0]}', public=False)['id']

    # Add tracks to newly created playlist
    sp.user_playlist_add_tracks(user, weekly, weeklyTracks[1:])

    print("Saved current Weekly Mix!")

# Save the current Release Radar to a new playlist
def saveRelease():

    # Get tracklist from the Release Radar playlist
    releaseTrackList = sp.user_playlist_tracks(user, releasePl['id'])
    
    # Get Track IDs
    releaseTracks = getTracks(releaseTrackList['items'])
    
    # Create new playlist
    release = sp.user_playlist_create(user, f'Release Radar {releaseTracks[0].split("T")[0]}', public=False)['id']

    # Add tracks to newly created playlist
    sp.user_playlist_add_tracks(user, release, releaseTracks[1:])

    print("Saved current Release Radar!")

# Get the user e-mail adress for Spotify     
eMail = input("Please enter your Spotify e-mail adress:\n")

# Get the authentication token
token = authenticate(eMail)

if token:
    # Create Spotify client
    sp = spotipy.Spotify(auth=token)
    sp.trace = False

    # Save user ID
    user = sp.me()['id']

    # Get playlists
    playlists = sp.current_user_playlists()['items']

    # Loop over playlists to find Release Radar and Weekly Mix
    for pl in playlists:
        if pl['name'] == 'Release Radar':
            releasePl = pl
        if pl['name'] == 'Discover Weekly':
            weeklyPl = pl
else:
    print('Authentication Error')
    sys.exit()

# If the two playlists were found 
if weeklyPl and releasePl:
    
    # Ask what playlists user wants to save
    choice = input("Press 'w' to save your Weekly Mix\nPress 'r' to save your Release Radar\nPress 'b' to save both\n")

    # Check input and save corresponding playlists
    if choice in ['w', 'W']:
        saveWeekly()
    elif choice in ['r', 'R']:
        saveRelease()
    elif choice in ['b', 'B']:
        saveWeekly()
        saveRelease()
    else:
        print("Invalid input")
        sys.exit()
else:
    print('Error while retrieving playlists')
    sys.exit()
    