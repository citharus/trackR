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

__all__: list = ['Database']


class Database:
    __instance: None = None
    __table: dict = dict()

    def __new__(cls) -> 'Database':
        if not cls.__instance:
            cls.__instance: 'Database' = super(Database, cls).__new__(cls)
        return cls.__instance

    def add(self, key, value) -> None:
        self.__table[key] = value

    def update(self, key, value) -> None:
        try:
            self.__table[key] = value
        except KeyError:
            raise Exception(f'Entry "{key}" does not exist.')

    def remove(self, key) -> None:
        try:
            del self.__table[key]
        except KeyError:
            raise Exception(f'Entry "{key}" does not exist.')