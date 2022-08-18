import re
import sys
from curses.ascii import isupper

ALLOWED_TAGS_PATTERS = ['^[a-zA-z]+-[0-9]+$', '^[A-Z][a-z]+(Api)?(_\\w{2})?$', '^\\(?KONTOMATIK-[\\w]{3,}\\)?$', '^Statements$']


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
            return False
    return True


def matches_any_known_tag(tag: str) -> bool:
    for pattern in ALLOWED_TAGS_PATTERS:
        if re.match(pattern, tag):
            return True
    return False


def fetch_tags(message: str) -> list:
    if ':' in message:
        colon_index = message.index(':')
        raw_tags = message[:colon_index]
        return raw_tags.split()
    else:
        return []


def main():
    message = sys.argv[1]
    if contains_review_leftover(message) or is_suspiciously_short(message) or is_title_valid(message):
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
