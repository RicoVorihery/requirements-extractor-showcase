"""
Utility helpers used by the block builder.
Simplified for clarity.
"""

def normalize(text: str) -> str:
    return text.replace("\xa0", " ").replace(" :", ":").strip()


def starts_with_prefix(text: str, prefix: str) -> bool:
    return normalize(text).startswith(normalize(prefix))


def looks_like_id(line: str) -> bool:
    """
    MVP heuristic only.
    Regex viendra plus tard via regex-generator.
    """
    line = normalize(line)
    if " " in line:
        return False
    if len(line) < 4:
        return False
    if not any(c.isdigit() for c in line):
        return False
    return True


def looks_like_text(line: str) -> bool:
    """
    Simple heuristique pour éviter des faux blocs
    quand le texte n'a pas de préfixe.
    """
    line = normalize(line)
    return len(line) >= 10


def looks_like_coverage(line: str) -> bool:
    """
    MVP: on accepte toute ligne non vide.
    La validation fine viendra plus tard.
    """
    return bool(normalize(line))