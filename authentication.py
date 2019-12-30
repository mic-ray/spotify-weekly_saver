# To access environment variables
import os
import spotipy.util as util

# Authenticates a user with Spotify
def authenticate(username):

    # Scope required to access/modify the playlists
    scope = 'playlist-modify-private playlist-read-private'

    # Get Client ID of the app from environmental variables
    client_id = os.environ.get('spo_client_id')

    # Get Client Secret of the app from environmental variables
    client_secret = os.environ.get('spo_client_secret')

    # Return the token after authenticating with Spotify using the Spotipy wrapper
    # Please note: After authentication user is redirected to localhost, since application is used locally
    return util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri='http://localhost:3000/')
