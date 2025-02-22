class YoutubeClass:

    #Attributes
    os = __import__("os")
    pytubefix = __import__("pytubefix")
    flag = False
    yt = ""

    #Methods
    def __init__(self):
        print("The process has started...")
    
    def download_video(self, url:str, path:str)->None:
        try:
            # url input from user
            self.yt = self.pytubefix.YouTube(str(url))
            # extract only audio
            video = self.yt.streams.filter(only_audio=True).first()
            # check for destination to save file
            print("Enter the destination (leave blank for current directory)")
            destination = str(path)
            # download the file
            out_file = video.download(output_path=destination)
            # save the file
            base, ext = self.os.path.splitext(out_file)
            new_file = base + '.mp3'
            self.os.rename(out_file, new_file)

            self.flag = True

        except Exception as error:

            print ("ERROR: {}".format(error))


    def __del__(self):
        print("The process has finished...")
        # result of success
        if self.flag:
            print(self.yt.title + " has been successfully downloaded.")
        else:
            print("There was a problem while downloading the video...")
