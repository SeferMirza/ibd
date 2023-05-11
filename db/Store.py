import json, os, datetime
from datetime import datetime
from pathlib import Path

class DB:
    __context = None
    def __init__(self, name) -> None:
        self.path = (Path(__file__).parent).joinpath(f"store/{name}.json")
        if not os.path.exists(str(self.path)):
            with open(str(self.path), "w") as jsonFile:
                json.dump({}, jsonFile, indent=2)
                self.__context = {}
                jsonFile.close()
        else:
            with open(self.path, "r") as jsonFile:
                self.__context = json.load(jsonFile, strict=False)

    def add(self, date: datetime, data):
        try:
            if not self.__dateIsValid(date):
                raise TypeError("Date is not valid")

            month, day, hour, minute, second = self.__makeDateValidFormat(date)
            id = f"{date.year}{month}{day}{hour}{minute}{second}"
            if id in self.__context:
                raise ValueError("Same id data is found")

            self.__context[id] = data
        except TypeError as t:
            # hata mesajını geri döndürecek
            print(t)
        except ValueError as v:
            # hata mesajını geri döndürecek
            print(v)

    def getAll(self):
        return self.__context

    def remove(self, id):
        return self.__context.pop(str(id))
        #not find mesajıda eklenecek

    def update(self, id, model):
        self.__context[str(id)] = model
        return model

    def getById(self, id):
        return self.__context[str(id)]

    def getByObject(self, modelData: dict):
        result = {}
        for i in self.__context:
            if modelData.items() <= self.__context[str(i)].items():
                result[str(i)] = self.__context[str(i)]
        return result

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.__context, f, indent=2)
            f.close()

    def __dateIsValid(self, date):
        if date.second > 60 or date.second < 0:
            return False
        if date.hour > 24 or date.hour < 0:
            return False
        if date.day > 31 or date.day < 1:
            return False
        if date.month > 12 or date.month < 1:
            return False
        return True

    def __makeDateValidFormat(self, date):
        month = date.month if date.month >= 10 else f"0{date.month}"
        day = date.day if date.day >= 10 else f"0{date.day}"
        hour = date.hour if date.hour >= 10 else f"0{date.hour}"
        minute = date.minute if date.minute >= 10 else f"0{date.minute}"
        second = date.second if date.second >= 10 else f"0{date.second}"

        return month, day, hour, minute, second