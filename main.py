import json
import tkinter as tk
from tkinter import filedialog
import webbrowser

#Object oriented programming use to easily create a number of songs

class Song:
    def __init__(self, title: str, artist: str, genre: str, length: int, link: str):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.length = length #Length will be done in seconds for each song
        self.link = link

#There are 3 popular songs from a variety of artists of a variety of different genres

song1 = Song("In the End", "Linkin Park", "Metal", 216, "https://open.spotify.com/track/60a0Rd6pjrkxjPbaKzXjfq?si=0512b5273be24323")
song2 = Song("Numb", "Linkin Park", "Metal", 187, "https://open.spotify.com/track/2nLtzopw4rPReszdYBJU6h?si=5e6518ec8e334691")
song3 = Song("What I've Done", "Linkin Park", "Metal", 205, "https://open.spotify.com/track/18lR4BzEs7e3qzc0KVkTpU?si=a82a9788de3241b6")
song4 = Song("Smells Like Teen Spirit", "Nirvana", "Grunge", 301, "https://open.spotify.com/track/4CeeEOM32jQcH3eN9Q2dGj?si=0009897a2a884f6a")
song5 = Song("Heart-Shaped Box", "Nirvana", "Grunge", 281, "https://open.spotify.com/track/11LmqTE2naFULdEP94AUBa?si=ad6c2468f935468a")
song6 = Song("Come As You Are", "Nirvana", "Grunge", 218, "https://open.spotify.com/track/2RsAajgo0g7bMCHxwH3Sk0?si=907a26e9dea24642")
song7 = Song("Billie Jean", "Michael Jackson", "Pop", 293, "https://open.spotify.com/track/7J1uxwnxfQLu4APicE5Rnj?si=ad759bbed70f45f3")
song8 = Song("Beat It", "Michael Jackson", "Pop", 258, "https://open.spotify.com/track/3BovdzfaX4jb5KFQwoPfAw?si=6f0f060731944130")
song9 = Song("Thriller", "Michael Jackson", "Pop", 357, "https://open.spotify.com/track/2LlQb7Uoj1kKyGhlkBf9aC?si=7b202ff624f94cf4")
song10 = Song("Magnolia", "Playboi Carti", "Rap", 181, "https://open.spotify.com/track/1e1JKLEDKP7hEQzJfNAgPl?si=93a7ddd6f10e4a2a")
song11 = Song("Sky", "Playboi Carti", "Rap", 193, "https://open.spotify.com/track/29TPjc8wxfz4XMn21O7VsZ?si=429339b48c9b484d")
song12 = Song("Location", "Playboi Carti", "Rap", 168, "https://open.spotify.com/track/3yk7PJnryiJ8mAPqsrujzf?si=f1d43d7e84a9422f")
song13 = Song("HUMBLE", "Kendrick Lamar", "Rap", 177, "https://open.spotify.com/track/7KXjTSCq5nL1LoYtL7XAwS?si=ce4e8959529f42af")
song14 = Song("Money Trees", "Kendrick Lamar", "Rap", 386, "https://open.spotify.com/track/74tLlkN3rgVzRqQJgPfink?si=f9744e39908f4e58")
song15 = Song("Not Like Us", "Kendrick Lamar", "Rap", 274, "https://open.spotify.com/track/6AI3ezQ4o3HUoP6Dhudph3?si=f87df1d9ba904995")
song16 = Song("Yale", "Ken Carson", "Rap", 106, "https://open.spotify.com/track/0HTIrbUwwFn984RzVZm5Fk?si=3b2d58504e89435b")
song17 = Song("Fighting My Demons", "Ken Carson", "Rap", 150, "https://open.spotify.com/track/2c7sRekhMGlj7u1WIIzoQu?si=7fcfabf883e945e7")
song18 = Song("Overseas", "Ken Carson", "Rap", 141, "https://open.spotify.com/track/722NAIXkI6WRNvu9O7JkdH?si=ee35fcac9d374f06")
song19 = Song("My Love Mine All Mine", "Mitski", "Indie", 137, "https://open.spotify.com/track/3vkCueOmm7xQDoJ17W1Pm3?si=64cd0f58949a4479")
song20 = Song("Washing Machine Heart", "Mitski", "Indie", 128, "https://open.spotify.com/track/3jjsRKEsF42ccXf8kWR3nu?si=9adca12b1f894337")
song21 = Song("Nobody", "Mitski", "Indie", 193, "https://open.spotify.com/track/2P5yIMu2DNeMXTyOANKS6k?si=4ea5064c5c124992")

songList = [ #This is done so that they can be listed and sorted when the user views the library of songs
    song1, song2, song3, song4, song5, song6, song7, song8, song9, song10, song11, song12, song13, song14, song15, song16, song17, song18, song19, song20, song21
]

sortedSongList = sorted(songList, key=lambda song: song.title) #Lambda is used here as it takes on all of the arguments (being each item within the list)

with open("users.json", "r") as f: #This creates a variable holding the information of the dictionary
    userFile = json.loads(f.read())

#Essential functions that are used many times throughout the application

def saveUserData(): #This function is called whenever there is a change in information so it is constantly up-to-date
    with open("users.json", "w") as f:
        saveData = json.dumps(userFile, indent=4)
        f.write(saveData)

