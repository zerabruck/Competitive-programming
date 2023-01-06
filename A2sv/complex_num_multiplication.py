class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        complex_numbers = []
        real_numbers = []

        num1 = num1.split("+")
        num2 = num2.split("+")

        for i in num1:
            for j in num2:
                if 'i' not in i and 'i' not in j:
                    product = int(i) * int(j)
                    real_numbers.append(product)
                elif 'i' in i and 'i' in j:
                    product = (int(i[:-1]) * int(j[:-1])) * -1
                    real_numbers.append(product)
                elif 'i' in i and 'i' not in j:
                    product = int(i[:-1]) * int(j)
                    complex_numbers.append(product)
                else:
                    product = int(i) * int(j[:-1])
                    complex_numbers.append(product)

        real_num_sum = sum(real_numbers)
        complex_num_sum = sum(complex_numbers)

        result = f"{real_num_sum}+{complex_num_sum}i"
        return result

