import re

import Utils


class Validator:
    DEFAULT_DATA_NAME = "Unknown"
    DEFAULT_REASON = None
    DEFAULT_NULL_CHECK = True
    DEFAULT_PRESENCE_CHECK = True
    DEFAULT_MIN_LENGTH = 3
    DEFAULT_MAX_LENGTH = 16
    DEFAULT_DATA_TYPE = str
    DEFAULT_ALLOWED_CHARS = None
    DEFAULT_REGEX_CHECK = None
    DEFAULT_UPPER_CASE = False
    DEFAULT_LOWER_CASE = False
    DEFAULT_RANGE_LOWER_BOUND = None
    DEFAULT_RANGE_UPPER_BOUND = None

    def __init__(self, null_check=DEFAULT_NULL_CHECK, presence=DEFAULT_PRESENCE_CHECK, min_length=DEFAULT_MIN_LENGTH, max_length=DEFAULT_MAX_LENGTH, data_type=DEFAULT_DATA_TYPE, allowed_chars=DEFAULT_ALLOWED_CHARS, regex_check=DEFAULT_REGEX_CHECK, upper_case=DEFAULT_UPPER_CASE, lower_case=DEFAULT_LOWER_CASE, range_lower_bound=DEFAULT_RANGE_LOWER_BOUND, range_upper_bound=DEFAULT_RANGE_UPPER_BOUND):
        self.data_name = self.DEFAULT_DATA_NAME
        self.default_reason = self.DEFAULT_REASON

        self.null_check = null_check
        self.presence = presence
        self.min_length = min_length
        self.max_length = max_length
        self.data_type = data_type
        self.allowed_chars = allowed_chars
        self.regex_check = regex_check
        self.upper_case = upper_case
        self.lower_case = lower_case
        self.range_lower_bound = range_lower_bound
        self.range_upper_bound = range_upper_bound

    def reset(self):
        self.data_name = self.DEFAULT_DATA_NAME
        self.default_reason = self.DEFAULT_REASON

        self.null_check = self.DEFAULT_NULL_CHECK
        self.presence = self.DEFAULT_PRESENCE_CHECK
        self.min_length = self.DEFAULT_MIN_LENGTH
        self.max_length = self.DEFAULT_MAX_LENGTH
        self.data_type = self.DEFAULT_DATA_TYPE
        self.allowed_chars = self.DEFAULT_ALLOWED_CHARS
        self.regex_check = self.DEFAULT_REGEX_CHECK
        self.upper_case = self.DEFAULT_UPPER_CASE
        self.lower_case = self.DEFAULT_LOWER_CASE
        self.range_lower_bound = self.DEFAULT_RANGE_LOWER_BOUND
        self.range_upper_bound = self.DEFAULT_RANGE_UPPER_BOUND

    def get_true_reason(self, data):
        if self.null_check and data is None:
            return f"{self.data_name} is null"

        if not self.null_check:
            return None

        if self.presence and data == "":
            return f"{self.data_name} is empty"

        data_type = type(data)

        if data_type == str:
            length = len(data)
            if length < self.min_length or length > self.max_length:
                return f"{self.data_name} is an invalid length"

            for char in data:
                if self.allowed_chars is not None and char not in self.allowed_chars:
                    return f"{self.data_name} contains an invalid character"

            if self.regex_check is not None and not re.match(self.regex_check, data):
                return f"{self.data_name} failed regex check: {self.regex_check}"

        if data_type == int:
            if self.range_lower_bound is not None and data < self.range_lower_bound:
                return f"{self.data_name} is too small"

            if self.range_upper_bound is not None and data > self.range_upper_bound:
                return f"{self.data_name} is too big"

        return None

    def get_reason(self, data):
        reason = self.get_true_reason(data)

        if self.default_reason is not None and reason is not None:
            return self.default_reason

        return reason

    def test(self, data):
        return self.get_reason(data) is None


def main():
    validator = Validator(min_length=2, max_length=25)

    validator.data_name = "Your first name"
    first_name = get_detail(validator, "What is your first name? ")

    validator.data_name = "Your middle name"
    validator.min_length = 0
    validator.max_length = 30
    validator.null_check = False
    middle_names = get_details(validator, "What is your middle name? ")

    validator.data_name = "Your last name"
    validator.min_length = 2
    validator.max_length = 20
    validator.null_check = True
    last_name = get_detail(validator, "What is your last name? ")

    validator.reset()
    validator.data_name = "Your birth date"
    validator.regex_check = "[0-9]{2}/[0-9]{2}/[0-9]{4}"
    validator.default_reason = "Must be in the format of DD/MM/YYYY"
    dob = get_detail(validator, "What is your date of birth? (DD/MM/YYYY) ")

    validator.data_name = "Your phone number"
    validator.min_length = 11
    validator.max_length = 11
    validator.data_type = int
    phone_number = get_detail(validator, "What is your phone number? ")

    validator.reset()
    validator.data_name = "Your sex"
    validator.min_length = 1
    validator.max_length = 1
    validator.allowed_chars = ('M', 'F')
    validator.upper_case = True
    validator.default_reason = "Valid sex': M/F"
    sex = get_detail(validator, "What is your sex? (M/F) ")

    validator.reset()
    validator.data_name = "Your dependents"
    validator.range_lower_bound = 1
    validator.min_length = 1
    validator.max_length = 2
    validator.data_type = int
    number_of_dependents = int(get_detail(validator, "How many dependents do you have? "))

    print()
    print("***Patient Details***")
    print(f"First name: {first_name}")
    print(f"Middle names: {Utils.formatStrList(middle_names)}")
    print(f"Last name: {last_name}")
    print(f"Date of birth: {dob}")
    print(f"Phone number: {phone_number}")
    print(f"Sex: {sex}")
    print(f"Number of dependents: {number_of_dependents}")


def get_details(validator, question):
    details = []

    while True:
        detail = get_detail(validator, question)
        details.append(detail)

        if not Utils.toBool(input(f"Would you like to add another {validator.data_name}? ")):
            break

    return details


def get_detail(validator, question):
    if not question.endswith(" "):
        question += " "

    while True:
        try:
            detail = input(question)

            if validator.data_type != str:
                detail = validator.data_type(detail)

            if type(detail) == str:
                if validator.upper_case:
                    detail = detail.upper()

                if validator.lower_case:
                    detail = detail.lower()

            fail_reason = validator.get_reason(detail)
        except:
            fail_reason = f"{validator.data_name} is of an invalid type"

        if fail_reason is not None:
            print(fail_reason)
            continue

        break

    return detail


if __name__ == "__main__":
    main()
