from selenium_driver import SeleniumDriver

import playlist

def main():
    # selenium_driver = SeleniumDriver()
    music_playlist = playlist.Playlist()
    music_playlist.add_entry("https://www.youtube.com/watch?v=6s4_EWHzv_o&list=FLhPx5RAYjdns77CKe7Vn2tA&index=19")
    music_playlist.print_collection()

    # selenium_driver.play_song()
if __name__ == "__main__":
    main()