from api_requests.openai_requests import send_openai_request
from background.download_video import download
from edit.editor import create_video
import os
os.environ['SSL_CERT_FILE'] = os.environ.get("SSL_FILE_LOCATION")

if __name__ == "__main__":
  story_prompt = input("Enter a story prompt for ChatGPT to generate: ")
  story_response = send_openai_request(story_prompt)
  print("We've got the story! Next step...")

  video_prompt = input("Enter a video game you'd like to play in the background of the video: ")
  video_title = download(video_prompt)
  video_path = f'./media/videos/{video_title}'
  create_video(video_title, story_response)




