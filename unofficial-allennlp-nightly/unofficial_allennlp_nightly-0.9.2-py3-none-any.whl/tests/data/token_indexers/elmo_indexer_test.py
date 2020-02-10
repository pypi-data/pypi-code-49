from allennlp.common.testing import AllenNlpTestCase
from allennlp.data import Token, Vocabulary
from allennlp.data.token_indexers import ELMoTokenCharactersIndexer


class TestELMoTokenCharactersIndexer(AllenNlpTestCase):
    def test_bos_to_char_ids(self):
        indexer = ELMoTokenCharactersIndexer()
        indices = indexer.tokens_to_indices([Token("<S>")], Vocabulary())
        expected_indices = [
            259,
            257,
            260,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
        ]
        assert indices == {"tokens": [expected_indices]}

    def test_eos_to_char_ids(self):
        indexer = ELMoTokenCharactersIndexer()
        indices = indexer.tokens_to_indices([Token("</S>")], Vocabulary())
        expected_indices = [
            259,
            258,
            260,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
        ]
        assert indices == {"tokens": [expected_indices]}

    def test_unicode_to_char_ids(self):
        indexer = ELMoTokenCharactersIndexer()
        indices = indexer.tokens_to_indices([Token(chr(256) + "t")], Vocabulary())
        expected_indices = [
            259,
            197,
            129,
            117,
            260,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
            261,
        ]
        assert indices == {"tokens": [expected_indices]}

    def test_elmo_as_array_produces_token_sequence(self):
        indexer = ELMoTokenCharactersIndexer()
        tokens = [Token("Second"), Token(".")]
        indices = indexer.tokens_to_indices(tokens, Vocabulary())
        padded_tokens = indexer.as_padded_tensor_dict(indices, padding_lengths={"tokens": 3})
        expected_padded_tokens = [
            [
                259,
                84,
                102,
                100,
                112,
                111,
                101,
                260,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
            ],
            [
                259,
                47,
                260,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        ]

        assert padded_tokens["tokens"].tolist() == expected_padded_tokens

    def test_elmo_indexer_with_additional_tokens(self):
        indexer = ELMoTokenCharactersIndexer(tokens_to_add={"<first>": 1})
        tokens = [Token("<first>")]
        indices = indexer.tokens_to_indices(tokens, Vocabulary())
        expected_indices = [
            [
                259,
                2,
                260,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
                261,
            ]
        ]
        assert indices["tokens"] == expected_indices
