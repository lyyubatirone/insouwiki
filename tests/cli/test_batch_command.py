from types import SimpleNamespace

from typer.testing import CliRunner

from insouwiki.cli.main import app


runner = CliRunner()


def test_batch_preview_displays_processing_estimate(
    monkeypatch,
):
    fake_batch = SimpleNamespace(
        name="Retraites",
        document_count=3,
        total_duration=SimpleNamespace(
            total_seconds=lambda: 7200,
        ),
        status="prepared",
    )

    class FakeRepository:
        pass

    class FakePreparer:
        def __init__(
            self,
            repository,
        ):
            pass

        def prepare(
            self,
            name,
            document_ids,
        ):
            return fake_batch

    class FakeEstimator:
        def __init__(
            self,
            price_per_minute,
        ):
            pass

        def estimate(
            self,
            batch,
        ):
            return 0.54

    monkeypatch.setattr(
        "insouwiki.cli.main.PostgresDocumentRepository",
        FakeRepository,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main.DocumentaryProcessingBatchPreparer",
        FakePreparer,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main.DocumentaryProcessingCostEstimator",
        FakeEstimator,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main.initialize_database",
        lambda: None,
    )

    result = runner.invoke(
        app,
        [
            "batch",
            "preview",
            "Retraites",
            "SRC-00000001",
            "SRC-00000002",
            "SRC-00000003",
        ],
    )

    assert result.exit_code == 0
    assert "Retraites" in result.stdout
    assert "3" in result.stdout
    assert "2 h 00 min" in result.stdout
    assert "0.54" in result.stdout
    assert "prepared" in result.stdout
    assert (
        "Aucun traitement payant"
        in result.stdout
    )

def test_batch_create_persists_prepared_batch(
    monkeypatch,
):
    fake_batch = SimpleNamespace(
        permanent_id=None,
        name="Retraites",
        document_count=3,
        document_ids=[
            "SRC-00000001",
            "SRC-00000002",
            "SRC-00000003",
        ],
        document_durations=[],
        total_duration=SimpleNamespace(
            total_seconds=lambda: 7200,
        ),
        status="prepared",
    )

    stored_batch = SimpleNamespace(
        permanent_id="BATCH-00000001",
        name="Retraites",
        document_count=3,
        document_ids=fake_batch.document_ids,
        document_durations=[],
        total_duration=fake_batch.total_duration,
        status="prepared",
    )

    class FakeDocumentRepository:
        pass

    class FakePreparer:
        def __init__(
            self,
            repository,
        ):
            pass

        def prepare(
            self,
            name,
            document_ids,
        ):
            return fake_batch

    class FakeBatchRepository:
        def register(
            self,
            batch,
        ):
            return stored_batch

    class FakeEstimator:
        def __init__(
            self,
            price_per_minute,
        ):
            pass

        def estimate(
            self,
            batch,
        ):
            return 0.54

    monkeypatch.setattr(
        "insouwiki.cli.main.PostgresDocumentRepository",
        FakeDocumentRepository,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main.DocumentaryProcessingBatchPreparer",
        FakePreparer,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main.PostgresDocumentaryProcessingBatchRepository",
        FakeBatchRepository,
        raising=False,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main.DocumentaryProcessingCostEstimator",
        FakeEstimator,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main.initialize_database",
        lambda: None,
    )

    result = runner.invoke(
        app,
        [
            "batch",
            "create",
            "Retraites",
            "SRC-00000001",
            "SRC-00000002",
            "SRC-00000003",
        ],
    )

    assert result.exit_code == 0
    assert "Lot documentaire créé" in result.stdout
    assert "BATCH-00000001" in result.stdout
    assert "Retraites" in result.stdout
    assert "3" in result.stdout
    assert "2 h 00 min" in result.stdout
    assert "0.54" in result.stdout
    assert "prepared" in result.stdout
    assert (
        "Aucun traitement payant"
        in result.stdout
    )

