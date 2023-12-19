import os
import eyed3
import yaml
from datetime import timedelta

# This function takes a file name, loads the audio file, extracts the necessary information,
# and returns it as a dictionary.
def get_audio_file_info(file):
    # Construct the full path of the file
    audio_file_path = os.path.join('audio', file)
    # Load the audio file
    audio_file = eyed3.load(audio_file_path)
    # Extract and join all comments in the audio file
    comments = ' '.join(comment.text for comment in audio_file.tag.comments)
    # Format the duration of the audio file
    duration = format_duration(audio_file.info.time_secs)
    # Get the size of the file in bytes and format it with commas as thousand separators
    size = format(os.path.getsize(audio_file_path), ',')
    # Return the extracted information as a dictionary
    return {'title': audio_file.tag.title, 'description': comments, 'file': '/audio/' + file, 'duration': duration, 'length': size}

# This function takes a duration in seconds and returns it as a string in the format HH:MM:SS.
def format_duration(seconds):
    return str(timedelta(seconds=int(seconds)))

# This function lists all .mp3 files in the 'audio' directory and returns their information as a list of dictionaries.
def get_audio_files():
    audio_files = []
    for file in os.listdir('audio'):
        if file.endswith('.mp3'):
            audio_files.append(get_audio_file_info(file))
    return audio_files

# This function writes the information of all audio files to a YAML file.
def main():
    with open('episodes.yaml', 'w') as file:
        yaml.dump(get_audio_files(), file,
                  default_flow_style=False, sort_keys=False)

# If this script is run as the main program, execute the main function.
if __name__ == "__main__":
    main()