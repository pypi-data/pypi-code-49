#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import re
from enum import Enum, unique

# todo: need refactor, some of the relation name are only for the code, eg. mention in
from sekg.text.extractor.domain_entity.nlp_util import SpacyNLPFactory


@unique
class RelationType(Enum):
    IS_A = "is a"
    REPRESENT = "represent"
    SUBCLASS_OF = "subclass of"
    PART_OF = "part of"
    MENTION_IN_COMENT = "mention in comment"
    MENTION_IN_INSIDE_COMENT = "mention in inside comment"
    MENTION_IN_STRING_LITERAL = "mention in string literal"
    MENTION_IN_SHORT_DESCRIPTION = "mention in short description"
    MENTION = "mention"

    HAS_OPERATION = "has operation"
    INSTANCE_OF = "instance of"
    OPERATE = "operate"
    CAN_BE_OPERATED = "can be operated"

    NAME_MENTION = "name mention"


class RelationDetector:
    def __init__(self):
        self.cache = {}
        self.nlp = SpacyNLPFactory.create_spacy_nlp_for_domain_extractor()
        self.pos_cache = {}
        self.terms = set()

    def expand(self, terms):
        terms = set(terms)
        self.terms = terms
        expanded = set()
        addition = set()
        for term in terms:
            # 拆分A and B 或者 A or B -> A, B
            tmp = re.sub(r'( and | or )', r' $ ', term)
            parts = tmp.split(" $ ")
            if len(parts) > 1:
                i = 0
                size = len(parts)
                while i < size - 1:
                    p = parts[i].split()
                    n = parts[i + 1].split()
                    if len(p) < len(n):
                        tmp = " ".join(p + n[len(p):])
                        addition.add(tmp)
                        if tmp not in self.cache:
                            self.cache[tmp] = set()
                        self.cache[tmp].add(term)
                        addition.add(parts[i + 1])
                        if parts[i + 1] not in self.cache:
                            self.cache[parts[i + 1]] = set()
                        self.cache[parts[i + 1]].add(term)
                        i += 2
                    else:
                        addition.add(parts[i])
                        if parts[i] not in self.cache:
                            self.cache[parts[i]] = set()
                        self.cache[parts[i]].add(term)
                        i += 1
                        if i == size - 1:
                            addition.add(parts[i])
                            if parts[i] not in self.cache:
                                self.cache[parts[i]] = set()
                            self.cache[parts[i]].add(term)
                expanded.add(term)
            tmp = re.sub(r'( of |\'s )', r' $ ', term)
            parts = tmp.split(" $ ")
            if len(parts) == 2:
                addition.add(parts[0])
                if parts[0] not in self.cache:
                    self.cache[parts[0]] = set()
                self.cache[parts[0]].add(term)
                addition.add(parts[1])
                if parts[1] not in self.cache:
                    self.cache[parts[1]] = set()
                self.cache[parts[1]].add(term)
                expanded.add(term)

        self.terms.update(addition)
        return expanded

    def detect_relation_by_starfix(self, terms):
        """[summary]
        detect relation by *fix (prefix, infix, suffix)
        Arguments:
            terms {[type]} -- [description]
        Returns:
            [type] -- [description]
        """
        # 有被扩展词组集合
        expanded = self.expand(terms)
        relations = set()
        new_candidate = set()
        # record记录可能存在的扩展对
        record = dict()
        # for c in candidate:
        for c in self.terms:
            new_candidate.add(c.lower())
        for i, term in enumerate(new_candidate):
            if i % 100 == 0:
                print(i)
            for t2 in new_candidate:
                if t2.find(term) >= 0:
                    if term not in record:
                        record[term] = {t2}
                    else:
                        record[term].add(t2)
        for i, term in enumerate(new_candidate):
            # if i % 10000 == 0:
            #     print(i)
            term1 = term
            for term2 in record[term]:
                short_term, long_term = (term1.lower(), term2.lower()) if len(term1) <= len(term2) else (
                    term2.lower(), term1.lower())
                if long_term.find(short_term) < 0:
                    continue
                if long_term.endswith(" " + short_term):
                    if long_term in self.pos_cache:
                        long_term_pos = self.pos_cache[long_term]
                    else:
                        long_term_pos = tuple([token.pos_ for token in self.nlp(long_term)])
                        self.pos_cache[long_term] = long_term_pos
                    if long_term_pos[-1] in {"NOUN", "PROPN"}:
                        short, long = (term1, term2) if len(term1) <= len(term2) else (
                            term2, term1)
                        if " of " in long:
                            relations.add((short, RelationType.PART_OF.value, long))
                        else:
                            relations.add((long, RelationType.IS_A.value, short))
                elif " {} ".format(short_term) in long_term or long_term.startswith(short_term + " "):
                    if long_term in self.pos_cache:
                        long_term_pos = self.pos_cache[long_term]
                    else:
                        long_term_pos = tuple([token.pos_ for token in self.nlp(long_term)])
                        self.pos_cache[long_term] = long_term_pos
                    if long_term_pos[long_term.split().index(short_term.split()[-1])] in {"NOUN", "PROPN"}:
                        short, long = (term1, term2) if len(term1) <= len(term2) else (
                            term2, term1)
                        if " of " in long:
                            relations.add((long, RelationType.IS_A.value, short))
                        else:
                            relations.add((short, RelationType.PART_OF.value, long))

        # for k, v in self.cache.items():
        #     for term in v:
        #         relations.add((term, RelationType.PART_OF.value, k))

        relations = set(filter(lambda x: x[0] != x[2], relations))
        relations = self.filter_rules(relations)
        relations = set(filter(lambda x: x[0] != x[2], relations))
        return relations

    def filter_rules(self, relations):
        rel = list(relations)
        for relation in relations:
            r1 = relation[0]
            r2 = relation[2]
            rela = relation[1]
            taga = relation[2] + ' and'
            tagb = 'and ' + relation[2]
            if tagb in relation[0] or taga in relation[0]:
                # print(rel)
                # print(relation)
                if relation in rel:
                    rel.append((relation[0], 'consist of', relation[2]))
                    rel.append(
                        (relation[0].replace(relation[2], '').replace('and', '').strip(), 'part of', relation[0]))
                    rel.append(
                        (relation[0], 'consist of', relation[0].replace(relation[2], '').replace('and', '').strip()))
                    rel.append((relation[2], 'part of', relation[0]))
                    rel.remove(relation)
            if 'kind' == relation[2]:
                if relation in rel:
                    rel.remove(relation)
            if 'pair of ' in relation[0]:
                if relation in rel:
                    rel.remove(relation)
            # when ABC -> BC, BC -> C and ABC -> C remove ABC -> C
            for sub_relation in relations:
                if sub_relation[0] == r2 and sub_relation[1] == rela:
                    abcd = (r1, rela, sub_relation[2])
                    if abcd in rel:
                        rel.remove(abcd)
        return set(rel)


if __name__ == "__main__":
    print(RelationType.IS_A.value)
    Re = RelationDetector()
    terms = {'sequence',"a sequence", "the sequence", "string and char", 'string', 'string builder', "builder", "character's sequence", "sequence of character", "sequence"}
    # terms = {"A's B"}
    t = Re.detect_relation_by_starfix(terms)
    print(t)