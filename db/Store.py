import json, os, datetime
from datetime import datetime
from pathlib import Path

class DB:
    context = None
    def __init__(self, name) -> None:
        self.path = (Path(__file__).parent).joinpath(f"store/{name}.json")
        if not os.path.exists(self.path):
            with open(self.path, "w") as jsonFile:
                json.dump({}, jsonFile, indent=2)
                self.context = {}
                jsonFile.close()
        else:
            with open(self.path, "r") as jsonFile:
                self.context = json.load(jsonFile, strict=False)

    def Add(self, date: datetime, data, isEnd = False):
        try:
            if not self._DateIsValid(date):
                raise TypeError("Date is not valid")

            id = f"{date.year}{date.month}{date.day}{date.hour}{date.minute}{'1' if isEnd else '0'}"
            if id in self.context:
                raise ValueError("Same id data is found")

            self.context[id] = data
        except TypeError as t:
            # hata mesajını geri döndürecek
            print(t)
        except ValueError as v:
            # hata mesajını geri döndürecek
            print(v)
    def Remove(self, id):
        pass

    def Update(self, id, model):
        pass

    def GetById(self, id):
        pass

    def GetByObject(self, modelData):
        pass

    def Save(self):
        with open(self.path, "w") as f:
            json.dump(self.context, f, indent=2)
            f.close()

    def _DateIsValid(self, date):
        if date.second > 60 or date.second <= 0:
            return False
        if date.hour > 24 or date.hour < 0:
            return False
        if date.day > 31 or date.day < 1:
            return False
        if date.month > 12 or date.month < 1:
            return False
        return True
