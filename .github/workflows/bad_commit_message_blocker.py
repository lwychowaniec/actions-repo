import sys
from curses.ascii import isupper


def contains_review_leftover(message: str) -> bool:
    lowercase = message.lower()
    words = lowercase.split()
    for word in words:
        if (word == 'cr') | (word == 'wip'):
            print('Detected review leftover in commit message')
            return True


def is_suspiciously_short(message: str) -> bool:
    if len(message) <= 7:
        print("Suspiciously short commit message")
        return True
    return False


def doesnt_start_with_capital_letter(message: str) -> bool:
    if ':' in message:
        index_after_colon = message.index(':') + 1
        after_tags = message[index_after_colon:]
        return (after_tags[0] == ' ') & (isupper(after_tags[1]))
    else:
        return isupper(message[0])


def main():
    message = sys.argv[1]
    if contains_review_leftover(message) | is_suspiciously_short(message) | doesnt_start_with_capital_letter(message):
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
