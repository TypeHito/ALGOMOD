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
    url_regex = r"(https?:\/\/)([\w\.-]+(:\d+)?(\/[\w\.-]*)*\/?)"
    return re.sub(url_regex, "", text)


async def translate(text, language):
    text = remove_urls(text)
    for key in language:
        text = replace_text(text, language[key]['from'], language[key]['to'])
    return text
