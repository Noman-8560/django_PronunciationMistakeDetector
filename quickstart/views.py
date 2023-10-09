# views.py

from django.shortcuts import render
from django.http import JsonResponse
import speech_recognition as sr
import nltk

nltk.download('cmudict')  # Download the CMU Pronouncing Dictionary

from nltk.corpus import cmudict
from nltk.tokenize import word_tokenize


# Load the CMU Pronouncing Dictionary
prondict = cmudict.dict()


def recording_view(request):
    return render(request, 'template.html')

def record_audio(request):
    if request.method == 'POST':
        audio_data = request.POST.get('audio_data')

        if audio_data:
            # Perform speech recognition on the audio data
            recognizer = sr.Recognizer()
            try:
                with sr.AudioFile(audio_data) as source:
                    audio = recognizer.record(source)
                transcribed_text = recognizer.recognize_google(audio)

                # Implement quickstart analysis here
                pronunciation_mistakes = analyze_pronunciation(transcribed_text)

                return JsonResponse({'success': True, 'transcribed_text': transcribed_text, 'pronunciation_mistakes': pronunciation_mistakes})
            except Exception as e:
                return JsonResponse({'success': False, 'error_message': str(e)})

    return JsonResponse({'success': False, 'error_message': 'Invalid request'})

def analyze_pronunciation(transcribed_text):
    pronunciation_mistakes = []

    # Tokenize the transcribed text
    words = word_tokenize(transcribed_text)

    for word in words:
        # Check if the word is in the CMU Pronouncing Dictionary
        if word.lower() in prondict:
            # Retrieve the list of possible phonetic pronunciations for the word
            pronunciations = prondict[word.lower()]

            # For simplicity, check if any quickstart contains numbers (indicating phonetic symbols)
            # This is a basic check and may not cover all quickstart variations
            if any(any(char.isdigit() for char in pronunciation) for pronunciation in pronunciations):
                pronunciation_mistakes.append({'word': word, 'suggestion': 'Check quickstart'})

    return pronunciation_mistakes
