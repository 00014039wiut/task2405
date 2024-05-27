import datetime


class TimerContextManager:
    def __init__(self, limit):
        self.limit = limit

    def __enter__(self):
        self.start_time = datetime.datetime.now()
        print(self.start_time)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish = datetime.datetime.now()
        print(self.finish)
        self.difference = self.finish - self.start_time
        print("The time spent on this task is " + str(self.difference))


with TimerContextManager(100000) as manager:
    for i in range(manager.limit):
        print(i * (i + 1))

    print("The context manager is working")
