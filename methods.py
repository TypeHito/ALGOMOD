import re


def replace_text(text, from_text, to_text):
    """
    text: The text to search.
    from_text: The text to replace all occurrences of the pattern with.
    to_text: The text to replace all occurrences of the pattern with.

    Returns:
        A new string with all occurrences of the pattern replaced by replace_text.
    """
    regex = r"(?i)" + from_text
    return re.sub(regex, to_text, text)


def remove_urls(text):
    """
    text: Строка текста.
    Returns:
        Строка текста без ссылок.
    """
    url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    t_regex = r"t\.me"
    user_regex = r"@"
    url_detect = re.search(url_regex, text)
    t_detect = re.search(t_regex, text)
    user_detect = re.search(user_regex, text)

    if url_detect or user_detect or t_detect:
        return True
    else:
        return False


async def translate(text, language):
    for key in language:
        text = replace_text(text, language[key]['from'], language[key]['to'])
    return text

