#!/usr/bin/env python
"""Testing seq_tools.py"""
########################################################################
# File: seq_tools_test.py
#  executable: seq_tools_test.py
#
# Author: Andrew Bailey
# History: 02/15/18 Created
########################################################################

import unittest
from py3helpers.seq_tools import *
from py3helpers.utils import captured_output
import pysam


class SeqToolsTests(unittest.TestCase):
    """Test the functions in seq_tools.py"""

    @classmethod
    def setUpClass(cls):
        super(SeqToolsTests, cls).setUpClass()
        cls.HOME = '/'.join(os.path.abspath(__file__).split("/")[:-1])
        cls.fasta = os.path.join(cls.HOME,
                                 "test_files/test.fa")
        cls.fastq = os.path.join(cls.HOME,
                                 "test_files/test.fastq")
        cls.reference = os.path.join(cls.HOME,
                                     "test_files/ecoli_k12_mg1655.fa")

    def test_read_fasta(self):
        with captured_output() as (_, _):
            for header, sequence in read_fasta(self.fasta, upper=True):
                self.assertEqual(header, "test perfect alignment")
                self.assertEqual(sequence,
                                 "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGCTTCTGAACTGA")

            for header, sequence in read_fasta(self.fasta, upper=False):
                self.assertEqual(header, "test perfect alignment")
                self.assertEqual(sequence,
                                 "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGCTTCTGAACTGa")

    def test_get_minimap_cigar(self):
        with captured_output() as (_, _):
            cigar = get_minimap_cigar(self.reference,
                                      "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGCTTCTGAACTG")
            self.assertEqual(cigar, '80M')
            cigar = get_minimap_cigar(self.reference,
                                      'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGCTTCTGAACTG',
                                      cigar_string=False)
            self.assertEqual(cigar, [[80, 0]])
            with self.assertRaises(AssertionError):
                get_minimap_cigar(self.reference,
                                  "AGCTTTTCATTCTAGTGTCTGATAGCAGCTTCTGAACTG",
                                  cigar_string=False)

    def test_create_pairwise_alignment(self):
        with captured_output() as (_, _):
            alignment = create_pairwise_alignment("AATA", "AATA", local=True)
            self.assertEqual(alignment["reference"], "AATA")
            self.assertEqual(alignment["query"], "AATA")
            alignment = create_pairwise_alignment("AAAA", "AATA")
            self.assertEqual(alignment["reference"], "AAAA")
            self.assertEqual(alignment["query"], "AATA")
            alignment = create_pairwise_alignment("ATTTTA", "AATA")
            self.assertEqual(alignment["reference"], "ATTTTA")
            self.assertEqual(alignment["query"], "A--ATA")
            alignment = create_pairwise_alignment("ATTTTA", "TTTT", local=True)
            self.assertEqual(alignment["reference"], "ATTTTA")
            self.assertEqual(alignment["query"], "-TTTT-")

    def test_cigar_conversion(self):
        with captured_output() as (_, _):
            self.assertEqual(cigar_conversion("M"), 0)
            self.assertEqual(cigar_conversion("I"), 1)
            self.assertEqual(cigar_conversion("D"), 2)
            self.assertEqual(cigar_conversion("N"), 3)
            self.assertEqual(cigar_conversion("S"), 4)
            self.assertEqual(cigar_conversion("H"), 5)
            self.assertEqual(cigar_conversion("P"), 6)
            self.assertEqual(cigar_conversion("="), 7)
            self.assertEqual(cigar_conversion("X"), 8)

            self.assertEqual(cigar_conversion(0), "M")
            self.assertEqual(cigar_conversion(1), "I")
            self.assertEqual(cigar_conversion(2), "D")
            self.assertEqual(cigar_conversion(3), "N")
            self.assertEqual(cigar_conversion(4), "S")
            self.assertEqual(cigar_conversion(5), "H")
            self.assertEqual(cigar_conversion(6), "P")
            self.assertEqual(cigar_conversion(7), "=")
            self.assertEqual(cigar_conversion(8), "X")

            with self.assertRaises(AssertionError):
                cigar_conversion("A")
                cigar_conversion("ADSDFS")
                cigar_conversion("MID")
                cigar_conversion(9)
                cigar_conversion(-1)

    def test_get_pairwise_cigar(self):
        with captured_output() as (_, _):
            cigar = get_pairwise_cigar(ref="AATA", query="AATA")
            self.assertEqual(cigar, "4M")
            cigar = get_pairwise_cigar(query="ATTTTA", ref="TTTT", local=True)
            self.assertEqual(cigar, "1S4M1S")
            cigar = get_pairwise_cigar(query="ATTTTA", ref="TTFTT", local=True)
            self.assertEqual(cigar, "1S2M1D2M1S")

    def test_write_fasta(self):
        with captured_output() as (_, _):
            with tempfile.TemporaryDirectory() as tempdir:
                path = os.path.join(tempdir, "test.fasta")
                write_fasta({"header": "sequence"}, path)
                for header, sequence in read_fasta(path):
                    self.assertEqual(header, "header")
                    self.assertEqual(sequence, "SEQUENCE")
                os.remove(path)

            with self.assertRaises(AssertionError):
                write_fasta({"header": "sequence"}, "asdf.asdf")
                write_fasta(["header", "sequence"], path)

    def test_create_fastq_line(self):
        with captured_output() as (_, _):
            read_id = "asdf"
            sequence = "asdf"
            q_values = "asdf"
            fastq = create_fastq_line(read_id, sequence, q_values)
            self.assertEqual("@asdf\nasdf\n+\nasdf", fastq)
            bad_read_id = "as\ndf"
            bad_sequence = "as\ndf"
            bad_q_values = "asd"
            with self.assertRaises(AssertionError):
                create_fastq_line(bad_read_id, sequence, q_values)
                create_fastq_line(read_id, bad_sequence, q_values)
                create_fastq_line(read_id, sequence, bad_q_values)

    def test_check_fastq_line(self):
        with captured_output() as (_, _):
            fastq_record = "@asdf\nasdf\n+\nasdf"
            self.assertTrue(check_fastq_line(fastq_record))
            with self.assertRaises(AssertionError):
                check_fastq_line("asdf\nasdf\n+\nasdf")
                check_fastq_line("@asdfasdf\n+\nasdf")
                check_fastq_line("@asdf\nasdf+\nasdf")
                check_fastq_line("@asdf\nasdf\n+\nasdf\n")
                check_fastq_line("@asdf\nasdf\n+asdf")
                check_fastq_line("@asdf\nasdsf\n+\nasdf")
                check_fastq_line("@asdf\nasdf\n+\nassdf")

    def test_pairwise_alignment_accuracy(self):
        with captured_output() as (_, _):
            self.assertEqual(pairwise_alignment_accuracy("AATA", "AATA"), 1)
            self.assertEqual(pairwise_alignment_accuracy("AAAA", "AATA"), .75)
            self.assertEqual(pairwise_alignment_accuracy("AAATTTAAAA", "AAAAAAA"), .70)
            self.assertEqual(pairwise_alignment_accuracy("CCCCCAAATTTAAAA", "AAAAAAA", soft_clip=True), 7 / 15)
            self.assertEqual(pairwise_alignment_accuracy(query="CCCCCAAATTTAAAA", ref="AAAAAAA", soft_clip=False), .70)

    def test_initialize_pysam_wrapper(self):
        with captured_output() as (_, _):
            header = "@SQ	SN:Chromosome	LN:4641652 \n@PG	ID:bwa	PN:bwa	VN:0.7.15-r1142-dirty	CL:bwa mem -x ont2d /Users/andrewbailey/CLionProjects/nanopore-RNN/signalAlign/bin/test_output/tempFiles_alignment/temp_bwaIndex /Users/andrewbailey/CLionProjects/nanopore-RNN/signalAlign/bin/test_output/tempFiles_alignment/tempFiles_miten_PC_20160820_FNFAD20259_MN17223_mux_scan_AMS_158_R9_WGA_Ecoli_08_20_16_83098_ch138_read23_strand/temp_seq_5048dffc-a463-4d84-bd3b-90ca183f488a.fa\n"
            test_sam = "5048dffc-a463-4d84-bd3b-90ca183f488a\t16\tChromosome\t623201\t57\t14S16M2I2M2I20M1I35M1D9M1D1M1D4M2I1M1I26M1D8M1I8M1D3M1D12M1D5M4D1M2D3M1D14M3D3M1I2M1I8M2D5M3D6M2D25M1I2M1I26M2I31M5D2M1D23M1D4M1D16M1D6M1I3M1I2M1I13M11S\t*\t0\t0\tAAACATAAACAGAACCACGGGTCCGTCTGGGCCCGACGACGCCGAGGTGGATTTTAGGGCGTGGCTTATCTGGCGCTGTTCGGCTGGTTGAGGCGGTCAGCCTTGCCGTCGTAACACATCACGCTGCAATCGCAAACCCGGAAGTTGATGTTAGGCGATTAACGGCTTCAGACCTACAGACGGGCGACGCCGGCTACAGGCGCCGCGGTCGAAGCGCCGATGACACCGGCTGTTTCCGCAAGCCGCCGAGCTTGCCTGGCCTGTTGATTATCTATGCAAGTTGTCATTGCTGGTGCCGGTGGAGTCATGACGCCAGACGCCGCCGCAGGTACAGAACCGACAGTTAATGCTAAAACAAGCAACACGTAAACCGAACCGGGAAGTACGG\t*\tNM:i:102\tMD:Z:3T0T4T2T5T2T5T17T2G24^T9^T1^G6C2T3C0A1T7A6^C8C7^G3^G9T2^G0T0G3^GGCG1^AG0A2^G0T9T3^ATA3G6T2^TG3G1^TTT0G0G4^GA0T11T2C16G0G0T0T0T3T0T11G2G0T5T11T8^TGCGA2^T1T0T20^G4^C0G0T14^T9G2T3G2T1T2\tAS:i:159\tXS:i:0\n"
            pysam_h = initialize_pysam_wrapper(header + test_sam)
            self.assertIsInstance(pysam_h, pysam.AlignmentFile)
            self.assertIsInstance(pysam_h, PysamWrapper)
            with self.assertRaises(ValueError):
                initialize_pysam_wrapper(header)
                initialize_pysam_wrapper(test_sam)
                initialize_pysam_wrapper("randomstring")
            with self.assertRaises(OSError):
                test_sam = "@SQ	SN:ref	LN:45\n@SQ	SN:ref2	LN:40\nr001	163	ref	7	30	6M1	=	37	39	GATTACA	*	XX:B:S,12561,2,20,112"
                pysam_h = initialize_pysam_wrapper(test_sam)

    def test_sam_string_to_aligned_segment(self):
        with captured_output() as (_, _):
            test_sam = "8898d755-e46d-4cbe-842c-545a97718b9d_Basecall_1D_template	0	rna_fake_reversed	674	11	20S12M2I21M1I4M3I10M2I4M5I37M3I4M1I3M2I5M2D5M6D5M2D15M5D3M3D4M2D5M2D9M2D6M2D2M2D1M2D5M2D1M2D1M2D12M2D1M2D15M2D7M2D1M2D3M2D3M2D4M2D5M2D1M2D8M2D3M2D1M2D3M2D3M2D1M2D2M2D1M2D5M2D4M2D2M2D1M2D3M2D4M2D3M2D3M2D4M2D3M2D4M2D3M2D14M2D3M2D3M2D7M2D4M2D3M2D3M2D4M2D7M2D3M2D4M2D1M2D4M2D3M2D3M2D13M1D8M57S	*	0	0	AACCTAACGACACCACTATCCCTACACCCTATCCAACTACTATTACTCTATTCTACTTATCACCCTACTACTACCTCATCCTCCTCCCTAAAATTTCGAGTAAGTAAAATCAATTTCGTGTCAAAATTCATTAAGGGCATCCTAATAGAGGTTGGTCGGCGATTTTAATAAGTGTATGTTTCGGACGTTCATAAGTTTAAAGTGTTTGTGTTAACGTTTTCGTCTTTGATTTTGGAAGTATCAGTCACTCTAATTTTGTTACGAAGTAGTAAGAATTTCATGGACAATTATTTACGACGATTTATGATTCACGATTTTTTTTTTTCGATCACGACCGTCGACCGACGACCACCGACCGTCGACCACCGAACCTACCATTATTTTTCCTTTTGAAAATATTACTGTTCGTGAGAATATAAGTAAAAAATAGAGTATTGACCTATTGTGTCCCGTCCTAC	*	NM:i:179	MD:Z:3C1T6T1T2T4T0T2G3G6T0G2T2T3T3T1A1T1T0T5T2C1T2T0T2T1T4A1T1T11^TT5^TTATTT2T2^TT15^TTTTA3^TTT2T1^TT5^TT9^TT6^TT2^TT1^TT5^TT1^TT1^TT12^TT1^TT15^TT7^TT1^TT3^TT3^TT4^TT5^TT1^TT8^TT3^TT1^TT3^TT3^TT1^TT2^TT1^TT5^TT4^TT2^TT1^TT3^TT4^TT3^TT3^TT4^TT3^TT4^TT3^TT14^TT3^TT3^TT7^TT4^TT3^TT3^TT4^TT7^TT3^TT4^TT1^TT4^TT3^TT3^TT13^T0T1T5	AS:i:82	XS:i:0"
            pysam_h = sam_string_to_aligned_segment(test_sam)
            forward_seq = pysam_h.get_forward_sequence()
            self.assertEqual(forward_seq,
                             "AACCTAACGACACCACTATCCCTACACCCTATCCAACTACTATTACTCTATTCTACTTATCACCCTACTACTACCTCATCCTCCTCCCTAAAATTTCGAGTAAGTAAAATCAATTTCGTGTCAAAATTCATTAAGGGCATCCTAATAGAGGTTGGTCGGCGATTTTAATAAGTGTATGTTTCGGACGTTCATAAGTTTAAAGTGTTTGTGTTAACGTTTTCGTCTTTGATTTTGGAAGTATCAGTCACTCTAATTTTGTTACGAAGTAGTAAGAATTTCATGGACAATTATTTACGACGATTTATGATTCACGATTTTTTTTTTTCGATCACGACCGTCGACCGACGACCACCGACCGTCGACCACCGAACCTACCATTATTTTTCCTTTTGAAAATATTACTGTTCGTGAGAATATAAGTAAAAAATAGAGTATTGACCTATTGTGTCCCGTCCTAC")
            self.assertEqual(pysam_h.get_reference_sequence(),
                             "CCTcCtCCCTATtAtTAtTATTttTCgATTgTATTATtgTAtTAtTATtATTtCaTtAttTTTCGtGTcAtTAttATtAtTTTCaTtTtATTATTGGGCATTTCCTATTATTTATtGATTGGTTGGTCGGCGATTTTTTATTATTTATtATTGTGTATTTGTTTCGGATTCGTTCATTTATTATTGTTTATTATTATTGTGTTTGTGTTATTATTCGTTTTCGTCTTTGATTTTTTGGATTATTGTATTTCATTGTCATTCTCTATTATTTTTTGTTATTCGATTATTGTATTGTATTATTGATTATTTTTCATTTGGATTCATTATTTTATTTTTATTCGATTCGATTTTTATTTGATTTTCATTCGATTTTTTTTTTTTTCGATTTCATTCGATTCCGTCGATTCCGATTCGATTCCATTCCGATTCCGTCGATTCCATTCCGATTATTCCTATTCCATTTTATTTTTTTCCTTTTGATtAtTATTA")

    def test_is_iupac_base(self):
        with captured_output() as (_, _):
            for char in IUPAC_BASES:
                self.assertTrue(is_iupac_base(char))
                self.assertTrue(is_iupac_base(char.lower()))

            self.assertFalse(is_iupac_base("F"))

    def test_iupac_complement(self):
        with captured_output() as (_, _):
            handle = ReverseComplement()
            for char in IUPAC_BASES:
                bases = iupac_base_to_bases(char)
                complement = iupac_complement(char)
                complement_chars = iupac_base_to_bases(complement)
                for x in bases:
                    self.assertTrue(handle.complement(x) in complement_chars)

    def test_iupac_base_to_bases(self):
        with captured_output() as (_, _):
            self.assertRaises(AssertionError, iupac_base_to_bases, "F")

    def test_is_non_canonical_iupac_base(self):
        with captured_output() as (_, _):
            self.assertFalse(is_non_canonical_iupac_base("A"))
            self.assertFalse(is_non_canonical_iupac_base("T"))
            self.assertFalse(is_non_canonical_iupac_base("G"))
            self.assertFalse(is_non_canonical_iupac_base("C"))
            for char in IUPAC_BASES:
                if char not in "ATGC":
                    self.assertTrue(is_non_canonical_iupac_base(char))

    def test_kmer_iterator(self):
        with captured_output() as (_, _):
            a = [x for x in kmer_iterator("ATGC", 2)]
            self.assertEqual(len(a), 3)
            a = [x for x in kmer_iterator("AAAA", 3)]
            self.assertEqual(len(a), 2)

    def test_count_all_sequence_kmers(self):
        with captured_output() as (_, _):
            kmers = count_all_sequence_kmers("ATGC", 2, rev_comp=False)
            self.assertEqual(len(kmers), 3)
            kmers = count_all_sequence_kmers("AAAA", 3, rev_comp=True)
            self.assertEqual(len(kmers), 2)
            self.assertEqual(kmers["AAA"], 2)
            self.assertEqual(kmers["TTT"], 2)
            kmers = count_all_sequence_kmers("AAAA", 3, rev_comp_only=True)
            self.assertEqual(len(kmers), 1)
            self.assertEqual(kmers["TTT"], 2)

