import json, os, datetime
from datetime import datetime
from pathlib import Path

class DB:
    context = None
    def __init__(self, name) -> None:
        self.path = (Path(__file__).parent).joinpath(f"store/{name}.json")
        if not os.path.exists("store/data.json"):
            with open(self.path, "w") as jsonFile:
                json.dump({}, jsonFile, indent=2)
                self.context = {}
                jsonFile.close()
        else:
            with open(self.path, "r") as jsonFile:
                self.context = json.load(jsonFile, strict=False)

    def Add(self, date: datetime, data, isEnd = False):
        if self._DateIsValid(date):
            self.context[f"{date.year}{date.month}{date.day}{date.hour}{date.minute}0"] = data

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
        if date.second > 60 or date.second < 0:
            return False
        if date.hour > 24 or date.hour < 1:
            return False
        if date.day > 31 or date.day < 1:
            return False
        if date.month > 12 or date.month < 1:
            return False
        return True


class Id:
    year: int
    month: int
    day: int
    hour: int
    second: int

    def __init__(self, year, month, day, hour, second) -> None:
        if second > 60 or second < 0:
            raise ValueError(second)
        if hour > 24 or hour < 1:
            raise ValueError(hour)
        if day > 31 or day < 1:
            raise ValueError(day)
        if month > 12 or month < 1:
            raise ValueError(month)

        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.second = second
