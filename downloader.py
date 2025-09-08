import yt_dlp

def audio_downloader(urls,folder_selected,logger=print):  
        for url in urls:
            logger(f"Starting download for {url}")
            #IS AN AUDIO PLAYLIST
            if "playlist?list" in url or "&list=" in url:
                outtmpl = f'{folder_selected}/'+'%(playlist_title)s/%(title)s.%(ext)s'
                youtube_dl_opt = {
                'format': 'bestaudio/best',
                'ignoreerrors': True,
                'outtmpl': outtmpl,
                'postprocessors': [
                    {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }
                                ]
                                }
                try:
                    with yt_dlp.YoutubeDL(youtube_dl_opt) as ydo:
                        ydo.download([url])
                except yt_dlp.utils.DownloadError:
                    print("One of the videos required sign-in.")

            #NOT AN AUDIO PLAYLIST
            else:
                outtmpl = f'{folder_selected}/'+'%(title)s.%(ext)s'
                youtube_dl_opt = {
                'format': 'bestaudio/best',
                'ignoreerrors': True,
                'outtmpl': outtmpl,
                'postprocessors': [
                    {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }
                                ]
                                }
                try:
                    with yt_dlp.YoutubeDL(youtube_dl_opt) as ydo:
                        ydo.download([url])
                except yt_dlp.utils.DownloadError:
                    print("One of the videos required sign-in.")
                    continue


def video_downloader(urls,folder_selected,logger=print):
        for url in urls:
            logger(f"Starting download for {url}")
            #IS A VIDEO PLAYLIST
            if "playlist?list" in url or "&list=" in url:
                outtmpl = f'{folder_selected}/'+'%(playlist_title)s/%(title)s.%(ext)s'
                print(outtmpl)
                youtube_dl_opt = {
                'format': 'bestvideo+bestaudio/best',
                'ignoreerrors': True,
                'outtmpl': outtmpl,
                'merge_output_format': 'mp4',
                'writesubtitles': True,
                'subtitleslangs': ['en'],
                'subtitlesformat': 'srt'
                                }
                try:
                    with yt_dlp.YoutubeDL(youtube_dl_opt) as ydo:
                        ydo.download([url])
                except yt_dlp.utils.DownloadError:
                    print("One of the videos required sign-in.")
                    continue
             #NOT A VIDEO PLAYLIST       
            else:
                outtmpl = f'{folder_selected}/'+'%(title)s.%(ext)s'
                print(outtmpl)
                youtube_dl_opt = {
                'format': 'bestvideo+bestaudio/best',
                'ignoreerrors': True,
                'outtmpl': outtmpl,
                'merge_output_format': 'mp4',
                'writesubtitles': True,
                'subtitleslangs': ['en'],
                'subtitlesformat': 'srt'
                                }
                try:
                    with yt_dlp.YoutubeDL(youtube_dl_opt) as ydo:
                        ydo.download([url])
                except yt_dlp.utils.DownloadError:
                    print("One of the videos required sign-in.")
                    continue