class CigarTest(unittest.TestCase):
    """Test the functions in Cigar class"""

    @classmethod
    def setUpClass(cls):
        super(CigarTest, cls).setUpClass()
        cigar = "1X1=1M1I1D1N1N1P1S1H"
        cls.base = Cigar(cigar)

    def test_accuracy_from_cigar(self):
        with captured_output() as (_, _):
            acc = self.base.accuracy_from_cigar()
            self.assertEqual(acc, 2 / 5)
            self.assertEqual(Cigar("10M").accuracy_from_cigar(), 1)
            with self.assertRaises(AssertionError):
                Cigar("234Y").accuracy_from_cigar()

    def test_reverse_cigar(self):
        with captured_output() as (_, _):
            rev_cigar = self.base.reverse_cigar()
            self.assertEqual(rev_cigar, "1S1P2N1D1I2M1X")
            cigar = "6M2I3M"
            base = Cigar(cigar)
            rev_cigar = base.reverse_cigar()
            self.assertEqual(rev_cigar, "3M2I6M")


class SeqAlignmentTest(unittest.TestCase):
    """Test the functions in SeqAlignment class"""

    @classmethod
    def setUpClass(cls):
        super(SeqAlignmentTest, cls).setUpClass()
        ref = "ABCDEFFFGGGAA"
        query = "AABCCEGGGTTAAf"
        cigar = "1S5M3D3M2I2M1S"
        cls.base = SeqAlignment(cigar=cigar, ref=ref, query=query)

    def test_initialize(self):
        with captured_output() as (_, _):
            self.assertEqual(17, len(self.base.full_alignment_map))
            self.assertEqual(15, len(self.base.alignment_map))
            self.assertEqual(9, len(self.base.true_matches_map))
            self.assertEqual(len(self.base.ref_map), 13)
            self.assertEqual(len(self.base.query_map), 14)

    def test_alignment_accuracy(self):
        with captured_output() as (_, _):
            characters = [chr(x) for x in range(108, 122)]
            for x in range(10):
                size = np.random.randint(10, 30)
                query = ''.join(np.random.choice(characters, size=size))
                size = np.random.randint(10, 30)
                reference = ''.join(np.random.choice(characters, size=size))
                cigar = get_pairwise_cigar(query=query, ref=reference)
                acc = Cigar(cigar).accuracy_from_cigar()
                sa_handle = SeqAlignment(cigar=cigar, ref=reference, query=query)
                self.assertEqual(acc, sa_handle.alignment_accuracy())


