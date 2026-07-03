from insouwiki.domain.verification_request import VerificationRequest


def test_create_verification_request():
    request = VerificationRequest(
        query="Mélenchon retraites",
    )

    assert request.query == "Mélenchon retraites"