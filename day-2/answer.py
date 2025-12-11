"""My answer for Day 2"""


class DayTwoSolver:
    def __init__(self, is_part_one):
        self.input = []
        self.final_answer = 0
        self.is_part_one = is_part_one

    def read_txt_to_list(self, input_file: str = "day-2/input.txt") -> list:
        """Read .txt file as Python list

        Returns:
            list: List version of input.txt files
        """
        try:
            with open(input_file, "r", encoding="utf-8") as input_text:
                inputs = input_text.readline().split(",")
                return inputs
        except FileNotFoundError as file_not_found_error:
            print(f"Erm, can't find that file: {file_not_found_error}")

    def is_valid(self, id_string: str) -> bool:
        """Determines if an id string is valid (for Part One)

        Args:
            id_string (str): ID string (ex. "123123")

        Returns:
            bool: True if string is not symmetric (so is valid)
        """
        id_string_length = len(id_string)
        if id_string_length % 2 == 1:
            return True

        mid_point_index = id_string_length // 2
        is_symmetric = id_string[:mid_point_index] == id_string[mid_point_index:]
        return not is_symmetric

    def get_all_divisors(self, some_num: int) -> list[int]:
        """Helper function for Part Two

        Args:
            some_num (int): Number (length of string) to get all int divisors of

        Returns:
            list[int]: List of all divisors
        """
        all_divisors = []
        for i in range(1, some_num):
            if some_num % i == 0:
                all_divisors.append(i)
        return all_divisors

    def is_valid_part_two(self, id_string: str) -> bool:
        """is_valid() equivalent for Part Two.

        Args:
            id_string (str): ID string (ex. "123123")

        Returns:
            bool: True if string does not have repeating substrings
                (so is valid)
        """
        id_string_length = len(id_string)
        all_divisors = self.get_all_divisors(id_string_length)
        for divisor in all_divisors:
            id_substring = id_string[:divisor]
            num_substring = id_string_length // divisor
            if (id_substring * num_substring) == id_string:
                return False
        return True

    def traverse_id_range(self, id_ranges: str) -> None:
        """Traverses range of IDs

        Args:
            id_ranges (str): ID range (ex. "11-22")
        """
        start_id_str, end_id_str = id_ranges.split(sep="-", maxsplit=2)
        start_id = int(start_id_str)
        end_id = int(end_id_str)

        for some_id in range(start_id, end_id + 1):
            if self.is_valid(str(some_id)) and self.is_part_one:
                continue

            if self.is_valid_part_two(str(some_id)):
                continue

            self.final_answer += some_id
            print(f"Found invalid ID: {some_id}")

    def process_all_input(self) -> None:
        """Main entry function"""
        self.input = self.read_txt_to_list(input_file="day-2/input.txt")
        for some_range in self.input:
            self.traverse_id_range(some_range)
        print(f"Final answer: {self.final_answer}")


if __name__ == "__main__":
    my_answer = DayTwoSolver(is_part_one=False)
    my_answer.process_all_input()
