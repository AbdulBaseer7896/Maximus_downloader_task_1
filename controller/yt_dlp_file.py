import yt_dlp

# ydl_opts = {
#     'format': 'best',  # You can customize the format based on resolution preferences
# }

class dlp:
    "This class is used for yt_dlp. In this class I make the functions which download the video using its URL"
    def get_video_info(url, ydl_opts):
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            filename_template = ydl.prepare_filename(info_dict)
            return filename_template

    def download_video(url,  ydl_opts):
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

obj = dlp 
format = {'format': 'best'}

obj.download_video('https://www.youtube.com/watch?v=hr3KIb_Buvk' , format)

