import unittest

import pandas as pd


def _prepare_dataframe(table: pd.DataFrame, id_column: str) -> pd.DataFrame:
    table[id_column].sort_values(inplace=True)
    return table.copy()


class CsvComparator(unittest.TestCase):
    """This class compares that one csv is the same to another comparing its shape, name of columns and each value"""

    def setUp(self) -> None:
        print('Fetching first table...')
        self.table_1 = pd.read_csv('path_table_1')
        self.table_2 = pd.read_csv('path_table_2')

    def test_compare_headers(self):
        print('Comparing headers...')
        self.assertListEqual(self.table_1.columns.to_list(), self.table_2.columns.to_list())
        print("Headers compared")

    def test_compare_shape(self):
        print('Comparing shapes...')
        self.assertTrue(self.table_1.shape, self.table_2.shape)
        print("Shapes compared")

    def test_compare_values(self):
        print('Comparing values...')
        for column in self.table_1.columns:
            print(f'Asserting equality in column {column}')
            table_1_column = self.table_1[column].to_list()
            table_2_column = self.table_2[column].to_list()

            for i, cols in enumerate(zip(table_1_column, table_2_column)):
                element_table_1 = cols[0]
                element_table_2 = cols[1]
                if pd.isnull(element_table_1) and pd.isnull(element_table_2):
                    continue

                err_msg = f'Mismatch in column {column}, at index {i}. Values compared for the first table and second' \
                          f'table are: {element_table_1}. {element_table_2}'
                assert element_table_1 == element_table_2, err_msg
        print('Values compared')


if __name__ == '__main__':
    unittest.main()
