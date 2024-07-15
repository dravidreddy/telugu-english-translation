from deep_translator import GoogleTranslator
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

# Function to translate English literal to telugu
def transliterate_text(text):
    telugu_script = transliterate(text, sanscript.ITRANS, sanscript.TELUGU)
    return telugu_script

# Function to translate Telugu to English
def translate_te_to_en(text):
  translator = GoogleTranslator(source='te', target='en')  # Telugu (te) to English (en)
  translated_text = translator.translate(text)
  return translated_text

# Example usage
telugu_text = input("Enter the text to translate : ")  # How are you? (in Telugu)
literal = transliterate_text(telugu_text)
english_text = translate_te_to_en(literal)
print(f"Telugu: {telugu_text}")
print(f"English: {english_text}")
