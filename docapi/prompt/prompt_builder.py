from datetime import datetime
from docapi.prompt import doc_zh, doc_en


lang2name = {
  "en": "English",
  "es": "Spanish",
  "fr": "French",
  "de": "German",
  "ja": "Japanese",
  "ru": "Russian",
  "ar": "Arabic",
  "hi": "Hindi",
  "pt": "Portuguese",
  "bn": "Bengali",
  "ko": "Korean",
  "it": "Italian",
  "tr": "Turkish",
  "vi": "Vietnamese",
  "pl": "Polish",
  "nl": "Dutch",
  "th": "Thai",
  "sv": "Swedish",
  "fi": "Finnish",
  "no": "Norwegian",
  "da": "Danish",
  "cs": "Czech",
  "el": "Greek",
  "hu": "Hungarian",
  "ro": "Romanian",
  "sk": "Slovak",
  "uk": "Ukrainian",
  "id": "Indonesian",
  "ms": "Malay",
  "he": "Hebrew",
  "fa": "Persian",
  "sr": "Serbian",
  "bg": "Bulgarian",
  "hr": "Croatian",
  "lt": "Lithuanian",
  "lv": "Latvian",
  "et": "Estonian",
  "sl": "Slovenian"
}


def build_prompt(lang, template):
    if lang == "zh":
        time = datetime.now().strftime('%Y-%m-%d %H:%M')
        template = template.format(datetime=time)
        doc_zh.system = doc_zh.system.format(template=template)
        return doc_zh
    else:
        time = datetime.now().strftime('%Y-%m-%d %H:%M')
        template = template.format(datetime=time)
        doc_en.system = doc_en.system.format(lang=lang2name.get(lang, 'English'), template=template)
        return doc_en
