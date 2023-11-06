from gtts import gTTS
from moviepy.editor import *
import os

audio_directory = './media/audio/'

def create_audio(sentences):
    print('Creating audio from gTTS...')

    for i, sentence in enumerate(sentences):
        if len(sentence) > 1:
            try:
                filename = f'{i}.mp3'
                filepath = audio_directory + filename
                gTTS(text=sentence, lang='en').save(filepath)
            except Exception as e:
                print('Error when generating text to speech', e)

    print('Done creating audio...')


def create_video(video_name, story):
    original_video = VideoFileClip('./media/videos/' + video_name)

    sentences = [sentence.strip() for sentence in story.split('.') if sentence.strip()]

    # Crop video to 9:16 aspect ratio
    original_video = original_video.crop(x_center=original_video.w/2, y_center=original_video.h/2, width=(original_video.h) * 9/16, height=original_video.h)

    # Create audio for each sentence
    create_audio(sentences)

    video_duration = 0
    audio_clips = []
    video_clips = []

    for i, sentence in enumerate(sentences):
        # Grab audio clip associated with sentence
        sentence_audio_clip = AudioFileClip(audio_directory + f'{i}.mp3').fx(vfx.speedx, 1.5)
        sentence_duration = sentence_audio_clip.duration

        audio_clips.append(sentence_audio_clip)
        
        # Create text clip for current sentence
        text_clip = TextClip(
            sentence, 
            fontsize=25, 
            color='white', 
            size=(original_video.w * 0.9, None),
            align='center',
            method='caption',
            )
        text_clip = text_clip.set_position(('center', 'center'))
        text_clip = text_clip.set_duration(sentence_duration)

        video_clip = CompositeVideoClip([text_clip])

        # Create video clip
        video_clip = video_clip.set_audio(sentence_audio_clip)
        video_clip = video_clip.set_start(video_duration)
        video_clip = video_clip.set_end(video_duration + sentence_duration)

        video_clips.append(video_clip)

        video_duration += sentence_duration

    trimmed_video = original_video.subclip(0, video_duration)

    final_video = CompositeVideoClip([trimmed_video] + video_clips)
    final_video = final_video.set_audio(concatenate_audioclips(audio_clips))
    final_video.write_videofile('./media/final_videos/final_video.mp4', codec='libx264', fps=24)

    if os.path.exists('./media/videos/' + video_name):
        os.remove('./media/videos/' + video_name)

    for i in range(len(sentences)):
        os.remove(audio_directory + f'{i}.mp3')

# to test within the file use this one blow
# audio_directory = '../media/audio/'

# to test within the file use this one
# original_video = VideoFileClip('../media/videos/' + video_name)