def clearScreen(root):
    for i in root.winfo_children():
        i.destroy()

#Functionality for displaying each of the genres and information about each genre




#Functionality for saving songs by a specific artist into a text file

def artistDiscography(root, currentUser):
    clearScreen(root)
    selectedArtist = tk.StringVar()
    mainTitle = tk.Label(root, text="ARTIST MENU", font=("Arial", 30))
    selectArtistLabel = tk.Label(root, text="Select an artist to see their available songs:", font=("Arial", 18))
    currentArtistSelected = tk.Label(root, text="Current artist: None", font=("Arial", 18))

    artistFrame = tk.Frame(root)
    artistFrame.columnconfigure(0, weight=1)
    artistFrame.columnconfigure(1, weight=1)
    artistFrame.columnconfigure(2, weight=1)
    artistFrame.columnconfigure(3, weight=1)
    artistFrame.columnconfigure(4, weight=1)
    artistFrame.columnconfigure(5, weight=1)
    artistFrame.columnconfigure(6, weight=1)

    button1 = tk.Button(artistFrame, text="Linkin Park", cursor="hand2", font=("Arial", 18), command=lambda: editArtist(currentArtistSelected, selectedArtist, "Linkin Park"))
    button1.grid(row=0, column=0)
    button2 = tk.Button(artistFrame, text="Nirvana", cursor="hand2", font=("Arial", 18), command=lambda: editArtist(currentArtistSelected, selectedArtist, "Nirvana"))
    button2.grid(row=0, column=1)
    button3 = tk.Button(artistFrame, text="Michael Jackson", cursor="hand2", font=("Arial", 18), command=lambda: editArtist(currentArtistSelected, selectedArtist, "Michael Jackson"))
    button3.grid(row=0, column=2)
    button4 = tk.Button(artistFrame, text="Playboi Carti", cursor="hand2", font=("Arial", 18), command=lambda: editArtist(currentArtistSelected, selectedArtist, "Playboi Carti"))
    button4.grid(row=0, column=3)
    button5 = tk.Button(artistFrame, text="Kendrick Lamar", cursor="hand2", font=("Arial", 18), command=lambda: editArtist(currentArtistSelected, selectedArtist, "Kendrick Lamar"))
    button5.grid(row=0, column=4)
    button6 = tk.Button(artistFrame, text="Ken Carson", cursor="hand2", font=("Arial", 18), command=lambda: editArtist(currentArtistSelected, selectedArtist, "Ken Carson"))
    button6.grid(row=0, column=5)
    button7 = tk.Button(artistFrame, text="Mitski", cursor="hand2", font=("Arial", 18), command=lambda: editArtist(currentArtistSelected, selectedArtist, "Mitski"))
    button7.grid(row=0, column=6)

    errorMessage = tk.Label(root, text="", font=("Arial", 18), fg="red")
    confirmButton = tk.Button(root, text="Save to text file", cursor="hand2", font=("Arial", 18), command=lambda: saveToFile(str(selectedArtist.get()), errorMessage))
    backButton = tk.Button(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: mainMenu(root, currentUser))

    mainTitle.pack(pady=20)
    selectArtistLabel.pack(pady=20)
    currentArtistSelected.pack(pady=20)
    artistFrame.pack(pady=20)
    errorMessage.pack(pady=20)
    confirmButton.pack(pady=20)
    backButton.pack(pady=20)
    #Artists songs can be saved to a text file

def editArtist(currentArtistSelected, selectedArtist, newArtist):
    selectedArtist.set(newArtist)
    currentArtistSelected.configure(text=f"Current genre: {newArtist}")

def saveToFile(selectedArtist, errorMessage):
    if selectedArtist == "":
        errorMessage.configure(text="You did not select an artist, please try again.")
        return
    
    filePath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text file", "*.txt")])

    artistSongList = []

    for i in sortedSongList:
        if i.artist == selectedArtist:
            artistSongList.append(i.title)

    if filePath: #Check if the user actually selected a path
        with open(filePath, "w") as f:
            f.write(f"{artistSongList}")
        errorMessage.configure(text="Sucessfully saved file.", fg="green")
    else:
        errorMessage.configure(text="Save either failed or was cancelled.")

# Functionality for all of the playlist functions

def playlistMenu(root, currentUser):
    clearScreen(root)
    mainTitle = tk.Label(root, text="PLAYLIST MENU", font=("Arial", 30))
    viewPlaylist = tk.Button(root, text="View playlists", font=("Arial", 18), command=lambda: selectPlaylists(root, currentUser))
    editPlaylist = tk.Button(root, text="Edit playlists", font=("Arial", 18), command=lambda: editPlaylists(root, currentUser))
    createPlaylist = tk.Button(root, text="Create playlist", font=("Arial", 18), command=lambda: createPlaylists(root, currentUser))
    autoCreatePlaylist = tk.Button(root, text="Automatically generate playlist", font=("Arial", 18), command=lambda: autoCreatePlaylists(root, currentUser))
    backButton = tk.Button(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: mainMenu(root, currentUser))
    mainTitle.pack(pady=20)
    viewPlaylist.pack(pady=20)
    editPlaylist.pack(pady=20)
    createPlaylist.pack(pady=20)
    autoCreatePlaylist.pack(pady=20)
    backButton.pack(pady=20)

