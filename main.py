"""The Tired Dark Lord: a 100-word villain monologue.

Writes MONOLOGUE to /output/entry.txt (or argv[1] when it is a path,
not a flag). Stdlib only; no network, no file reads, no env access,
no clock or randomness: same bytes always.
"""

import os
import sys

MONOLOGUE = "Right. The eclipse. I wrote it down. Three hundred years on the obsidian throne, and still the goblins file my conquests under 'miscellaneous.' My generals want a war cry. My war cry wants a nap. The blood moon rises at midnight, the priests chant... hmm. Where was I? Oh. The ritual. The dagger, the chalice, the choir of chained wraiths. All very Tuesday. Kneel, hero. Or don't. The paperwork alone will bury you. Varkhul conquered nine kingdoms, outlived three prophecies, and nobody refills the ink. So. Shall we do the monologue, or shall I sign the surrender forms and go to bed?"

DEFAULT_OUTPUT = "/output/entry.txt"


def word_count(text):
    """Word count of text."""
    return len(text.split())


def is_valid(text):
    """Gate: 1-600 chars, not blank, UTF-8."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 600:
        return False
    if text.strip() == "":
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def write_entry(path, text=None):
    """Write text (default MONOLOGUE) to path, no trailing newline.

    Raises ValueError and writes nothing when the text fails is_valid().
    """
    if text is None:
        text = MONOLOGUE
    if not is_valid(text):
        raise ValueError("invalid entry text")
    parent = os.path.dirname(os.path.abspath(path))
    os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return path


def main(argv):
    output = DEFAULT_OUTPUT
    if len(argv) > 1 and not argv[1].startswith("-"):
        output = argv[1]
    write_entry(output)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
