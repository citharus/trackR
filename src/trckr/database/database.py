#  MIT License
#
#  Copyright (c) 2021-present citharus
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from typing import Iterator

from trckr.database import Table

__all__: list = ['Database']


class Database:
    __instance: None = None
    __tables: dict = dict()

    def __new__(cls) -> 'Database':
        if not cls.__instance:
            cls.__instance: 'Database' = super(Database, cls).__new__(cls)
        return cls.__instance

    def __iter__(self) -> Iterator:
        return iter(self.__tables)

    def __getitem__(self, table_name: str) -> Table:
        return self.__tables[table_name]

    def __setitem__(self, table_name: str, table: Table) -> None:
        self.__tables[table_name] = table

    def __delitem__(self, table_name: str) -> None:
        del self.__tables[table_name]

    def create_table(self, table_name: str) -> Table:
        table = self[table_name] = Table()
        return table

    def delete_table(self, table_name: str) -> None:
        try:
            del self[table_name]
        except KeyError:
            raise Exception(f'Table "{table_name}" does not exist.')
