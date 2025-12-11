"""My answer for Day 3"""


class DayThreeSolver:
    def __init__(self):
        self.inputs = []
        self.final_answer = 0

    def read_txt_as_list(self, input_file: str = "day-3/input.txt") -> list:
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

    def get_highest_voltage(self, battery_bank: str) -> int:
        highest_jolt = 0
        num_batteries = len(battery_bank)
        for i in range(num_batteries):
            for j in range(num_batteries)[i:]:
                if i != j:
                    jolt_str = battery_bank[i] + battery_bank[j]
                    jolt_int = int(jolt_str)
                    if jolt_int > highest_jolt:
                        highest_jolt = jolt_int
        return highest_jolt

    def process_all_input(self) -> None:
        self.inputs = self.read_txt_as_list(input_file="day-3/input.txt")
        for battery_bank in self.inputs:
            self.final_answer += self.get_highest_voltage(battery_bank)
        print(f"Final answer: {self.final_answer}")


if __name__ == "__main__":
    my_answer = DayThreeSolver()
    my_answer.process_all_input()
