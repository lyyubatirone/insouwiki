from insouwiki.domain.documentary_relation import DocumentaryRelation
from insouwiki.domain.documentary_relation_type import DocumentaryRelationType


def test_documentary_relation_creation():
    relation = DocumentaryRelation(
        permanent_id="REL-00000001",
        relation_type=DocumentaryRelationType.SAME_TOPIC,
        source_fact_id="FACT-00000001",
        target_fact_id="FACT-00000002",
    )

    assert relation.permanent_id == "REL-00000001"
    assert relation.relation_type == DocumentaryRelationType.SAME_TOPIC
    assert relation.source_fact_id == "FACT-00000001"
    assert relation.target_fact_id == "FACT-00000002"