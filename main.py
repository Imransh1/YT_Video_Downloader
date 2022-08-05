from pytube import YouTube
from pytube import Playlist
import os

x = 0
i = 1

def downloader(link):
    global i,x
    try:
        yt = YouTube(link)
        # Check for the link on YouTube
    except:
        x = 1
        # Using variable x to let the Menu functions know 
        # about errors/exceptions 
        # 0 = No Error, 1 = Connection error, 2 = Download error.

        print("\nConnection Error")
        # Incase there's a connection error this will execute.

    if x== 0:
        try:
            print(f'Downloading: {yt.title}')
            # Display which file is being downloaded

            yd = yt.streams.get_highest_resolution().download(r'C:\Users\Asus\Downloads\YT_Downloads') # Your path goes here
            # Get the highest resolution available for download
            # And download to the specified path.

            last_backslash = yd.rfind("\\")
            res = list(yd)
            res.insert(last_backslash + 1, str(i) + " ")
            res = ''.join(res)
            os.rename(yd, str(res))
            i+=1
            # Rename downloaded file names
            # Using variable i to add a serial number to downloaded files 
        except:
            x = 2
            print(f'\nCould Not Download: {yt.title}')
            # Incase of Download error this will be excecuted.
            Menu()



def Menu():
    global x
    select = input("""
                                                        |-------------------------------------|
                                                        |    Enter 1 to Download A Video      |
                                                        |    Enter 2 to Download A Playlist   |
                                                        |    Enter 3 to Exit                  |
                                                        |-------------------------------------|    
                    \nChoose Option: """)
    if select == '1':
        v_link = input('\nEnter Link To Video: ')
        downloader(v_link)
        if x == 2:
            print("Error: Check Your URL")
            Menu()
        else:
            Menu()
    elif select == '2':
        p_link = input('\nEnter Link To Playlist: ')
        try:
            p = Playlist(p_link)
            try:
                for url in p.video_urls:
                    downloader(url)
                    if x == 1 or x == 2:
                        break

            except:
                    print('\nError: Could Not Fetch The URL')
                    Menu()
        except:
            print('\nSome Error: Please Check The Link And Try Again!')
            Menu()
    elif select == '3':
        exit()
    else:
        print("""
                                                        Error: Choose Correct Option\n""")
        Menu()
    
    # Menu function to display the available options
    # And perform operations accordingly 
        
Menu()
