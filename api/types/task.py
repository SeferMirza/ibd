class Task:
    def __init__(self):
        self.__start = None
        self.__end = None
        self.__task = None

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, value):
        self.__start = value

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, value):
        self.__end = value

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, value):
        self.__task = value

    def getDict(self):
        return {
            "start": self.start,
            "task": self.task,
            "end": self.end
        }