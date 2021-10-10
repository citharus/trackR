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

from typing import Iterator, Any

__all__: list = ['Table']


class Table:
    def __init__(self) -> None:
        self.entries: dict = dict()

    def __len__(self) -> int:
        return len(self.entries)

    def __iter__(self) -> Iterator:
        return iter(self.entries)

    def __getitem__(self, key: Any) -> Any:
        return self.entries[key]

    def __setitem__(self, key: Any, value: Any) -> None:
        self.entries[key] = value

    def add(self, key: Any, value: Any) -> None:
        self.entries[key] = value

    def update(self, key: Any, value: Any) -> None:
        try:
            self.entries[key] = value
        except KeyError:
            raise Exception(f'Entry "{key}" does not exist.')

    def remove(self, key: Any) -> None:
        try:
            del self.entries[key]
        except KeyError:
            raise Exception(f'Entry "{key}" does not exist.')
