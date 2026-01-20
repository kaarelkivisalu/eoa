from __future__ import annotations

from enum import Enum

# NOTE: This map is intentionally hardcoded (as requested). If a new subject is added
# to the DB, update this mapping.
SUBJECT_ABBREV: dict[str, str] = {
    "Füüsika": "efo",
    "Keemia": "eko",
    "Informaatika": "eio",
    "Bioloogia": "ebo",
    "Loodusteadused": "elo",
    "Matemaatika": "emo",
    "Astronoomia": "ast",
    "Filosoofia": "fil",
    "Maateadused": "mte",
    "Lingvistika": "lin",
    "Usundiõpetus": "usu",
    "Emakeel": "ema",
    "Inglise keel": "ing",
    "Saksa keel": "sak",
    "Vene keel emakeelena": "vem",
    "Vene keel võõrkeelena": "vvk",
    "Prantsuse keel": "pra",
    "Geograafia": "geo",
    "Inimeseõpetus": "ini",
}


class SubjectAbbrev(str, Enum):
    efo = "efo"
    eko = "eko"
    eio = "eio"
    ebo = "ebo"
    elo = "elo"
    emo = "emo"
    ast = "ast"
    fil = "fil"
    mte = "mte"
    lin = "lin"
    usu = "usu"
    ema = "ema"
    ing = "ing"
    sak = "sak"
    vem = "vem"
    vvk = "vvk"
    pra = "pra"
    geo = "geo"
    ini = "ini"
