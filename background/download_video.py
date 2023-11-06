import certifi
import ssl

# Set the SSL certificate verification context to use the Certifi bundle
ssl._create_default_https_context = ssl._create_unverified_context
ssl._create_default_https_context().load_verify_locations(certifi.where())

from pytube import Search, YouTube

download_path = './media/videos'

def download(query):
  search = Search(query)

  for result in search.results:
    video_title = query
    
    if 90 <= result.length <= 500:
      try:
        stream = result.streams.filter(file_extension='mp4', res='1080p').first()
        if stream:
          stream.download(output_path=download_path, filename=video_title)
          print('Downloaded:', video_title)
          break
        else:
           # attempt with lower quality
           stream = result.streams.filter(file_extension='mp4', res='720p').first()
           stream.download(output_path=download_path, filename=video_title)
           print('Downloaded:', video_title)
           break
      except Exception as e:
         print('No suitable video found/failed to download for:', video_title)
         print('Error:', e)
  
  return video_title