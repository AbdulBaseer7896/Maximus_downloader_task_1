from app import app
from functools import wraps
from flask import session
from flask import redirect , url_for , render_template , request , flash , send_file
import ast , os
from controller.yt_dlp_file import dlp

obj = dlp

@app.route('/index' , methods=["GET", "POST"])
def download_fun():
    if request.method == 'POST':
        data = request.form.to_dict()
        print("This is form data" , data)
        print("This is form data" , data['video_url'])
        format = {'format': 'best'}
        info = obj.download_video(f"{data['video_url']}" , format)
        video_info = obj.get_video_info(f"{data['video_url']}" , format)
        print("Video Name:", video_info)
        
            # Check if the file exists and return it
        if os.path.exists(video_info):
            new_filename = 'file_for_download.mp4'  # Specify the new filename you want
            return send_file(video_info, as_attachment=True, download_name=new_filename)
        # else:
        #     return "File not found"
        return render_template('download_fail_page.html' , download_link = "file_for_download.mp4")
    
    

