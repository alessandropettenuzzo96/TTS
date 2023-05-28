import re

# List of (regular expression, replacement) pairs for abbreviations in italian:
abbreviations_it = [
    (re.compile("\\b%s\\." % x[0], re.IGNORECASE), x[1])
    for x in [
        ("sig", "signore"),
        ("sig.no", "signorino"),
        ("sig.ra", "signora"),
        ("sig.na", "signorina"),
        ("co", "company"),
        ("es", "esempio"),
        ("ex", "esempio")
        ("etc", "eccetera"),
        ("dr", "dottore"),
        ("st", "santo"),
        ("c.a", "circa"),
    ]
]
