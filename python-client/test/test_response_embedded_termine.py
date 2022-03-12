"""
    Arbeitsagentur Weiterbildungssuche API

    Eine der größten Weiterbildungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:  **ClientID:** 38053956-6618-4953-b670-b4ae7a2360b1  **ClientSecret:** c385073c-3b97-42a9-b916-08fd8a5d1795.   **Achtung**: der generierte Token muss bei folgenden GET-requests im header als 'OAuthAccessToken' inkludiert werden.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.weiterbildungssuche.model.response_embedded_adresse import (
    ResponseEmbeddedAdresse,
)
from deutschland.weiterbildungssuche.model.response_embedded_angebot import (
    ResponseEmbeddedAngebot,
)
from deutschland.weiterbildungssuche.model.response_embedded_ansprechpartner import (
    ResponseEmbeddedAnsprechpartner,
)
from deutschland.weiterbildungssuche.model.response_embedded_dauer import (
    ResponseEmbeddedDauer,
)
from deutschland.weiterbildungssuche.model.response_embedded_unterrichtsform import (
    ResponseEmbeddedUnterrichtsform,
)
from deutschland.weiterbildungssuche.model.response_embedded_unterrichtszeit import (
    ResponseEmbeddedUnterrichtszeit,
)

from deutschland import weiterbildungssuche

globals()["ResponseEmbeddedAdresse"] = ResponseEmbeddedAdresse
globals()["ResponseEmbeddedAngebot"] = ResponseEmbeddedAngebot
globals()["ResponseEmbeddedAnsprechpartner"] = ResponseEmbeddedAnsprechpartner
globals()["ResponseEmbeddedDauer"] = ResponseEmbeddedDauer
globals()["ResponseEmbeddedUnterrichtsform"] = ResponseEmbeddedUnterrichtsform
globals()["ResponseEmbeddedUnterrichtszeit"] = ResponseEmbeddedUnterrichtszeit
from deutschland.weiterbildungssuche.model.response_embedded_termine import (
    ResponseEmbeddedTermine,
)


class TestResponseEmbeddedTermine(unittest.TestCase):
    """ResponseEmbeddedTermine unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseEmbeddedTermine(self):
        """Test ResponseEmbeddedTermine"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResponseEmbeddedTermine()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