def selectPlaylists(root, currentUser):
    clearScreen(root)
    mainTitle = tk.Label(root, text="VIEW PLAYLISTS", font=("Arial", 30))
    mainTitle.pack()
    viewplaylistFrame = tk.Frame(root)
    viewplaylistFrame.pack(fill="both", expand=True)
    viewplaylistScrollbar = tk.Scrollbar(viewplaylistFrame)
    viewplaylistScrollbar.pack(side="right", fill="y")
    viewplaylistListBox = tk.Listbox(viewplaylistFrame, yscrollcommand=viewplaylistScrollbar.set, font=("Arial", 18))

    playlistNames = list(userFile[currentUser]["playlists"].keys())

    if playlistNames: #Confirms that the user actually has playlists in their profile
        for i in playlistNames:
            viewplaylistListBox.insert(tk.END, i)

    viewplaylistListBox.pack(side="left", fill="both", expand=True)

    backButton = tk.Button(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: playlistMenu(root, currentUser))
    backButton.pack(pady=25)

    viewplaylistListBox.bind("<<ListboxSelect>>", lambda event: displaySelectedPlaylist(event, root, currentUser, playlistNames))

def displaySelectedPlaylist(event, root, currentUser, playlistNames):
    widget = event.widget
    index = widget.curselection()[0]
    selectedPlaylist = playlistNames[index]

    clearScreen(root)

    mainTitle = tk.Label(root, text="YOUR PLAYLIST", font=("Arial", 30))
    mainTitle.pack()
    libraryFrame = tk.Frame(root)
    libraryFrame.pack(fill="both", expand=True)
    libraryScrollbar = tk.Scrollbar(libraryFrame)
    libraryScrollbar.pack(side="right", fill="y")
    libraryListBox = tk.Listbox(libraryFrame, yscrollcommand=libraryScrollbar.set, font=("Arial", 18))

    for i in userFile[currentUser]["playlists"][selectedPlaylist]:
        libraryListBox.insert(tk.END, f"Song: {i}")
    
    libraryListBox.pack(side="left", fill="both", expand=True)

    backButton = tk.Button(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: mainMenu(root, currentUser))
    backButton.pack(pady=25)

    libraryListBox.bind("<<ListboxSelect>>", lambda event: playSongPlaylist(event, userFile[currentUser]["playlists"][selectedPlaylist]))

def playSongPlaylist(event, selectedPlaylist):
    widget = event.widget
    index = widget.curselection()[0]
    selectedSong = selectedPlaylist[index]

    for i in sortedSongList:
        if i.title == selectedSong:
            webbrowser.open(i.link)
            break

def editPlaylists(root, currentUser):
    clearScreen(root)
    mainTitle = tk.Label(root, text="EDIT PLAYLIST MENU", font=("Arial", 30))
    addSongs = tk.Button(root, text="Add songs to a playlist", font=("Arial", 18), command=lambda: playlistSelection(root, currentUser, "add"))
    removeSongs = tk.Button(root, text="Remove songs from a playlist", font=("Arial", 18), command=lambda: playlistSelection(root, currentUser, "remove"))
    renamePlaylist = tk.Button(root, text="Rename a playlist", font=("Arial", 18), command=lambda: playlistSelection(root, currentUser, "rename"))
    deletePlaylist = tk.Button(root, text="Delete a playlist", font=("Arial", 18), command=lambda: playlistSelection(root, currentUser, "delete"))
    backButton = tk.Button(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: playlistMenu(root, currentUser))
    mainTitle.pack(pady=20)
    addSongs.pack(pady=20)
    removeSongs.pack(pady=20)
    renamePlaylist.pack(pady=20)
    deletePlaylist.pack(pady=20)
    backButton.pack(pady=25)

def playlistSelection(root, currentUser, playlistFunc):
    clearScreen(root)
    if playlistFunc == "add":
        mainTitle = tk.Label(root, text="SELECT PLAYLIST TO ADD SONGS TO", font=("Arial", 30))
    elif playlistFunc == "remove":
        mainTitle = tk.Label(root, text="SELECT PLAYLIST TO REMOVE SONGS FROM", font=("Arial", 30))
    elif playlistFunc == "rename":
        mainTitle = tk.Label(root, text="SELECT PLAYLIST TO RENAME", font=("Arial", 30))
    elif playlistFunc == "delete":
        mainTitle = tk.Label(root, text="SELECT PLAYLIST TO DELETE", font=("Arial", 30))
    mainTitle.pack()
    viewplaylistFrame = tk.Frame(root)
    viewplaylistFrame.pack(fill="both", expand=True)
    viewplaylistScrollbar = tk.Scrollbar(viewplaylistFrame)
    viewplaylistScrollbar.pack(side="right", fill="y")
    viewplaylistListBox = tk.Listbox(viewplaylistFrame, yscrollcommand=viewplaylistScrollbar.set, font=("Arial", 18))

    playlistNames = list(userFile[currentUser]["playlists"].keys())

    if playlistNames: #Confirms that the user actually has playlists in their profile
        for i in playlistNames:
            viewplaylistListBox.insert(tk.END, i)

    viewplaylistListBox.pack(side="left", fill="both", expand=True)

    backButton = tk.Button(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: editPlaylists(root, currentUser))
    backButton.pack(pady=25)

    viewplaylistListBox.bind("<<ListboxSelect>>", lambda event: processPlaylist(event, root, currentUser, playlistFunc, playlistNames))

