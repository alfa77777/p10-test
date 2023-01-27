class GetNextPrimeTill1000:

    @staticmethod
    def split_prime():
        prime_list = []
        non_prime = []
        for i in range(2, 1001):
            for e in range(2, int((i ** (1 / 2)) // 1) + 1):
                if i % e == 0:
                    non_prime.append(" ")
            if len(non_prime) == 0:
                prime_list.append(i)
            else:
                non_prime = []

        return prime_list

    @staticmethod
    def generator():
        for number in GetNextPrimeTill1000.split_prime():
            yield number


prime_numbers = GetNextPrimeTill1000.generator()
for prime in prime_numbers:
    print(next(prime_numbers))
