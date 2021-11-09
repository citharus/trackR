"""
MIT License

Copyright (c) 2021-present citharus

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import bson

from trckr.database.chart import Chart

if TYPE_CHECKING:
    from typing import Iterator

__all__: list = ['Database']


class Database:
    __instance: None = None
    __charts: dict = dict()

    def __new__(cls, *args) -> 'Database':
        if not cls.__instance:
            cls.__instance: 'Database' = super().__new__(cls)
        return cls.__instance

    def __init__(self, path: str) -> None:
        self.path: Path = Path(path).expanduser()
        if not self.path.exists():
            self.path.mkdir(parents=True)

    def __iter__(self) -> Iterator:
        return iter(self.__charts)

    def __getitem__(self, chart_name: str) -> Chart:
        return self.__charts[chart_name]

    def __setitem__(self, chart_name: str, chart: Chart) -> None:
        self.__charts[chart_name] = chart

    def __delitem__(self, chart_name: str) -> None:
        del self.__charts[chart_name]

    def save(self) -> None:
        for table in self:
            with open(self.path / table, 'wb') as file:
                data: bytes = bson.dumps(dict(self[table].__dict__()))
                file.write(data)

    def load(self) -> None:
        for chart in self.path.iterdir():
            with open(chart, 'rb') as file:
                data: dict = bson.loads(file.read())
                self[chart.name] = Chart(chart.name, entries=data)

    def create_chart(self, chart_name: str) -> Chart:
        chart = self[chart_name] = Chart(chart_name)
        return chart

    def delete_chart(self, chart_name: str) -> None:
        try:
            del self[chart_name]
        except KeyError:
            raise Exception(f'Table "{chart_name}" does not exist.')
