import config_file

import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

# create a speech recognition object
r = sr.Recognizer()

# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)  
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    if config_file.logs: print("create a directory to store the audio chunks")
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    if config_file.logs: print("process each chunk") 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            if config_file.logs: print(f"trying to recognize chunk{i}.wav")
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
                if config_file.logs: print(f"chunk{i}.wav recognize with great SUCCESS")
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                if config_file.logs: print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    return whole_text

def create_txt_file(whole_output_text):
    if config_file.logs: print(f"write result to file {whole_output_text}")
    fp = open(config_file.output_file_path, 'w+')
    fp.write(whole_output_text)
    fp.close()
    return

def main_mod():
    transcripted_txt = get_large_audio_transcription(config_file.input_wav_file_path)
    if config_file.output_file_path != None:
        create_txt_file(whole_output_text=transcripted_txt)
        return 
    print(transcripted_txt)
    return

main_mod()
