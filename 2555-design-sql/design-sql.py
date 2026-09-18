"""
names and columns are the same length

each row has an id with autoincrement
"""
from collections import defaultdict
class SQL:

    def __init__(self, names: list[str], columns: list[int]):
        self.counter = defaultdict(int)
        self.tables = set(names)
        self.table_columns = defaultdict(dict)
        for i, table in enumerate(names):
            self.table_columns[table]=columns[i] 
        self.db = defaultdict(dict)
    def ins(self, name: str, row: list[str]) -> bool:
        if (name not in self.tables or 
        len(row) != self.table_columns[name]):
            return False
        self.counter[name]+=1
        self.db[name][self.counter[name]] = row
        return True

    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.db:
            return
        if rowId not in self.db[name]:
            return
        del self.db[name][rowId]

    def sel(self, name: str, rowId: int, columnId: int) -> str:

        if name not in self.db:
            return "<null>"
        
        if rowId not in self.db[name]:
            return "<null>"
        
        if columnId > (len(self.db[name][rowId])):
            return "<null>"
        return self.db[name][rowId][columnId-1]

    def exp(self, name: str) -> list[str]:
        if name not in self.tables: return []
        res = []
        for key, row in self.db[name].items():
            item = f'{key},'
            item+=','.join(row)
            res.append(item)
        return res


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)