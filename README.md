# QQmusic_to_Spotify

For long I want to convert my music app from QQ Music to Spotify for streaming music and new release albums, but I have accumulated 800+ songs in the QQ music playlists, and I want them to be transferred to Spotify. The UI of QQ music app was intentionally designed to avoid text selection, so copy/paste the song names were impossible. While I googled solutions and there was no easy way, I thought of using the text recognition tool in GCP to convert the screenshots into 'Song - Artist' pairs.

### The process is really easy:
- Register GCP and download VisionAPI
- Adjust the font size of QQ Music APP to the smallest
- Take screenshots of 'Song - Artist' pairs and store them in the 'Images' folder
- Run code in 'VisionAPI_demo.py'
- Done! You can find the extracted playlist.txt in the output folder

### The last step is to import the playlist into Spotify (or any other music app you like)
- Find a website/app to do this. For example, I used TuneMyMusic.