def test_batch_approve_persists_approved_status(
    monkeypatch,
):
    approved_batch = SimpleNamespace(
        permanent_id="BATCH-00000001",
        name="Retraites",
        status="approved",
    )

    class FakeStoredBatch:
        permanent_id = "BATCH-00000001"
        name = "Retraites"
        status = "prepared"

        def approve(self):
            return approved_batch

    class FakeBatchRepository:
        def get_by_permanent_id(
            self,
            permanent_id,
        ):
            assert permanent_id == "BATCH-00000001"
            return FakeStoredBatch()

        def update_status(
            self,
            batch,
        ):
            assert batch is approved_batch

    monkeypatch.setattr(
        "insouwiki.cli.main."
        "PostgresDocumentaryProcessingBatchRepository",
        FakeBatchRepository,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main.initialize_database",
        lambda: None,
    )

    result = runner.invoke(
        app,
        [
            "batch",
            "approve",
            "BATCH-00000001",
        ],
    )

    assert result.exit_code == 0

    assert (
        "Lot documentaire approuvé"
        in result.stdout
    )

    assert "BATCH-00000001" in result.stdout
    assert "Retraites" in result.stdout
    assert "approved" in result.stdout

    assert (
        "Aucun traitement payant"
        in result.stdout
    )

def test_batch_process_refuses_unapproved_batch(
    monkeypatch,
):
    class FakeStoredBatch:
        permanent_id = "BATCH-00000002"
        name = "Lot non approuvé"
        status = "prepared"

    class FakeBatchRepository:
        def get_by_permanent_id(
            self,
            permanent_id,
        ):
            assert permanent_id == "BATCH-00000002"
            return FakeStoredBatch()

    monkeypatch.setattr(
        "insouwiki.cli.main."
        "PostgresDocumentaryProcessingBatchRepository",
        FakeBatchRepository,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main.initialize_database",
        lambda: None,
    )

    result = runner.invoke(
        app,
        [
            "batch",
            "process",
            "BATCH-00000002",
        ],
    )

    assert result.exit_code == 1

    assert (
        "Le lot doit être approuvé avant traitement."
        in result.stdout
    )

def test_batch_process_runs_approved_batch_and_marks_it_processed(
    monkeypatch,
):
    processed_batch = SimpleNamespace(
        permanent_id="BATCH-00000001",
        name="Retraites",
        status="processed",
    )

    class FakeStoredBatch:
        permanent_id = "BATCH-00000001"
        name = "Retraites"
        status = "approved"

        def mark_processed(self):
            return processed_batch

    class FakeBatchRepository:
        def get_by_permanent_id(
            self,
            permanent_id,
        ):
            assert permanent_id == "BATCH-00000001"
            return FakeStoredBatch()

        def update_status(
            self,
            batch,
        ):
            assert batch is processed_batch

    class FakeProcessor:
        def __init__(
            self,
            repository,
            indexer,
        ):
            pass

        def process(
            self,
            batch,
        ):
            assert batch.status == "approved"

    class FakeApplication:
        def __init__(self):
            self.document_repository = object()
            self.document_indexer = object()

    monkeypatch.setattr(
        "insouwiki.cli.main."
        "PostgresDocumentaryProcessingBatchRepository",
        FakeBatchRepository,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main."
        "DocumentaryProcessingBatchProcessor",
        FakeProcessor,
        raising=False,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main.initialize_database",
        lambda: None,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main.Application",
        FakeApplication,
    )

    result = runner.invoke(
        app,
        [
            "batch",
            "process",
            "BATCH-00000001",
        ],
        input="y\n",
    )

    assert result.exit_code == 0

    assert (
        "Lot documentaire traité"
        in result.stdout
    )

    assert "BATCH-00000001" in result.stdout
    assert "processed" in result.stdout

