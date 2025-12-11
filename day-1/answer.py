"""My answer for Day 1"""

class DayOneSolver:
    """Day One solver
    """
    def __init__(self):
        """Initialize solver variables
        """
        self.input = []
        self.current_position = 50
        self.final_answer = 0
        self.part_one = False

    def read_txt_as_list(self, input_file: str = "day-1/input.txt") -> list:
        """Read .txt file as Python list

        Returns:
            list: List version of input.txt files
        """
        try:
            with open(input_file, "r", encoding="utf-8") as input_text:
                inputs = [line.strip() for line in input_text]
                return inputs
        except FileNotFoundError as file_not_found_error:
            print(f"Erm, can't find that file: {file_not_found_error}")

    def turn_right(self, num_of_moves: int) -> None:
        """Turn right given number of moves

        Args:
            num_of_moves (int): Number of moves to turn
        """
        while num_of_moves > 0:
            self.current_position += 1
            if self.current_position > 99:
                self.current_position = 0
            if self.current_position <= 0 and not self.part_one:
                self.final_answer += 1
            num_of_moves -= 1

    def turn_left(self, num_of_moves: int) -> None:
        """Turn left given number of moves

        Args:
            num_of_moves (int): Number of moves to turn
        """
        while num_of_moves > 0:
            self.current_position -= 1
            if self.current_position < 0:
                self.current_position = 99
            if self.current_position <= 0 and not self.part_one:
                self.final_answer += 1
            num_of_moves -= 1
        
    def process_single_input(self, input_line: str) -> None:
        """Process a single line of instruction

        Args:
            input_line (str): A line of instruction (ex. "R68")
        """
        direction_str = input_line[0]
        num_of_moves = int(input_line[1:])
        if direction_str == "R":
            self.turn_right(num_of_moves)
            return
        self.turn_left(num_of_moves)
    
    def process_all_inputs(self) -> None:
        """Wrapper for looping through every line
        """
        self.input = self.read_txt_as_list(input_file="day-1/input.txt")
        for input_line in self.input:
            print(f"Processing line: {input_line}")
            self.process_single_input(input_line)
            print(f"Current position is: {self.current_position}")
            if self.current_position == 0 and self.part_one:
                self.final_answer += 1
            print("----------")
        print(f"Final answer: {my_answer.final_answer}")
        return


if __name__ == "__main__":
    my_answer = DayOneSolver()
    my_answer.process_all_inputs()