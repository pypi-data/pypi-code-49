from sdg_utils import dump_bits, nums2bits

if __name__ == '__main__':
    print(dump_bits(0x0001))
    print(dump_bits(0x8000))
    print(dump_bits(0x8080))
    print(bin(nums2bits(1, 2, 3, 4)))
    print(bin(nums2bits(1, 2, 3, 4, shift=-1)))

