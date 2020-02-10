from .PseudonymDataGenerator import PseudonymDataGenerator
from .PseudonymData import PseudonymData

class UsernameDomainPseudonymDataGenerator(PseudonymDataGenerator):
    def __init__(self, domain_pseudonymizer, username_pseudonymizer_factory):
        self.__domain_pseudonymizer = domain_pseudonymizer
        self.__username_pseudonymizer_factory = \
            username_pseudonymizer_factory
        self.__username_pseudonymizers = {}

    def get_pseudonym_data(self, data):
        (domain, username) = data
        domain_pseudonym = self.__domain_pseudonymizer.get_pseudonym(domain)
        if domain_pseudonym is None:
            return None
        username_pseudonymizer = \
            self.__username_pseudonymizers.get(domain_pseudonym.deep_data)
        if username_pseudonymizer is None:
            username_pseudonymizer = self.__username_pseudonymizer_factory()
            self.__username_pseudonymizers[domain_pseudonym.deep_data] = \
                username_pseudonymizer
        username_pseudonym = username_pseudonymizer.get_pseudonym(username)
        if username_pseudonym is None:
            return None
        return PseudonymData(
            flat=(
                domain_pseudonym.formatted,
                username_pseudonym.formatted
            ),
            deep=(
                domain_pseudonym.deep_data,
                username_pseudonym.deep_data
            )
        )
