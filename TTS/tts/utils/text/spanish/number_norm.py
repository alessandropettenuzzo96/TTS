""" from https://github.com/keithito/tacotron """

import re
from typing import Dict
from num2words import num2words

import inflect

_inflect = inflect.engine()
_comma_number_re = re.compile(r"([0-9][0-9\,]+[0-9])")
_decimal_number_re = re.compile(r"([0-9]+\.[0-9]+)")
_currency_re = re.compile(r"([0-9\,\.]*[0-9]+)|([0-9\,\.]*[0-9]+)(£|\$|¥|€)")
_ordinal_re = re.compile(r"[0-9]+(o|a)")
_number_re = re.compile(r"-?[0-9]+")


def _remove_commas(m):
    return m.group(1).replace("'", "")


def _expand_decimal_point(m):
    return m.group(1).replace(".", " puntos ")


def __expand_currency(value: str, inflection: Dict[float, str]) -> str:
    parts = value.replace(",", "").split(".")
    if len(parts) > 2:
        return f"{value} {inflection[2]}"  # Unexpected format
    text = []
    integer = int(parts[0]) if parts[0] else 0
    if integer > 0:
        integer_unit = inflection.get(integer, inflection[2])
        text.append(f"{integer} {integer_unit}")
    fraction = int(parts[1]) if len(parts) > 1 and parts[1] else 0
    if fraction > 0:
        fraction_unit = inflection.get(fraction / 100, inflection[0.02])
        text.append(f"{fraction} {fraction_unit}")
    if len(text) == 0:
        return f"zero {inflection[2]}"
    return " ".join(text)


def _expand_currency(m: "re.Match") -> str:
    currencies = {
        "$": {
            0.01: "cent",
            0.02: "cents",
            1: "dolaro",
            2: "dolar",
        },
        "€": {
            0.01: "céntimo",
            0.02: "céntimos",
            1: "euro",
            2: "euros",
        },
        "£": {
            0.01: "centavo",
            0.02: "peniques",
            1: "gbp",
            2: "libras",
        }
    }
    unit = m.group(2)
    currency = currencies[unit]
    value = m.group(1)
    return __expand_currency(value, currency)


def _expand_ordinal(m):
    return num2words(m.group(0), to="ordinal", lang="es")


def _expand_number(m):
    return num2words(m, lang="es")


def normalize_numbers(text):
    text = re.sub(_comma_number_re, _remove_commas, text)
    text = re.sub(_decimal_number_re, _expand_decimal_point, text)
    text = re.sub(_ordinal_re, _expand_ordinal, text)
    text = re.sub(_number_re, _expand_number, text)
    return text
