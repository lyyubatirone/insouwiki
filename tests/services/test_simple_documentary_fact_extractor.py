from datetime import timedelta

from insouwiki.domain.documentary_sequence import DocumentarySequence
from insouwiki.services.simple_documentary_fact_extractor import (
    SimpleDocumentaryFactExtractor,
)


def test_simple_documentary_fact_extractor_creates_one_fact():
    sequence = DocumentarySequence(
        permanent_id="SEQ-00000001",
        document_id="DOC-00000001",
        start=timedelta(seconds=0),
        end=timedelta(seconds=12),
        text="Je pense que nous avons vécu un beau moment de notre histoire.",
    )

    extractor = SimpleDocumentaryFactExtractor()

    facts = extractor.extract([sequence])

    assert len(facts) == 1

    fact = facts[0]

    assert fact.permanent_id == "FACT-00000001"
    assert fact.author == "Inconnu"
    assert (
        fact.statement
        == "Je pense que nous avons vécu un beau moment de notre histoire."
    )
    assert fact.supporting_sequences == ["SEQ-00000001"]