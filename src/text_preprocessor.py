import re

def escape_ssml(text: str) -> str:
    return text.replace("&", "&amp;") \
               .replace("<", "&lt;") \
               .replace(">", "&gt;") \
               .replace('"', "&quot;") \
               .replace("'", "&apos;")

def insert_pauses(text: str, dot="x-strong", comma="strong") -> str:
    text = re.sub(r"\.\s", f".<break strength='{dot}'/> ", text)
    text = re.sub(r",\s", f",<break strength='{comma}'/> ", text)
    return text