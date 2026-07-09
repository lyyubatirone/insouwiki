from insouwiki.domain.documentary_analysis import DocumentaryAnalysis


POINT_D_INTERROGATION = "Point d'interrogation"
CHANGEMENT_DE_LOCUTEUR = "Changement de locuteur"
TRANSITION_EXPLICITE = "Transition explicite"
CONTINUITE_DIALOGIQUE = "Continuité dialogique"


class DocumentaryReasoningAnalyzer:
    """
    Analyse les indices documentaires permettant de déterminer
    si deux segments appartiennent au même raisonnement.
    """

    def belongs_to_same_reasoning(
        self,
        current_segment,
        next_segment,
    ) -> bool:
        analysis = self.analyze_reasoning_continuity(
            current_segment,
            next_segment,
        )

        return (
            analysis.proposed_conclusion
            == "Continuité documentaire."
        )

    def analyze_reasoning_continuity(
        self,
        current_segment,
        next_segment,
    ) -> DocumentaryAnalysis:
        if next_segment.text.startswith("Passons maintenant"):
            return DocumentaryAnalysis(
                observations=[
                    "Le texte commence par « Passons maintenant ».",
                ],
                indicators=[
                    TRANSITION_EXPLICITE,
                ],
                explanation=(
                    "La présence d'une transition explicite "
                    "indique un changement de sujet."
                ),
                proposed_conclusion=(
                    "Rupture documentaire."
                ),
            )

        observations = self._collect_observations(
            current_segment,
            next_segment,
        )

        return DocumentaryAnalysis(
            observations=observations,
            indicators=[
                CONTINUITE_DIALOGIQUE,
            ],
            explanation=(
                "La réponse répond directement à la question."
            ),
            proposed_conclusion=(
                "Continuité documentaire."
            ),
        )

    def _collect_observations(
        self,
        current_segment,
        next_segment,
    ) -> list[str]:
        observations = []

        if current_segment.text.endswith("?"):
            observations.append(POINT_D_INTERROGATION)

        if current_segment.speaker != next_segment.speaker:
            observations.append(CHANGEMENT_DE_LOCUTEUR)

        return observations