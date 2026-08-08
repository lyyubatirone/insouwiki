from insouwiki.consultation.document_view import DocumentView
from insouwiki.consultation.documentary_piece_view import (
    DocumentaryPieceView,
)
from insouwiki.consultation.personality_view import PersonalityView
from insouwiki.registry.postgres import PostgresDocumentRepository
from insouwiki.registry.postgres_sequence_repository import (
    PostgresDocumentarySequenceRepository,
)
from insouwiki.domain.documentary_personality import (
    DocumentaryPersonality,
)
from insouwiki.domain.documentary_personality_repository import (
    DocumentaryPersonalityRepository,
)
from insouwiki.services.simple_documentary_personality_repository import (
    SimpleDocumentaryPersonalityRepository,
)
from insouwiki.domain.document import Document

from insouwiki.domain.transcription import Transcription

from insouwiki.domain.documentary_sequence import (
    DocumentarySequence,
)

from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.services.simple_documentary_fact_extractor import (
    SimpleDocumentaryFactExtractor,
)

from insouwiki.consultation.documentary_fact_view import (
    DocumentaryFactView,
)

from insouwiki.services.youtube_timestamp_link_builder import (
    YouTubeTimestampLinkBuilder,
)

from insouwiki.domain.documentary_context import (
    DocumentaryContext,
)

from insouwiki.domain.documentary_type import (
    DocumentaryType,
)
from insouwiki.domain.documentary_notice import (
    DocumentaryNotice,
)
from insouwiki.services.simple_documentary_notice_builder import (
    SimpleDocumentaryNoticeBuilder,
)
from insouwiki.services.documentary_periods import (
    DOCUMENTARY_PERIODS,
)
from insouwiki.services.simple_documentary_period_finder import (
    SimpleDocumentaryPeriodFinder,
)
from insouwiki.registry.postgres_documentary_period_repository import (
    PostgresDocumentaryPeriodRepository,
)

