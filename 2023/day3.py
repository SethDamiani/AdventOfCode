from typing import Optional, Union


class Number:
    def __init__(self, row: int, col: int, num: int) -> None:
        self.row = row
        self.col = col
        self.num = num
    
    def start_col(self) -> int:
        return self.col
    
    def end_col(self) -> int:
        return self.col + len(str(self.num))
    
    def __str__(self) -> str:
        return f"{self.num} at row={self.row} col={self.start_col()}-{self.end_col()}"

class Symbol:
    def __init__(self, row: int, col: int, sym: str) -> None:
        self.row = row
        self.col = col
        self.sym = sym
    
    def start_col(self) -> int:
        return self.col
    
    def end_col(self) -> int:
        return self.col + 1
    
    def __str__(self) -> str:
        return f"{self.sym} at row={self.row} col={self.col}"

class EngineSchematic:
    def __init__(self, filename: str, debug: bool = False) -> None:
        self.numbers: list[Number] = []
        self.symbols: list[Symbol] = []
        self.debug = debug
        # read file
        with open(filename) as f:
            text = [l.strip() for l in f.readlines()]

        self.total_rows = len(text)
        self.total_cols = len(text[0])
        
        text = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]
        
        for n in range(len(text)):
            # find Numbers in row
            col = 0
            acc = ""
            start_index = 0
            while col < len(text[n]):
                current_char = text[n][col]
                if current_char.isnumeric():
                    if len(acc) == 0:
                        start_index = col
                    acc += current_char
                    col += 1
                    if col < len(text[n]):
                        continue
                if acc != "":
                    self.numbers.append(Number(n, start_index, int(acc)))
                acc = ""
                col += 1
            
            # find Symbols in row
            for m in range(len(text[n])):
                char = text[n][m]
                if not char.isnumeric() and char != ".":
                    self.symbols.append(Symbol(n, m, char))
    
    def search(self, row: int, col: int) -> Optional[Union[Number, Symbol]]:
        if self.debug:
            print(f"          searching {row} {col}")
        for symbol in self.symbols:
            if symbol.row == row and symbol.col == col:
                return symbol
        for number in self.numbers:
            if number.row == row and number.start_col() <= col < number.end_col():
                return number
    
    def get_surrounding(self, item: Union[Number, Symbol]) -> set[Union[Number, Symbol]]:
        if self.debug:
            print(f"    finding surrounding of {item}")
        surrounding_items = set()
        start_search_col = 0
        end_search_col = self.total_cols
        # search beside
        if item.start_col() > 0:
            start_search_col = item.start_col() - 1
            if found := self.search(item.row, start_search_col):
                surrounding_items.add(found)
        if item.end_col() < self.total_cols:
            end_search_col = item.end_col()
            if found := self.search(item.row, end_search_col):
                surrounding_items.add(found)
        #search above
        if item.row > 0:
            for col in range(start_search_col, end_search_col+1):
                if found := self.search(item.row-1, col):
                    surrounding_items.add(found)
        # search below
        if item.row < self.total_rows-1:
            for col in range(start_search_col, end_search_col+1):
                if found := self.search(item.row+1, col):
                    surrounding_items.add(found)
        if item in surrounding_items:
            surrounding_items.remove(item)
        if self.debug:
            print(f"      found {len(surrounding_items)} surrounding items")
            for i in surrounding_items:
                print(f"        {i}")
        return surrounding_items
    
    def part1(self) -> int:
        total = 0
        for number in self.numbers:
            surrounding_symbols = [item for item in self.get_surrounding(number) if type(item) == Symbol]
            if len(surrounding_symbols) > 0:
                total += number.num
        return total
    
    def part2(self) -> int:
        total = 0
        for symbol in self.symbols:
            if symbol.sym != "*":
                continue
            surrounding_numbers = [item for item in self.get_surrounding(symbol) if type(item) == Number]
            print(symbol)
            for s in surrounding_numbers:
                print(f"  {s}")
            if len(surrounding_numbers) == 2:
                total += surrounding_numbers[0].num * surrounding_numbers[1].num
        return total


if __name__ == "__main__":
    es = EngineSchematic("2023/day3.txt", False)
    print(es.part1())
    print(es.part2())
