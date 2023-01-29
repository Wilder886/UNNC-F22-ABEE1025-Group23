import json

#treeview getting information function

class HistoryData:
    def __init__(self):
        self.history = json.loads(open('history.json', mode='r', encoding='utf-8').read())

    def all(self):
        return self.history

    def insert(self, history):
        self.history.append(history)

    def get_U_value(self, U_value):

        for u_value in self.history:
            print(u_value)


historydata = HistoryData()


if __name__ == '__main__':
    print(historydata.all())
    print(historydata.get_U_value('111'))