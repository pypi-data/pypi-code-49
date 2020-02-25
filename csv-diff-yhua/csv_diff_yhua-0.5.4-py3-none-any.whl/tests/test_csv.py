from csv_diff import load_csv, compare
import io

ONE = """id,name,age
1,Cleo,5
2,Pancakes,2"""

TWO = """id,name,age
1,Cleo,5
2,Pancakes,3"""


def test_row_changed_no_key():
    diff = compare(
        load_csv(io.StringIO(ONE)), load_csv(io.StringIO(TWO))
    )
    print(diff)

if __name__ == '__main__':
    print(load_csv(io.StringIO(ONE)))
    print(load_csv(io.StringIO(TWO)))

    test_row_changed_no_key()