class ReferenceHandlerTest(unittest.TestCase):
    """Test functions in ReferenceHandler"""

    @classmethod
    def setUpClass(cls):
        super(ReferenceHandlerTest, cls).setUpClass()
        cls.HOME = '/'.join(os.path.abspath(__file__).split("/")[:-1])
        cls.fasta = os.path.join(cls.HOME,
                                 "test_files/test.fa")
        cls.reference = os.path.join(cls.HOME,
                                     "test_files/ecoli_k12_mg1655.fa")
        cls.base = ReferenceHandler(cls.reference)

    def test_get_sequence(self):
        with captured_output() as (_, _):
            with tempfile.TemporaryDirectory() as tempdir:
                path = os.path.join(tempdir, "test.fa")
                with open(path, "w") as tmp:
                    tmp.write(">header \n ATGC")
                test = ReferenceHandler(path).get_sequence(chromosome_name="header", start=0, stop=4)
                self.assertEqual("ATGC", test)
                os.remove(path)

            ref_sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGCTTCTGAACTG"
            sequence = self.base.get_sequence(chromosome_name="Chromosome", start=0, stop=len(ref_sequence))
            self.assertEqual(ref_sequence, sequence)

    def test_get_chr_sequence_length(self):
        with captured_output() as (_, _):
            with tempfile.TemporaryDirectory() as tempdir:
                path = os.path.join(tempdir, "test.fa")
                with open(path, "w") as tmp:
                    tmp.write(">header \n ATGC")
                test_len = ReferenceHandler(path).get_chr_sequence_length(chromosome_name="header")
                self.assertEqual(4, test_len)
                os.remove(path)

            test = self.base.get_chr_sequence_length(chromosome_name="Chromosome")
            self.assertEqual(4641652, test)

    def test_write_new_reference(self):
        with captured_output() as (_, _):
            with tempfile.TemporaryDirectory() as tempdir:
                path = os.path.join(tempdir, "test.fa")
                with open(path, "w") as tmp:
                    tmp.write(">header \n ATGC\n")
                    tmp.write(">header2 \n EGF")

                new_ref = ReferenceHandler(path).write_new_reference(outpath=tempdir, reverse=True, complement=True,
                                                                     find="ATGCEF", replace="TACGFE")
                rev_comp_handle = ReferenceHandler(new_ref)
                rev_comp_1 = rev_comp_handle.get_sequence(chromosome_name="header_reverse_complement", start=0, stop=4)
                self.assertEqual("GCAT", rev_comp_1)
                rev_comp_2 = rev_comp_handle.get_sequence(chromosome_name="header2_reverse_complement", start=0, stop=4)
                self.assertEqual("ECF", rev_comp_2)

                os.remove(path)
                os.remove(new_ref)


