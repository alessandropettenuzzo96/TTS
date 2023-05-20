import re

# List of (regular expression, replacement) pairs for abbreviations in spanish:
abbreviations_es = [
    (re.compile("\\b%s\\." % x[0], re.IGNORECASE), x[1])
    for x in [
        ("sr", "señor"),
        ("sra", "señora"),
        ("srita", "señorita"),
        ("ud", "usted"),
        ("ej", "ejemplo"),
        ("etc", "etcetera"),
        ("dr", "doctor"),
        ("st", "santo"),
    ]
]
