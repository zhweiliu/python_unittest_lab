class Calculator:
    # using '*args' means method should accept \
    # multi parameters by ordered
    def add(self, *args):
        result = 0

        for n in args:
            result += n

        return result
