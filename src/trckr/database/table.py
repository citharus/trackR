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

from typing import Iterable, Callable, Any

__all__: list = ['Table']


class Table:
    def __init__(self, name: str, *, entries=None) -> None:
        self.name: str = name
        self.__entries: dict = entries or dict()

    def __len__(self) -> int:
        return len(self.__entries)

    def __iter__(self) -> Iterable['Table']:
        return iter(self.__entries)

    def __dict__(self) -> dict:
        return dict(self.__entries)

    def __getitem__(self, key: Any) -> Any:
        return self.__entries[key]

    def __setitem__(self, key: Any, value: Any) -> None:
        self.__entries[key] = value

    def __delitem__(self, key: Any, value: Any) -> None:
        del self.__entries[key]

    def add(self, key: Any, value: Any) -> None:
        self[key] = value

    def update(self, key: Any, value: Any) -> None:
        try:
            self[key] = value
        except KeyError:
            raise Exception(f'Entry "{key}" does not exist.')

    def delete(self, key: Any) -> None:
        try:
            del self[key]
        except KeyError:
            raise Exception(f'Entry "{key}" does not exist.')

    def query(self, key: Callable = None, limit: int = 10) -> dict:
        return dict(sorted(self.__entries.items(), key=key)[:limit])