class DocumentaryLibrary:
    """
    Bibliothèque documentaire de consultation.

    Point d'entrée des interfaces vers le patrimoine documentaire.
    """

    def __init__(
        self,
            document_repository: PostgresDocumentRepository | None = None,
        sequence_repository: (
            PostgresDocumentarySequenceRepository | None
        ) = None,
        personality_repository: (
            DocumentaryPersonalityRepository | None
        ) = None,
        transcription_repository=None,
        documentary_notice_builder: (
            SimpleDocumentaryNoticeBuilder | None
        ) = None,
    ):
            
        self.document_repository = (
            document_repository
            if document_repository is not None
            else PostgresDocumentRepository()
        )

        self.sequence_repository = (
            sequence_repository
            if sequence_repository is not None
            else PostgresDocumentarySequenceRepository()
        )

        self.personality_repository = (
            personality_repository
            if personality_repository is not None
            else SimpleDocumentaryPersonalityRepository(
                self.document_repository.find_all(),
            )
        )

        self.transcription_repository = (
            transcription_repository
        )

        self.documentary_notice_builder = (
            documentary_notice_builder
            if documentary_notice_builder is not None
            else SimpleDocumentaryNoticeBuilder(
                period_finder=SimpleDocumentaryPeriodFinder(
                    repository=PostgresDocumentaryPeriodRepository(),
                ),
            )
        )

    def get_personality(
        self,
        slug: str,
    ) -> PersonalityView:
        if slug == "jean-luc-melenchon":
            documents = self.document_repository.find_all()

            document_views = [
                DocumentView(
                    permanent_id=document.permanent_id,
                    title=document.title,
                    author=document.author,
                    original_url=str(document.original_url),
                )
                for document in documents[:10]
            ]

            first_document = (
                document_views[0]
                if document_views
                else None
            )

            return PersonalityView(
                name="Jean-Luc Mélenchon",
                description="Personnalité politique",
                document_count=self.document_repository.count(),
                documentary_piece_count=0,
                knowledge_count=0,
                relation_count=0,
                first_document=first_document,
                documents=document_views,
            )

        raise ValueError(
            f"Unknown personality: {slug}"
        )

    def list_personalities(
        self,
    ) -> list[DocumentaryPersonality]:
        return self.personality_repository.list_all()

    def get_document(
        self,
        permanent_id: str,
    ) -> DocumentView:
        documents = self.document_repository.find_all()

        for document in documents:
            if document.permanent_id == permanent_id:
                return DocumentView(
                    permanent_id=document.permanent_id,
                    title=document.title,
                    author=document.author,
                    original_url=str(document.original_url),
                    documentary_pieces=(
                        self.get_documentary_pieces(
                            document.permanent_id
                        )
                    ),
                )

        raise ValueError(
            f"Unknown document: {permanent_id}"
        )

    def list_contexts(
        self,
    ) -> list[DocumentaryContext]:
        return [
            DocumentaryContext(
                label="Tous les contextes",
            ),
            DocumentaryContext(
                label="Campagne présidentielle 2022",
            ),
            DocumentaryContext(
                label="XVIe législature (2022–2024)",
            ),
            DocumentaryContext(
                label="XVIIe législature (2024–présent)",
            ),
            DocumentaryContext(
                label="Élections européennes 2024",
            ),
        ]


    def list_document_types(
        self,
    ) -> list[DocumentaryType]:
        return [
            DocumentaryType(
                label="Tous les documents",
            ),
            DocumentaryType(
                label="Interview",
            ),
            DocumentaryType(
                label="Meeting",
            ),
            DocumentaryType(
                label="Discours",
            ),
            DocumentaryType(
                label="Question au Gouvernement",
            ),
        ]

    def get_documentary_pieces(
        self,
        document_permanent_id: str,
    ) -> list[DocumentaryPieceView]:
        """
        Retourne provisoirement une pièce documentaire
        de démonstration associée à un document.
        """
        return [
            DocumentaryPieceView(
                author="Jean-Luc Mélenchon",
                document_title=(
                    "La nouvelle géopolitique de la France"
                ),
                sequence_text=(
                    "La retraite doit être à 60 ans pour tous."
                ),
                sequence_start="00:00:00",
                sequence_end="00:00:30",
                document_url=(
                    "https://www.youtube.com/watch"
                    "?v=kLvEVQYSmhg"
                ),
            )
        ]

    def search_documentary_pieces(
        self,
        query: str,
    ) -> list[DocumentaryPieceView]:
        sequences = self.sequence_repository.search(
            query,
        )

        pieces: list[DocumentaryPieceView] = []

        for sequence in sequences:
            document = (
                self.document_repository.get_by_permanent_id(
                    sequence.document_id,
                )
            )

            if document is None:
                continue

            pieces.append(
                DocumentaryPieceView(
                    author=(
                        document.author
                        or "Auteur inconnu"
                    ),
                    document_title=document.title,
                    sequence_text=sequence.text,
                    sequence_start=str(sequence.start),
                    sequence_end=str(sequence.end),
                    document_url=str(
                        document.original_url
                    ),
                )
            )

        return pieces
    
    def documents_for_personality(
        self,
        slug: str,
    ) -> list[Document]:
        return [
            document
            for document in self.document_repository.find_all()
            if document.author
            and SimpleDocumentaryPersonalityRepository._slugify(
                document.author,
            )
            == slug
        ]
    
    def get_sequences(
        self,
        document_permanent_id: str,
    ) -> list[DocumentarySequence]:
        return self.sequence_repository.find_by_document(
            document_permanent_id,
        )


    def get_documentary_facts(
        self,
        document_permanent_id: str,
    ) -> list[DocumentaryFact]:
        document = self.document_repository.get_by_permanent_id(
            document_permanent_id,
        )

        author = (
            document.author
            if document is not None and document.author
            else "Inconnu"
        )

        sequences = self.get_sequences(
            document_permanent_id,
        )

        extractor = SimpleDocumentaryFactExtractor()

        return extractor.extract(
            author=author,
            sequences=sequences,
        )
    
    def get_documentary_fact_views(
        self,
        document_permanent_id: str,
    ) -> list[DocumentaryFactView]:
        document = self.document_repository.get_by_permanent_id(
            document_permanent_id,
        )

        sequences = self.get_sequences(
            document_permanent_id,
        )

        facts = self.get_documentary_facts(
            document_permanent_id,
        )

        sequences_by_id = {
            sequence.permanent_id: sequence
            for sequence in sequences
        }

        views: list[DocumentaryFactView] = []

        for fact in facts:
            for sequence_id in fact.supporting_sequences:
                sequence = sequences_by_id.get(
                    sequence_id,
                )

                if sequence is None:
                    continue

                source_url = ""

                if document is not None:
                    source_url = (
                        YouTubeTimestampLinkBuilder().build(
                            document,
                            sequence,
                        )
                    )

                views.append(
                    DocumentaryFactView(
                        author=fact.author,
                        statement=fact.statement,
                        source_sequence_id=sequence.permanent_id,
                        source_start=str(sequence.start),
                        source_end=str(sequence.end),
                        source_url=source_url,
                    )
                )

        return views

    def get_transcription(
        self,
        document_permanent_id: str,
    ) -> Transcription | None:
        if self.transcription_repository is None:
            return None

        return self.transcription_repository.find_by_document(
            document_permanent_id,
        )
    
    def test_returns_documentary_sequences_for_document():
        sequence = DocumentarySequence(
            permanent_id="SEQ-00000001",
            document_id="SRC-00000001",
            start=timedelta(seconds=0),
            end=timedelta(seconds=10),
            text="La retraite à 60 ans est une nécessité.",
        )

        library = DocumentaryLibrary(
            sequence_repository=(
                InMemoryDocumentarySequenceRepository(
                    [sequence],
                )
            ),
        )

        result = library.get_sequences(
            "SRC-00000001",
        )

        assert result == [sequence]

    def get_documentary_notice(
        self,
        permanent_id: str,
    ) -> DocumentaryNotice:
        documents = self.document_repository.find_all()

        for document in documents:
            if document.permanent_id == permanent_id:
                return self.documentary_notice_builder.build(
                    document,
                )

        raise ValueError(
            f"Unknown document: {permanent_id}"
        )

