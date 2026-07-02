from insouwiki.domain.documentary_evolution import DocumentaryEvolution
from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.services.simple_evolution_finder import (
    SimpleEvolutionFinder,
)


def test_returns_no_evolution_without_fact():
    finder = SimpleEvolutionFinder()

    assert finder.find([]) == []


def test_returns_no_evolution_with_single_fact():
    fact = DocumentaryFact(
        permanent_id="FACT-00000001",
        author="Jean-Luc Mélenchon",
        statement="Une affirmation documentaire.",
        supporting_sequences=["SEQ-00000001"],
    )

    finder = SimpleEvolutionFinder()

    assert finder.find([fact]) == []


def test_same_statement_is_not_an_evolution():
    facts = [
        DocumentaryFact(
            permanent_id="FACT-00000001",
            author="Jean-Luc Mélenchon",
            statement="La retraite doit être à 60 ans.",
            supporting_sequences=["SEQ-00000001"],
        ),
        DocumentaryFact(
            permanent_id="FACT-00000002",
            author="Jean-Luc Mélenchon",
            statement="La retraite doit être à 60 ans.",
            supporting_sequences=["SEQ-00000002"],
        ),
        DocumentaryFact(
            permanent_id="FACT-00000003",
            author="Jean-Luc Mélenchon",
            statement="La retraite doit être à 60 ans.",
            supporting_sequences=["SEQ-00000003"],
        ),
    ]

    finder = SimpleEvolutionFinder()

    assert finder.find(facts) == []


def test_precision_is_not_yet_an_evolution():
    facts = [
        DocumentaryFact(
            permanent_id="FACT-00000001",
            author="Jean-Luc Mélenchon",
            statement="La retraite doit être à 60 ans.",
            supporting_sequences=["SEQ-00000001"],
        ),
        DocumentaryFact(
            permanent_id="FACT-00000002",
            author="Jean-Luc Mélenchon",
            statement="La retraite doit être à 60 ans pour les carrières longues.",
            supporting_sequences=["SEQ-00000002"],
        ),
    ]

    finder = SimpleEvolutionFinder()

    assert finder.find(facts) == []


def test_detects_a_documentary_evolution():
    facts = [
        DocumentaryFact(
            permanent_id="FACT-00000001",
            author="Jean-Luc Mélenchon",
            statement="La retraite doit être à 65 ans.",
            supporting_sequences=["SEQ-00000001"],
        ),
        DocumentaryFact(
            permanent_id="FACT-00000002",
            author="Jean-Luc Mélenchon",
            statement="La retraite doit être à 60 ans.",
            supporting_sequences=["SEQ-00000002"],
        ),
    ]

    finder = SimpleEvolutionFinder()

    evolutions = finder.find(facts)

    assert len(evolutions) == 1

    assert isinstance(
        evolutions[0],
        DocumentaryEvolution,
    )