class ReverseComplementTest(unittest.TestCase):
    """Test the functions in ReverseComplement class"""

    @classmethod
    def setUpClass(cls):
        super(ReverseComplementTest, cls).setUpClass()
        cls.HOME = '/'.join(os.path.abspath(__file__).split("/")[:-1])
        cls.fasta = os.path.join(cls.HOME,
                                 "test_files/test.fa")
        cls.fastq = os.path.join(cls.HOME,
                                 "test_files/test.fastq")

        cls.reference = os.path.join(cls.HOME,
                                     "test_files/ecoli_k12_mg1655.fa")
        cls.base = ReverseComplement()

    def test_instantiation(self):
        with captured_output() as (_, _):
            self.assertEqual(ReverseComplement().find, "ATGC")
            self.assertEqual(ReverseComplement().replace, "TACG")

            with self.assertRaises(AssertionError):
                ReverseComplement(find="asdfe")
                ReverseComplement(replace="asdfe")
                ReverseComplement(find="asdfe", replace="poiuyq")
            with self.assertRaises(AssertionError):
                ReverseComplement(find="aa", replace="at")

    def test_complement(self):
        with captured_output() as (_, _):
            test = self.base.complement("ATGC")
            self.assertEqual(test, "TACG")
            with self.assertRaises(AttributeError):
                self.base.complement(1)
            testbase = ReverseComplement(find="a1", replace="c2")
            self.assertEqual(testbase.complement("A1"), "C2")
            self.assertEqual(testbase.complement("a1"), "C2")

    def test_reverse(self):
        with captured_output() as (_, _):
            test = self.base.reverse("ATGC")
            self.assertEqual(test, "CGTA")
            with self.assertRaises(AttributeError):
                self.base.reverse(1)
            self.assertEqual(self.base.reverse("A1"), "1A")
            self.assertEqual(self.base.reverse("a1"), "1A")

    def test_reverse_complement(self):
        with captured_output() as (_, _):
            test = self.base.reverse_complement("ATGC")
            self.assertEqual(test, "GCAT")
            with self.assertRaises(AttributeError):
                self.base.reverse_complement(1)
            testbase = ReverseComplement(find="a1", replace="c2")
            self.assertEqual(testbase.reverse_complement("A1"), "2C")
            self.assertEqual(testbase.reverse_complement("a1"), "2C")

    def test_convert_write_fasta(self):
        with captured_output() as (_, _):
            with tempfile.TemporaryDirectory() as tempdir:
                path = os.path.join(tempdir, "test.fasta")
                self.base.convert_write_fasta(self.fasta, path, complement=True, reverse=True)
                bad_path = os.path.join(tempdir, "test.txt")
                for header, sequence in read_fasta(path):
                    self.assertTrue(header.endswith("reverse_complement"))
                    self.assertTrue(sequence,
                                    "TCAGTTCAGAAGCTGCTATCAGACACTCTTTTTTTAATCCACACAGAGACATATTGCCCGTTGCAGTCAGAATGAAAAGCT")
                os.remove(path)
            with self.assertRaises(AssertionError):
                self.base.convert_write_fasta(self.fasta, bad_path, complement=True, reverse=True)
                self.base.convert_write_fasta(self.fasta, path, complement=False, reverse=False)

    def test_convert_write_fastq(self):
        with captured_output() as (_, _):
            with tempfile.TemporaryDirectory() as tempdir:
                path = os.path.join(tempdir, "test.fastq")
                ReverseComplement(find="AUGC", replace="ATGC").convert_write_fastq(self.fastq, path, complement=True,
                                                                                   reverse=True)
                bad_path = os.path.join(tempdir, "test.txt")
                for new_record, record in zip(SeqIO.parse(path, "fastq"), SeqIO.parse(self.fastq, "fastq")):
                    self.assertTrue(new_record.id.endswith("reverse_complement"))
                    self.assertTrue(str(new_record.seq).find("U") == -1)
                self.assertEqual(str(new_record.seq),
                                 "AACCTAACGACACCACTATCCCTACACCCTATCCAACTACTATTACTCTATTCTACTTATCACCCTACTACTACCTCATCCTCCTCCCTAAAATTTCGAGTAAGTAAAATCAATTTCGTGTCAAAATTCATTAAGGGCATCCTAATAGAGGTTGGTCGGCGATTTTAATAAGTGTATGTTTCGGACGTTCATAAGTTTAAAGTGTTTGTGTTAACGTTTTCGTCTTTGATTTTGGAAGTATCAGTCACTCTAATTTTGTTACGAAGTAGTAAGAATTTCATGGACAATTATTTACGACGATTTATGATTCACGATTTTTTTTTTTCGATCACGACCGTCGACCGACGACCACCGACCGTCGACCACCGAACCTACCATTATTTTTCCTTTTGAAAATATTACTGTTCGTGAGAATATAAGTAAAAAATAGAGTATTGACCTATTGTGTCCCGTCCTAC")
                self.assertEqual(new_record.letter_annotations["phred_quality"],
                                 record.letter_annotations["phred_quality"][::-1])
                os.remove(path)
            with self.assertRaises(AssertionError):
                self.base.convert_write_fastq(self.fastq, bad_path, complement=True, reverse=True)
                self.base.convert_write_fastq(self.fastq, path, complement=False, reverse=False)


