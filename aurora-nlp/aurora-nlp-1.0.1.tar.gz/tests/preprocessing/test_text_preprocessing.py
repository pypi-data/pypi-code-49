from aurora import text_preprocessing
from unittest import TestCase
from datetime import datetime


class TestTextPreprocessing(TestCase):
    def test_simple_case(self):
        """
        https://tinhte.vn/thread/netflix-da-ngung-chieu-9-phim-vi-yeu-cau-cua-chinh-phu-cac-nuoc-viet-nam-go-1-phim-singapore-go-5.3079634/
        :return:
        """
        start = datetime.now()
        text = u"xác chết như núi không bằng lão này đi đêm vài lần , https://vi.wikipedia.org/wiki/Henry_Kissinger cơ bản mạng sống binh linh mẽo, việt hoặc một đất nước như những con cờ thôi hi sinh đạt kết quả cuối cùng, hạ liên xô bán một hai đảo đài loan hay nam việt nam cũng chuyện thường."
        actual = text_preprocessing(text)
        expected = "xác chết như núi không bằng lão này đi đêm vài lần , cơ bản mạng sống binh linh mẽo, việt hoặc một đất nước như những con cờ thôi hi sinh đạt kết quả cuối cùng, hạ liên xô bán một hai đảo đài loan hay nam việt nam cũng chuyện thường."
        end = datetime.now()
        diff = end - start
        print(f"Total preprocessing time {diff.microseconds / 1000} ms")
        self.assertEqual(actual, expected)
