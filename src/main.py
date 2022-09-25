from selenium_driver import SeleniumDriver

import playlist

def main():
    selenium_driver = SeleniumDriver()
    # music_playlist = playlist.Playlist()

    selenium_driver.play_song()
if __name__ == "__main__":
    main()