def processPlaylist(event, root, currentUser, playlistFunc, playlistNames):
    widget = event.widget #Finds the widget that the user interacted with to determine the song they chose
    index = widget.curselection()[0] #Finds the index of the song that the user chose
    selectedPlaylist = playlistNames[index] #Obtains the object so the link can be accessed

    if playlistFunc == "add":
        addSongsPlaylist(root, currentUser, selectedPlaylist)
    elif playlistFunc == "remove":
        removeSongsPlaylist(root, currentUser, selectedPlaylist)
    elif playlistFunc == "rename":
        renameChosenPlaylist(root, currentUser, selectedPlaylist)
    elif playlistFunc == "delete":
        confirmPlaylistDeletion(root, currentUser, selectedPlaylist)

def addSongsPlaylist(root, currentUser, currentPlaylist):
    clearScreen(root)
    mainTitle = tk.Label(root, text="ADD SONG", font=("Arial", 30))
    mainTitle.pack()
    libraryFrame = tk.Frame(root)
    libraryFrame.pack(fill="both", expand=True)
    libraryScrollbar = tk.Scrollbar(libraryFrame)
    libraryScrollbar.pack(side="right", fill="y")
    libraryListBox = tk.Listbox(libraryFrame, yscrollcommand=libraryScrollbar.set, font=("Arial", 18))

    for i in sortedSongList:
        libraryListBox.insert(tk.END, f"Song: {i.title}, Artist: {i.artist}, Genre: {i.genre}, Length: {i.length // 60}:{i.length % 60:02d}") #Specifies all the information about each song
        #The length of the song is formatted in a stadard way using :02d in order to include the 0 in single digit numbers
    
    libraryListBox.pack(side="left", fill="both", expand=True)

    backButton = tk.Button(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: mainMenu(root, currentUser))
    backButton.pack(pady=25)

    libraryListBox.bind("<<ListboxSelect>>", lambda event: addSong(event, root, currentUser, currentPlaylist))

def addSong(event, root, currentUser, currentPlaylist):
    widget = event.widget 
    index = widget.curselection()[0]
    selectedSong = sortedSongList[index]

    userFile[currentUser]["playlists"][currentPlaylist].append(selectedSong.title)
    saveUserData()
    editPlaylists(root, currentUser)

def removeSongsPlaylist(root, currentUser, currentPlaylist):
    clearScreen(root)
    mainTitle = tk.Label(root, text="REMOVE SONG", font=("Arial", 30))
    mainTitle.pack()
    libraryFrame = tk.Frame(root)
    libraryFrame.pack(fill="both", expand=True)
    libraryScrollbar = tk.Scrollbar(libraryFrame)
    libraryScrollbar.pack(side="right", fill="y")
    libraryListBox = tk.Listbox(libraryFrame, yscrollcommand=libraryScrollbar.set, font=("Arial", 18))

    for i in userFile[currentUser]["playlists"][currentPlaylist]:
        libraryListBox.insert(tk.END, f"Song: {i}") #Specifies all the information about each song
        #The length of the song is formatted in a stadard way using :02d in order to include the 0 in single digit numbers
    
    libraryListBox.pack(side="left", fill="both", expand=True)

    backButton = tk.Button(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: mainMenu(root, currentUser))
    backButton.pack(pady=25)

    libraryListBox.bind("<<ListboxSelect>>", lambda event: removeSong(event, root, currentUser, currentPlaylist))

def removeSong(event, root, currentUser, currentPlaylist):
    widget = event.widget
    index = widget.curselection()[0]
    selectedSong = widget.get(index).split(",")[0].split(": ")[1] #Ensures its only the name of the song

    userFile[currentUser]["playlists"][currentPlaylist].remove(selectedSong)
    saveUserData()
    editPlaylists(root, currentUser)

def renameChosenPlaylist(root, currentUser, currentPlaylist):
    clearScreen(root)
    newPlaylistName = tk.StringVar()
    mainTitle = tk.Label(root, text="RENAME PLAYLIST", font=("Arial", 30))
    newPlaylistEntry = tk.Entry(root, textvariable=newPlaylistName)
    confirmRenameButton = tk.Button(root, text="Confirm", cursor="hand2", font=("Arial", 18), command=lambda: changePlaylistName(root, currentUser, currentPlaylist, str(newPlaylistName.get())))
    mainTitle.pack(pady=20)
    newPlaylistEntry.pack(pady=20)
    confirmRenameButton.pack(pady=20)

def changePlaylistName(root, currentUser, currentPlaylist, newPlaylistName):
    userFile[currentUser]["playlists"][newPlaylistName] = userFile[currentUser]["playlists"].pop(currentPlaylist) #replaces the key, which is the name of the playlist
    saveUserData()
    editPlaylists(root, currentUser)

