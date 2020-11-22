class Validator:
    @staticmethod
    def validate_input(row, column, sign):
        if not row.isdigit() or not column.isdigit():
            raise ValueError("Row and Column must be integers!")
        if not(0<= int(row) <6 ) or not (0<= int(column)<6):
            raise ValueError("Move outside the board!")
        if sign not in ["X", "O"]:
            raise ValueError("Invalid Sign")
class BoardError(Exception):
    pass
class SaveError(Exception):
    pass
