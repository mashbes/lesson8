class StringCalculator():
    def add(self,string):
        if string == '':
            return 0

        elif ',' not in string and '\n' not in string:
            return int(string)

        else:
            sum= 0
            negative_numbers = ''
            separators = (',', '\n')
            for i in separators:
                string = string.replace(i, ' ')
            numbers_string = string.split()

            if numbers_string[0].startswith("//"):
                new_separator = numbers_string[0][2:len(numbers_string[0])]
                numbers_string = numbers_string[1].split(new_separator)

            for number in numbers_string:
                if int(number) < 0:
                    negative_numbers += number + ','

                elif int(number) >= 1000:
                    continue

                else:
                    sum += int(number)

            if negative_numbers != '':
                return 'negative numbers are forbidden:' + negative_numbers[:-1]

            return sum





