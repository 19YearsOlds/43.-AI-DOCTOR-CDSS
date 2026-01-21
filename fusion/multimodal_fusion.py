from utils.math import normalize

def fuse(text_score, image_score, audio_score):
    return normalize([text_score, image_score, audio_score])