class PysamWrapperTest(unittest.TestCase):
    """Test the functions in PysamWrapper class"""

    @classmethod
    def setUpClass(cls):
        """Setup class"""
        super(PysamWrapperTest, cls).setUpClass()
        cls.HOME = '/'.join(os.path.abspath(__file__).split("/")[:-1])
        cls.test_sam_file = os.path.join(cls.HOME,
                                         "test_files/test_sam_file.sam")
        cls.reference = os.path.join(cls.HOME,
                                     "test_files/ecoli_k12_mg1655.fa")

        cls.header = "@SQ	SN:Chromosome	LN:4641652 \n@PG	ID:bwa	PN:bwa	VN:0.7.15-r1142-dirty	CL:bwa mem -x ont2d /Users/andrewbailey/CLionProjects/nanopore-RNN/signalAlign/bin/test_output/tempFiles_alignment/temp_bwaIndex /Users/andrewbailey/CLionProjects/nanopore-RNN/signalAlign/bin/test_output/tempFiles_alignment/tempFiles_miten_PC_20160820_FNFAD20259_MN17223_mux_scan_AMS_158_R9_WGA_Ecoli_08_20_16_83098_ch138_read23_strand/temp_seq_5048dffc-a463-4d84-bd3b-90ca183f488a.fa\n"
        cls.test_sam = "5048dffc-a463-4d84-bd3b-90ca183f488a\t16\tChromosome\t623201\t57\t14S16M2I2M2I20M1I35M1D9M1D1M1D4M2I1M1I26M1D8M1I8M1D3M1D12M1D5M4D1M2D3M1D14M3D3M1I2M1I8M2D5M3D6M2D25M1I2M1I26M2I31M5D2M1D23M1D4M1D16M1D6M1I3M1I2M1I13M11S\t*\t0\t0\tAAACATAAACAGAACCACGGGTCCGTCTGGGCCCGACGACGCCGAGGTGGATTTTAGGGCGTGGCTTATCTGGCGCTGTTCGGCTGGTTGAGGCGGTCAGCCTTGCCGTCGTAACACATCACGCTGCAATCGCAAACCCGGAAGTTGATGTTAGGCGATTAACGGCTTCAGACCTACAGACGGGCGACGCCGGCTACAGGCGCCGCGGTCGAAGCGCCGATGACACCGGCTGTTTCCGCAAGCCGCCGAGCTTGCCTGGCCTGTTGATTATCTATGCAAGTTGTCATTGCTGGTGCCGGTGGAGTCATGACGCCAGACGCCGCCGCAGGTACAGAACCGACAGTTAATGCTAAAACAAGCAACACGTAAACCGAACCGGGAAGTACGG\t*\tNM:i:102\tMD:Z:3T0T4T2T5T2T5T17T2G24^T9^T1^G6C2T3C0A1T7A6^C8C7^G3^G9T2^G0T0G3^GGCG1^AG0A2^G0T9T3^ATA3G6T2^TG3G1^TTT0G0G4^GA0T11T2C16G0G0T0T0T3T0T11G2G0T5T11T8^TGCGA2^T1T0T20^G4^C0G0T14^T9G2T3G2T1T2\tAS:i:159\tXS:i:0\n"

        cls.pysamwrapper = initialize_pysam_wrapper(cls.header + cls.test_sam)
        cls.as_wrapper = initialize_aligned_segment_wrapper(cls.test_sam)

    def test_get_reference_sequence(self):
        with captured_output() as (_, _):
            seq_1 = self.pysamwrapper.get_reference_sequence()
            test_sam_no_mz = "5048dffc-a463-4d84-bd3b-90ca183f488a\t16\tChromosome\t623201\t57\t14S16M2I2M2I20M1I35M1D9M1D1M1D4M2I1M1I26M1D8M1I8M1D3M1D12M1D5M4D1M2D3M1D14M3D3M1I2M1I8M2D5M3D6M2D25M1I2M1I26M2I31M5D2M1D23M1D4M1D16M1D6M1I3M1I2M1I13M11S\t*\t0\t0\tAAACATAAACAGAACCACGGGTCCGTCTGGGCCCGACGACGCCGAGGTGGATTTTAGGGCGTGGCTTATCTGGCGCTGTTCGGCTGGTTGAGGCGGTCAGCCTTGCCGTCGTAACACATCACGCTGCAATCGCAAACCCGGAAGTTGATGTTAGGCGATTAACGGCTTCAGACCTACAGACGGGCGACGCCGGCTACAGGCGCCGCGGTCGAAGCGCCGATGACACCGGCTGTTTCCGCAAGCCGCCGAGCTTGCCTGGCCTGTTGATTATCTATGCAAGTTGTCATTGCTGGTGCCGGTGGAGTCATGACGCCAGACGCCGCCGCAGGTACAGAACCGACAGTTAATGCTAAAACAAGCAACACGTAAACCGAACCGGGAAGTACGG\t*\tNM:i:102\tAS:i:159\tXS:i:0\n"
            another_instance = initialize_pysam_wrapper(self.header + test_sam_no_mz, reference_path=self.reference)
            seq_2 = another_instance.get_reference_sequence()
            self.assertEqual(seq_1, seq_2)
            self.assertEqual(self.as_wrapper.get_reference_sequence(), seq_2)
            # test as_wrapper
            test_sam_no_mz = "5048dffc-a463-4d84-bd3b-90ca183f488a\t16\tChromosome\t623201\t57\t14S16M2I2M2I20M1I35M1D9M1D1M1D4M2I1M1I26M1D8M1I8M1D3M1D12M1D5M4D1M2D3M1D14M3D3M1I2M1I8M2D5M3D6M2D25M1I2M1I26M2I31M5D2M1D23M1D4M1D16M1D6M1I3M1I2M1I13M11S\t*\t0\t0\tAAACATAAACAGAACCACGGGTCCGTCTGGGCCCGACGACGCCGAGGTGGATTTTAGGGCGTGGCTTATCTGGCGCTGTTCGGCTGGTTGAGGCGGTCAGCCTTGCCGTCGTAACACATCACGCTGCAATCGCAAACCCGGAAGTTGATGTTAGGCGATTAACGGCTTCAGACCTACAGACGGGCGACGCCGGCTACAGGCGCCGCGGTCGAAGCGCCGATGACACCGGCTGTTTCCGCAAGCCGCCGAGCTTGCCTGGCCTGTTGATTATCTATGCAAGTTGTCATTGCTGGTGCCGGTGGAGTCATGACGCCAGACGCCGCCGCAGGTACAGAACCGACAGTTAATGCTAAAACAAGCAACACGTAAACCGAACCGGGAAGTACGG\t*\tNM:i:102\tAS:i:159\tXS:i:0\n"
            another_instance = initialize_aligned_segment_wrapper(test_sam_no_mz, reference_path=self.reference)
            seq_2 = another_instance.get_reference_sequence()
            self.assertEqual(self.as_wrapper.get_reference_sequence(), seq_2)

            # test insert and deletes
            test_sam = "r001\t163\tChromosome\t1\t30\t6M1I1D\t=\t37\t39\tAGCTTTC\t*\tXX:B:S,12561,2,20,112"  # \tMD:Z:6T"
            insert_delete = initialize_pysam_wrapper(self.header + test_sam, reference_path=self.reference)
            seq_1 = insert_delete.get_reference_sequence()
            self.assertEqual(seq_1, "AGCTTTT")
            # test as_wrapper
            insert_delete = initialize_aligned_segment_wrapper(test_sam, reference_path=self.reference)
            seq_1 = insert_delete.get_reference_sequence()
            self.assertEqual(seq_1, "AGCTTTT")

            # test mismatch
            test_sam = "r001\t163\tChromosome\t1\t30\t6M1X\t=\t37\t39\tAGCTTTC\t*\tXX:B:S,12561,2,20,112"  # \tMD:Z:6T"
            with_ref = initialize_pysam_wrapper(self.header + test_sam, reference_path=self.reference)
            seq_1 = with_ref.get_reference_sequence()
            self.assertEqual(seq_1, "AGCTTTT")
            with self.assertRaises(AssertionError):
                initialize_pysam_wrapper(self.header + test_sam)
            # test as_wrapper
            with_ref = initialize_aligned_segment_wrapper(test_sam, reference_path=self.reference)
            seq_1 = with_ref.get_reference_sequence()
            self.assertEqual(seq_1, "AGCTTTT")
            with self.assertRaises(AssertionError):
                initialize_aligned_segment_wrapper(test_sam)

            # use MD:Z field
            test_sam = "r001\t163\tChromosome\t1\t30\t6M1X\t=\t37\t39\tAGCTTTC\t*\tXX:B:S,12561,2,20,112\tMD:Z:6T"
            no_ref = initialize_pysam_wrapper(self.header + test_sam)
            # match with reference
            fasta_handle = ReferenceHandler(self.reference)
            ref_sequence = fasta_handle.get_sequence(chromosome_name=no_ref.alignment_segment.reference_name,
                                                     start=no_ref.alignment_segment.reference_start,
                                                     stop=no_ref.alignment_segment.reference_end)

            seq_2 = no_ref.get_reference_sequence()
            self.assertEqual(seq_2, "AGCTTTT")
            self.assertEqual(ref_sequence, "AGCTTTT")
            # test as_wrapper
            no_ref = initialize_aligned_segment_wrapper(test_sam)
            # match with reference
            fasta_handle = ReferenceHandler(self.reference)
            ref_sequence = fasta_handle.get_sequence(chromosome_name=no_ref.alignment_segment.reference_name,
                                                     start=no_ref.alignment_segment.reference_start,
                                                     stop=no_ref.alignment_segment.reference_end)

            seq_2 = no_ref.get_reference_sequence()
            self.assertEqual(seq_2, "AGCTTTT")
            self.assertEqual(ref_sequence, "AGCTTTT")

    def test_initialize(self):
        with captured_output() as (_, _):
            # use MD:Z field
            test_sam = "r001\t0\tChromosome\t1\t30\t6M1S\t=\t37\t39\tAGCTTTC\t*\tXX:B:S,12561,2,20,112\tMD:Z:6"
            no_ref = initialize_aligned_segment_wrapper(test_sam)
            matches_map = no_ref.seq_alignment.matches_map
            self.assertEqual(matches_map[0], no_ref.seq_alignment.base_alignment(0, "A", 0, "A"))

            test_sam = "r001\t16\tChromosome\t1\t30\t1S6M\t=\t37\t39\tGAAAGCT\t*\tXX:B:S,12561,2,20,112\tMD:Z:6"
            no_ref = initialize_aligned_segment_wrapper(test_sam)
            matches_map2 = no_ref.seq_alignment.matches_map

            self.assertEqual(matches_map2[0], no_ref.seq_alignment.base_alignment(0, "A", 0, "A"))
            for x, y in zip(matches_map, matches_map2):
                self.assertEqual(x, y)


if __name__ == '__main__':
    unittest.main()