def confirmPlaylistDeletion(root, currentUser, currentPlaylist):
    clearScreen(root)
    mainTitle = tk.Label(root, text="CONFIRM PLAYLIST DELETION", font=("Arial", 30))
    confirmText = tk.Label(root, text=f"Are you sure you want to delete the playlist {currentPlaylist}?", font=("Arial", 18))
    yesButton = tk.Button(root, text="Yes", cursor="hand2", font=("Arial", 18), command=lambda: deletePlaylist(root, currentUser, currentPlaylist))
    noButton = tk.Button(root, text="No", cursor="hand2", font=("Arial", 18), command=lambda: mainMenu(root, currentUser))
    mainTitle.pack(pady=20)
    confirmText.pack(pady=20)
    yesButton.pack(pady=20)
    noButton.pack(pady=20)

def deletePlaylist(root, currentUser, currentPlaylist):
    userFile[currentUser]["playlists"].pop(currentPlaylist)
    saveUserData()
    mainMenu(root, currentUser)

def createPlaylists(root, currentUser):
    clearScreen(root)
    newPlaylistName = tk.StringVar()
    mainTitle = tk.Label(root, text="CREATE PLAYLISTS", font=("Arial", 30))
    newPlaylistLabel = tk.Label(root, text="Name of new playlist:", font=("Arial", 18))
    newPlaylistEntry = tk.Entry(root, textvariable=newPlaylistName)
    confirmPlaylistCreation = tk.Button(root, text="Confirm", cursor="hand2", font=("Arial", 18), command=lambda: createNewPlaylist(root, currentUser, str(newPlaylistName.get())))
    backButton = tk.Button(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: mainMenu(root, currentUser))
    mainTitle.pack(pady=20)
    newPlaylistLabel.pack(pady=20)
    newPlaylistEntry.pack(pady=20)
    confirmPlaylistCreation.pack(pady=20)
    backButton.pack(pady=20)

def createNewPlaylist(root, currentUser, newPlaylistName):
    userFile[currentUser]["playlists"].update({newPlaylistName: []})
    saveUserData()
    mainMenu(root, currentUser)

def autoCreatePlaylists(root, currentUser):
    clearScreen(root)
    newPlaylistName = tk.StringVar()
    timeLimit = tk.StringVar()
    selectedGenre = tk.StringVar(value="None")
    mainTitle = tk.Label(root, text="AUTO GENERATE PLAYLISTS", font=("Arial", 30))
    newPlaylistLabel = tk.Label(root, text="Name of new playlist:", font=("Arial", 18))
    newPlaylistEntry = tk.Entry(root, textvariable=newPlaylistName)
    timeLimitLabel = tk.Label(root, text="Enter in a time limit for the playlist (minutes):", font=("Arial", 18))
    timeLimitEntry = tk.Entry(root, textvariable=timeLimit)
    genreSelectionLabel = tk.Label(root, text="Select a genre for the label to be: ", font=("Arial", 18))
    currentGenreSelected = tk.Label(root, text="Current genre: None", font=("Arial", 18))

    genreFrame = tk.Frame(root)
    genreFrame.columnconfigure(0, weight=1)
    genreFrame.columnconfigure(1, weight=1)
    genreFrame.columnconfigure(2, weight=1)
    genreFrame.columnconfigure(3, weight=1)
    genreFrame.columnconfigure(4, weight=1)
    genreFrame.columnconfigure(5, weight=1)

    metalButton = tk.Button(genreFrame, text="Metal", cursor="hand2", font=("Arial", 18), command=lambda: editGenre(currentGenreSelected, selectedGenre, "Metal"))
    metalButton.grid(row=0, column=0)
    grungeButton = tk.Button(genreFrame, text="Grunge", cursor="hand2", font=("Arial", 18), command=lambda: editGenre(currentGenreSelected, selectedGenre, "Grunge"))
    grungeButton.grid(row=0, column=1)
    popButton = tk.Button(genreFrame, text="Pop", cursor="hand2", font=("Arial", 18), command=lambda: editGenre(currentGenreSelected, selectedGenre, "Pop"))
    popButton.grid(row=0, column=2)
    rapButton = tk.Button(genreFrame, text="Rap", cursor="hand2", font=("Arial", 18), command=lambda: editGenre(currentGenreSelected, selectedGenre, "Rap"))
    rapButton.grid(row=0, column=3)
    indieButton = tk.Button(genreFrame, text="Indie", cursor="hand2", font=("Arial", 18), command=lambda: editGenre(currentGenreSelected, selectedGenre, "Indie"))
    indieButton.grid(row=0, column=4)
    noneButton = tk.Button(genreFrame, text="None (All genres)", cursor="hand2", font=("Arial", 18), command=lambda: editGenre(currentGenreSelected, selectedGenre, "None"))
    noneButton.grid(row=0, column=5)

    errorMessage = tk.Label(root, text="", font=("Arial", 18), fg="red")
    confirmButton = tk.Button(root, text="Confirm", cursor="hand2", font=("Arial", 18), command=lambda: autoCreateNewPlaylist(root, currentUser, str(timeLimit.get()), str(newPlaylistName.get()), str(selectedGenre.get()), errorMessage))
    backButton = tk.Button(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: mainMenu(root, currentUser))

    mainTitle.pack(pady=20)
    newPlaylistLabel.pack(pady=20)
    newPlaylistEntry.pack(pady=20)
    timeLimitLabel.pack(pady=20)
    timeLimitEntry.pack(pady=20)
    genreSelectionLabel.pack(pady=20)
    currentGenreSelected.pack(pady=20)
    genreFrame.pack(pady=20)
    errorMessage.pack()
    confirmButton.pack(pady=20)
    backButton.pack(pady=20)

