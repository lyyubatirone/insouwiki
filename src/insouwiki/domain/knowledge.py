from pydantic import BaseModel, model_validator


class Knowledge(BaseModel):
    """
    Connaissance documentaire.

    Une connaissance représente une organisation explicable
    de faits documentaires reliés entre eux.

    Elle ne remplace jamais les faits qui la composent.
    """

    permanent_id: str

    title: str

    summary: str

    supporting_fact_ids: list[str]

    @model_validator(mode="after")
    def validate_supporting_facts(self):
        if len(self.supporting_fact_ids) == 0:
            raise ValueError(
                "Une connaissance documentaire doit référencer au moins un fait documentaire."
            )
        return self