class Date:
    @classmethod
    def get_number(cls, the_date):
        cls.the_date = the_date.split('-')
        new_date = []
        for el in cls.the_date:
            new_date.append(int(el))
        print(Date.valid_number(new_date))

    @staticmethod
    def valid_number(numbers):
        if numbers[0] > 31:
            numbers[0] = 31
        elif numbers[0] < 1:
            numbers[0] = 1
        if numbers[1] > 12:
            numbers[1] = 12
        elif numbers[1] < 1:
            numbers[1] = 1
        if numbers[2] < 2000:
            numbers[2] = 2000
        elif numbers[2] > 2080:
            numbers[2] = 2080
        new_numbers = []
        for el_1 in numbers:
            new_numbers.append(str(el_1))
        new_numbers = '-'.join(new_numbers)
        return new_numbers


Date.get_number(input('Введите дату в формате день-месяц-год: '))



