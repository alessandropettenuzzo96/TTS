import re
from num2words import num2words

_time_re = re.compile(
    r"""\b
                          ((0?[0-9])|(1[0-1])|(1[2-9])|(2[0-3]))  # hours
                          :
                          ([0-5][0-9])                            # minutes
                          \s*(a\\.m\\.|am|pm|p\\.m\\.|a\\.m|p\\.m)? # am/pm
                          \b""",
    re.IGNORECASE | re.X,
)


def _expand_num(n: int) -> str:
    return num2words(n, lang="it")


def _expand_time_italian(match: "re.Match") -> str:
    hour = int(match.group(1))
    past_noon = False
    time = []
    if hour == 12:
        hour = "mezzogiorno"
    elif hour == 0:
        hour = "mezzanotte"
    else:
        time.append(_expand_num(hour))

    minute = int(match.group(6))
    if minute > 0:
        time.append(" e ")
        time.append(_expand_num(minute))
    return " ".join(time)


def expand_time_spanish(text: str) -> str:
    return re.sub(_time_re, _expand_time_italian, text)
