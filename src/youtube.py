from youtubesearchpython import VideosSearch

class YouTubeSearch:
    def __init__(self):
        self.music_url = ""
        self.music_title = ""

        self.search_song_meta_data()

    # ----------------------------------------
    # Public Methods
    # ----------------------------------------

    def search_song_meta_data(self, song_name):
        # video_search = VideosSearch("Post Malone Circles", limit=1, language="en", region="US")
        video_search = VideosSearch(song_name, limit=1, language="en", region="US")
        search_result = video_search.result()
        
        search_result_list = search_result["result"]

        for link in search_result_list:
            self.music_title = link["title"]
            self.music_url = link["link"]

    def get_music_url(self):
        print (self.music_url)
        return self.music_url
    
    def get_music_title(self):
        print(self.music_title)
        return self.music_title

    # ----------------------------------------
    # Private Methods
    # ----------------------------------------

if __name__ == "__main__":
    youtube_obj = YouTubeSearch()

    youtube_obj.get_music_url()