def test_batch_process_requires_explicit_confirmation(
    monkeypatch,
):
    class FakeStoredBatch:
        permanent_id = "BATCH-00000001"
        name = "Retraites"
        status = "approved"

    class FakeBatchRepository:
        def get_by_permanent_id(
            self,
            permanent_id,
        ):
            return FakeStoredBatch()

    class FakeProcessor:
        def __init__(self):
            self.called = False

        def process(
            self,
            batch,
        ):
            raise AssertionError(
                "Le traitement ne doit pas commencer."
            )

    monkeypatch.setattr(
        "insouwiki.cli.main."
        "PostgresDocumentaryProcessingBatchRepository",
        FakeBatchRepository,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main."
        "DocumentaryProcessingBatchProcessor",
        FakeProcessor,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main.initialize_database",
        lambda: None,
    )

    result = runner.invoke(
        app,
        [
            "batch",
            "process",
            "BATCH-00000001",
        ],
        input="n\n",
    )

    assert result.exit_code == 0

    assert (
        "Aucun traitement n'a été lancé"
        in result.stdout
    )

def test_batch_process_uses_application_dependencies(
    monkeypatch,
):
    processed_batch = SimpleNamespace(
        permanent_id="BATCH-00000001",
        name="Retraites",
        status="processed",
    )

    class FakeStoredBatch:
        permanent_id = "BATCH-00000001"
        name = "Retraites"
        status = "approved"

        def mark_processed(self):
            return processed_batch

    class FakeBatchRepository:
        def get_by_permanent_id(
            self,
            permanent_id,
        ):
            return FakeStoredBatch()

        def update_status(
            self,
            batch,
        ):
            assert batch is processed_batch

    fake_document_repository = object()
    fake_document_indexer = object()

    class FakeApplication:
        def __init__(self):
            self.document_repository = (
                fake_document_repository
            )
            self.document_indexer = (
                fake_document_indexer
            )

    class FakeProcessor:
        def __init__(
            self,
            repository,
            indexer,
        ):
            assert repository is (
                fake_document_repository
            )
            assert indexer is (
                fake_document_indexer
            )

        def process(
            self,
            batch,
        ):
            assert batch.status == "approved"

    monkeypatch.setattr(
        "insouwiki.cli.main.Application",
        FakeApplication,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main."
        "PostgresDocumentaryProcessingBatchRepository",
        FakeBatchRepository,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main."
        "DocumentaryProcessingBatchProcessor",
        FakeProcessor,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main.initialize_database",
        lambda: None,
    )

    result = runner.invoke(
        app,
        [
            "batch",
            "process",
            "BATCH-00000001",
        ],
        input="y\n",
    )

    assert result.exit_code == 0

    assert (
        "Lot documentaire traité"
        in result.stdout
    )

def test_batch_process_does_not_mark_processed_when_processing_fails(
    monkeypatch,
):
    class FakeStoredBatch:
        permanent_id = "BATCH-00000001"
        name = "Retraites"
        status = "approved"

        def mark_processed(self):
            raise AssertionError(
                "Le lot ne doit pas être marqué processed."
            )

    class FakeBatchRepository:
        status_updated = False

        def get_by_permanent_id(
            self,
            permanent_id,
        ):
            assert permanent_id == "BATCH-00000001"
            return FakeStoredBatch()

        def update_status(
            self,
            batch,
        ):
            self.status_updated = True
            raise AssertionError(
                "Le statut ne doit pas être mis à jour."
            )

    class FakeApplication:
        def __init__(self):
            self.document_repository = object()
            self.document_indexer = object()

    class FailingProcessor:
        def __init__(
            self,
            repository,
            indexer,
        ):
            pass

        def process(
            self,
            batch,
        ):
            raise RuntimeError(
                "Échec du traitement documentaire"
            )

    monkeypatch.setattr(
        "insouwiki.cli.main.Application",
        FakeApplication,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main."
        "PostgresDocumentaryProcessingBatchRepository",
        FakeBatchRepository,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main."
        "DocumentaryProcessingBatchProcessor",
        FailingProcessor,
    )

    monkeypatch.setattr(
        "insouwiki.cli.main.initialize_database",
        lambda: None,
    )

    result = runner.invoke(
        app,
        [
            "batch",
            "process",
            "BATCH-00000001",
        ],
        input="y\n",
    )

    assert result.exit_code == 1

    assert (
        "Erreur pendant le traitement documentaire"
        in result.stdout
    )

    assert (
        "Échec du traitement documentaire"
        in result.stdout
    )