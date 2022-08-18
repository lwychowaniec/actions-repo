import re
import sys
from curses.ascii import isupper

ALLOWED_TAGS_PATTERS = ['^[A-Z]+-[0-9]+$', '^[A-Z][a-z]+(Api)?(_[a-z]{2})?$', '^\\(?KONTOMATIK-[A-Z]{3,}\\)?$']


def main(message: str):
    if contains_review_leftover(message) or is_suspiciously_short(message):
        sys.exit(1)
    message_valid = is_title_valid(message) and are_tags_valid(message)
    sys.exit(0 if message_valid else 1)


def contains_review_leftover(message: str) -> bool:
    lowercase = message.lower()
    words = lowercase.split()
    for word in words:
        if (word == 'cr') or (word == 'wip'):
            print('Detected review leftover in commit message')
            return True


def is_suspiciously_short(message: str) -> bool:
    if len(message) <= 7:
        print("Suspiciously short commit message")
        return True
    return False


def is_title_valid(message: str) -> bool:
    if ':' in message:
        index_after_colon = message.index(':')
        if message[index_after_colon] == ' ':
            print('Colon separating title from tags should be followed by blank space')
            return False
    title = fetch_title(message)
    return (isupper(title[0])) and (not (title[-1] in '.,?!'))


def fetch_title(message: str) -> str:
    if ':' in message:
        title_first_index = message.index(':') + 2
        return message[title_first_index:]
    else:
        return message


def are_tags_valid(message: str) -> bool:
    tags = fetch_tags(message)
    for tag in tags:
        if not matches_any_known_tag(tag):
            print('Tag ' + tag + " doesn't match any known tag pattern")
            return False
    return True


def fetch_tags(message: str) -> list:
    if ':' in message:
        colon_index = message.index(':')
        raw_tags = message[:colon_index]
        return raw_tags.split()
    else:
        return []


def matches_any_known_tag(tag: str) -> bool:
    for pattern in ALLOWED_TAGS_PATTERS:
        if re.match(pattern, tag):
            return True
    return False


if __name__ == "__main__":
    main(sys.argv[1])
