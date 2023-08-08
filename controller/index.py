from app import app
from flask import  render_template , request , send_file
import  os
from controller.yt_dlp_file import dlp

obj = dlp

@app.route('/index', methods=["GET", "POST"])
def download_fun():
    if request.method == 'POST':
        data = request.form.to_dict()
        print("This is form data", data)
        video_quality = request.form['video_quality']
        
        try:
            format = {'format': f'bestvideo[height<={video_quality}]+bestaudio/best[height<={video_quality}]'}
            try:
                obj.download_video(data['video_url'], format)
            except:
                return render_template('download_fail_page.html')
        except:
            format = {'format': 'best'}
            obj.download_video(data['video_url'], format)
        video_info = obj.get_video_info(data['video_url'], format)
        print("Video Name:", video_info)

        # Check if the file exists and return it
        if os.path.exists(video_info):
            new_filename = 'your_download_file.mp4'  # Specify the new filename you want
            return send_file(video_info, as_attachment=True, download_name=new_filename)
        return render_template('download_fail_page.html')

    
    

