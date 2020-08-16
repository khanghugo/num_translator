class ToDecimal:
    def __init__(self, user_input):
        self.user_input = user_input

        self.num_dict = {
            "binary": "01",
            "hexadecimal": "0123456789ABCDEF"
        }

        self.len_dict = {
            "binary": 8,
            "hexadecimal": 2
        }

        if self.num_type():
            self.num_type = self.num_type()
            self.num_list = self.num_list()
            self.base_len = len(self.num_list)
            self.num_len = self.num_len()

            self.result = self.to_decimal()  # is int()

    def num_type(self):
        for key, value in self.len_dict.items():
            if len(self.user_input) == value:
                return key
        else:
            print('Consider using to_decimal_custom')
            return False

    def num_list(self):
        return self.num_dict[self.num_type]

    def num_len(self):
        return len(self.user_input)

    def to_decimal(self):
        result = 0
        for index, num in enumerate(self.user_input):
            eval_num = int(self.num_list.index(num))
            result += (self.base_len ** (self.num_len - 1 - index)) * eval_num
        return result

    def to_decimal_custom(self, s, base_list):
        result = 0
        for index, num in enumerate(s):
            eval_num = int(base_list.index(s))
            result += (len(base_list) ** (len(s) - 1 - index)) * eval_num
        return result


def debug():
    test_string = "00101011"
    test_string = "F1"
    # test_string = "JJFJKD"
    c = ToDecimal(test_string)
    # print(c.result)


if __name__ == "__main__":
    debug()