def editGenre(currentGenreSelected, selectedGenre, newGenre):
    selectedGenre.set(newGenre)
    currentGenreSelected.configure(text=f"Current genre: {newGenre}")

def autoCreateNewPlaylist(root, currentUser, timeLimit, newPlaylistName, selectedGenre, errorMessage):
    if not timeLimit.isnumeric():
        errorMessage.configure(text="You did not enter in a valid number, please try again.")
        return
    
    playlist = []
    currentTime = int(timeLimit)

    for i in sortedSongList:
        if (i.genre == selectedGenre or selectedGenre == "None") and currentTime > (i.length // 60):
            currentTime -= (i.length // 60)
            playlist.append(i.title)
    
    if playlist == []:
        errorMessage.configure(text="You did not enter in a long enough time.")
        return
    
    userFile[currentUser]["playlists"].update({newPlaylistName: playlist})
    saveUserData()
    mainMenu(root, currentUser)

#Functionality for the library menu

def libraryMenu(root, currentUser): #Shows a variety of songs which the user can click on to play
    clearScreen(root)
    mainTitle = tk.Label(root, text="LIBRARY MENU", font=("Arial", 30))
    mainTitle.pack()
    libraryFrame = tk.Frame(root)
    libraryFrame.pack(fill="both", expand=True)
    libraryScrollbar = tk.Scrollbar(libraryFrame)
    libraryScrollbar.pack(side="right", fill="y")
    libraryListBox = tk.Listbox(libraryFrame, yscrollcommand=libraryScrollbar.set, font=("Arial", 18))

    for i in sortedSongList:
        libraryListBox.insert(tk.END, f"Song: {i.title}, Artist: {i.artist}, Genre: {i.genre}, Length: {i.length // 60}:{i.length % 60:02d}") #Specifies all the information about each song
        #The length of the song is formatted in a stadard way using :02d in order to include the 0 in single digit numbers
    
    libraryListBox.pack(side="left", fill="both", expand=True)

    backButton = tk.Button(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: mainMenu(root, currentUser))
    backButton.pack(pady=25)

    libraryListBox.bind("<<ListboxSelect>>", lambda event: songSelected(event)) #Creates functionality for when the user clicks on a song

def songSelected(event): #I wouldve built in the music into the app but i dont want to be copyrighted
    widget = event.widget #Finds the widget that the user interacted with to determine the song they chose
    index = widget.curselection()[0] #Finds the index of the song that the user chose
    selectedSong = sortedSongList[index] #Obtains the object so the link can be accessed

    webbrowser.open(selectedSong.link) #Opens the song the user selected in a new browser window in spotify and automatically plays

#Functionality for changing the favourite genre of the user

def changeFavouriteGenre(newFavGenre, currentUser, root):
    userFile[currentUser]["favGenre"] = newFavGenre
    saveUserData()
    clearScreen(root)
    mainMenu(root, currentUser)

def editFavouriteGenre(root, currentUser):
    clearScreen(root)
    newFavGenre = tk.StringVar()
    mainTitle = tk.Label(root, text="EDIT FAVOURITE GENRE", font=("Arial", 30))
    enterGenre = tk.Label(root, text="Enter your favourite genre:", font=("Arial", 18))
    genreEntry = tk.Entry(root, textvariable=newFavGenre)
    confirmButton = tk.Button(root, text="Confirm", cursor="hand2", font=("Arial", 18))

    confirmButton.configure(command=lambda: changeFavouriteGenre(str(newFavGenre.get()), currentUser, root))

    mainTitle.pack(pady=20)
    enterGenre.pack(pady=20)
    genreEntry.pack(pady=20)
    confirmButton.pack(pady=20)

#Functionality for changing the favourite artist of the user

def changeFavouriteArtist(newFavArtist, currentUser, root):
    userFile[currentUser]["favArtist"] = newFavArtist
    saveUserData()
    clearScreen(root)
    mainMenu(root, currentUser)

def editFavouriteArtist(root, currentUser):
    clearScreen(root)
    newFavArtist = tk.StringVar()
    mainTitle = tk.Label(root, text="EDIT FAVOURITE ARTIST", font=("Arial", 30))
    enterArtist = tk.Label(root, text="Enter your favourite artist:", font=("Arial", 18))
    artistEntry = tk.Entry(root, textvariable=newFavArtist)
    confirmButton = tk.Button(root, text="Confirm", cursor="hand2", font=("Arial", 18))

    confirmButton.configure(command=lambda: changeFavouriteArtist(str(newFavArtist.get()), currentUser, root))

    mainTitle.pack(pady=20)
    enterArtist.pack(pady=20)
    artistEntry.pack(pady=20)
    confirmButton.pack(pady=20)

#The main menu where all functions of the program are accessible

def mainMenu(root, currentUser):
    clearScreen(root)
    mainTitle = tk.Label(root, text="MAIN MENU", font=("Arial", 30))
    artistButton = tk.Button(root, text="Edit favourite artist", cursor="hand2", font=("Arial", 18), command=lambda: editFavouriteArtist(root, currentUser))
    genreButton = tk.Button(root, text="Edit favourite genre", cursor="hand2", font=("Arial", 18), command=lambda: editFavouriteGenre(root, currentUser))
    libraryButton = tk.Button(root, text="View song library", cursor="hand2", font=("Arial", 18), command=lambda: libraryMenu(root, currentUser))
    playlistButton = tk.Button(root, text="Playlists", cursor="hand2", font=("Arial", 18), command=lambda: playlistMenu(root, currentUser))
    discographyButton = tk.Button(root, text="Artist discography", cursor="hand2", font=("Arial", 18), command=lambda: artistDiscography(root, currentUser))
    genreButton = tk.Button(root, text="View genres", cursor="hand2", font=("Arial", 18), command=lambda: artistDiscography(root, currentUser))
    quitButton = tk.Button(root, text="Quit", command=root.destroy, cursor="hand2", font=("Arial", 18))

    mainTitle.pack(pady=20)
    artistButton.pack(pady=20)
    genreButton.pack(pady=20)
    libraryButton.pack(pady=20)
    playlistButton.pack(pady=20)
    discographyButton.pack(pady=20)
    genreButton.pack(pady=20)
    quitButton.pack(pady=20)

# Functionality for the user logging in

def loginScreen(root):
    clearScreen(root)
    inputUsername = tk.StringVar()
    inputPassword = tk.StringVar()
    mainTitle = tk.Label(root, text="USER LOGIN", font=("Arial", 30))
    usernameLabel = tk.Label(root, text="Username: ", font=("Arial", 18))
    usernameEntry = tk.Entry(root, textvariable=inputUsername)
    passwordLabel = tk.Label(root, text="Password: ", font=("Arial", 18))
    passwordEntry = tk.Entry(root, textvariable=inputPassword)
    errorMessage = tk.Label(root, text="", font=("Arial", 14), fg="red")

    loginButton = tk.Button(root, text="Log In", cursor="hand2", font=("Arial", 18), command=lambda: userLogin(inputUsername, inputPassword, errorMessage, root))

    backButton = tk.Button(root, text="Go Back", cursor="hand2", font=("Arial", 18))
    backButton.configure(command=lambda: main(root))

    mainTitle.pack(pady=20)
    usernameLabel.pack(pady=5)
    usernameEntry.pack(pady=20)
    passwordLabel.pack(pady=5)
    passwordEntry.pack(pady=20)
    errorMessage.pack(pady=5)
    loginButton.pack(pady=20)
    backButton.pack(pady=50)

def userLogin(inputUsername, inputPassword, errorMessage, root):
    username = inputUsername.get()
    password = inputPassword.get()
    if not username in userFile:
        errorMessage.config(text="The username you entered does not exist. Please try again.")
    elif userFile[username]["password"] != password:
        errorMessage.config(text="The password you entered is incorrect. Please try again.")
    else:
        errorMessage.config(text="Logging in...", fg="green")
        clearScreen(root)
        mainMenu(root, str(username))

#Functionality for signing up

def signUpScreen(root):
    clearScreen(root)

    inputUsername = tk.StringVar()
    inputPassword = tk.StringVar()
    realName = tk.StringVar()
    userDay = tk.StringVar()
    userMonth = tk.StringVar()
    userYear = tk.StringVar()

    mainTitle = tk.Label(root, text="USER REGISTRATION", font=("Arial", 30))

    usernameLabel = tk.Label(root, text="Username: ", font=("Arial", 18))
    usernameEntry = tk.Entry(root, textvariable=inputUsername)

    passwordLabel = tk.Label(root, text="Password: ", font=("Arial", 18))
    passwordEntry = tk.Entry(root, textvariable=inputPassword)

    realNameLabel = tk.Label(root, text="Real name: ", font=("Arial", 18))
    realNameEntry = tk.Entry(root, textvariable=realName)

    dobLabel = tk.Label(root, text="Date of birth (DD/MM/YYYY): ", font=("Arial", 18))
    dobFrame = tk.Frame(root)
    dobFrame.columnconfigure(0, weight=1)
    dobFrame.columnconfigure(1, weight=1)
    dobFrame.columnconfigure(2, weight=1)

    dayEntry = tk.Entry(dobFrame, textvariable=userDay)
    dayEntry.grid(row=0, column=0)
    monthEntry = tk.Entry(dobFrame, textvariable=userMonth)
    monthEntry.grid(row=0, column=1)
    yearEntry = tk.Entry(dobFrame, textvariable=userYear)
    yearEntry.grid(row=0, column=2)

    favArtist = tk.StringVar()
    favGenre = tk.StringVar()

    artistLabel = tk.Label(root, text="Favourite artist: ", font=("Arial", 18))
    artistEntry = tk.Entry(root, textvariable=favArtist)
    genreLabel = tk.Label(root, text="Favourite genre: ", font=("Arial", 18))
    genreEntry = tk.Entry(root, textvariable=favGenre)

    errorMessage = tk.Label(root, text="", font=("Arial", 14), fg="red")

    completeSignupButton = tk.Button(root, text="Sign Up", cursor="hand2", font=("Arial", 18))
    completeSignupButton.configure(command=lambda: userRegistration(inputUsername, inputPassword, realName, userDay, userMonth, userYear, favArtist, favGenre, errorMessage, root))

    backButton = tk.Button(root, text="Go Back", cursor="hand2", font=("Arial", 18))
    backButton.configure(command=lambda: main(root))

    mainTitle.pack(pady=20)
    usernameLabel.pack(pady=5)
    usernameEntry.pack(pady=20)
    passwordLabel.pack(pady=5)
    passwordEntry.pack(pady=20)
    realNameLabel.pack(pady=5)
    realNameEntry.pack(pady=5)
    dobLabel.pack(pady=5)
    dobFrame.pack(fill="x")
    artistLabel.pack(pady=5)
    artistEntry.pack(pady=5)
    genreLabel.pack(pady=5)
    genreEntry.pack(pady=5)
    errorMessage.pack(pady=5)
    completeSignupButton.pack(pady=5)
    backButton.pack(pady=20)

def userRegistration(inputUsername, inputPassword, realName, userDay, userMonth, userYear, favArtist, favGenre, errorMessage, root):

    username = inputUsername.get()
    password = inputPassword.get()
    name = realName.get()
    dobDay = userDay.get()
    dobMonth = userMonth.get()
    dobYear = userYear.get()
    artist = favArtist.get()
    genre = favGenre.get()

    #A lot of if/elif statements to specifically tell the user what the error is when registering an account

    if not username.isalnum():
        errorMessage.config(text="The username you entered contains spaces or special characters. Only letters a-z and numbers 0-9 are allowed.")
    elif len(username) < 4:
        errorMessage.config(text="The username you entered is shorter than 4 characters. Please try again.")
    elif len(username) > 20:
        errorMessage.config(text="The username you entered is longer than 20 characters. Please try again.")
    elif username in userFile:
        errorMessage.config(text="The username you entered has already been taken. Please try again.")

    elif " " in password:
        errorMessage.config(text="The password you entered contains a spacebar. Please try again.")
    elif len(password) < 8:
        errorMessage.config(text="The password you entered is shorter than 8 characters. Please try again.")
    elif len(password) > 50:
        errorMessage.config(text="The password you entered is longer than 50 characters. Please try again.")

    elif not name.isalpha():
        errorMessage.config(text="The name you entered is invalid. Please make sure to only use characters a-z")

    elif not dobDay.isnumeric():
        errorMessage.config(text="The day of your birthday is not in numbers. Please try again.")
    elif not dobMonth.isnumeric():
        errorMessage.config(text="The month of your birthday is not in numbers. Please try again.")
    elif not dobYear.isnumeric():
        errorMessage.config(text="The year of your birthday is not in numbers. Please try again.")

    elif int(dobYear) > 2024 or int(dobYear) < 1900:
        errorMessage.config(text="The year you entered is invalid. Make sure the year is between 1900-2024.")
    elif int(dobMonth) > 12 or int(dobMonth) < 1:
        errorMessage.config(text="The month you entered is invalid. Please try again.")


    elif int(dobDay) < 1:
        errorMessage.config(text="The day you entered is invalid. Please try again.")
    elif (int(dobDay) > 28 and int(dobMonth) == 2 and int(dobYear) % 4 != 0) or (int(dobDay) > 29 and int(dobMonth) == 2 and int(dobYear) % 4 == 0): #Taking leap years into consideration
        errorMessage.config(text="The day you entered is invalid. Please try again.")
    elif (int(dobMonth) == 4 or int(dobMonth) == 6 or int(dobMonth) == 9 or int(dobMonth) == 11) and int(dobDay) > 30:
        errorMessage.config(text="The day you entered is invalid. Please try again.")
    elif (int(dobMonth) == 1 or int(dobMonth) == 3 or int(dobMonth) == 5 or int(dobMonth) == 7 or int(dobMonth) == 8 or int(dobMonth) == 10 or int(dobMonth) == 12) and int(dobDay) > 31:
        errorMessage.config(text="The day you entered is invalid. Please try again.")
    
    else:
        errorMessage.config(text="Creating account...", fg="green")

        userFile.update({str(username): { #Format used in order to save data
            "username": str(username),
            "password": str(password),
            "realName": str(name),
            "dob": f"{str(dobDay)}/{str(dobMonth)}/{str(dobYear)}",
            "favArtist": str(artist),
            "favGenre": str(genre),
            "playlists": {}
        }})

        saveUserData()
        clearScreen(root)
        mainMenu(root, str(username))

def main(root): #Login Screen
    clearScreen(root)
    root.geometry("1440x900")
    root.title("OCRtunes")

    mainTitle = tk.Label(root, text="LOGIN/SIGNUP", font=("Arial", 30))
    logInButton = tk.Button(root, text="Log In", cursor="hand2", font=("Arial", 18), command=lambda: loginScreen(root))
    signUpButton = tk.Button(root, text="Sign Up", cursor="hand2", font=("Arial", 18), command=lambda: signUpScreen(root))
    quitButton = tk.Button(root, text="Quit", command=root.destroy, cursor="hand2", font=("Arial", 18))

    mainTitle.pack(pady=50)
    logInButton.pack(pady=50)
    signUpButton.pack(pady=50)
    quitButton.pack(pady=50)

    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    main(root)