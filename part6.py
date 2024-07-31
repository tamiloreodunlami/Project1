class PeekableIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.extra = None
        self.extra_filled = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.extra_filled:
            next_element = self.extra
            self.extra = None
            self.extra_filled = None
            return next_element
        return next(self.iterator)

    def peek(self):
        if self.extra_filled:
            return self.extra
        peek_element = next(self.iterator)
        self.extra = peek_element
        self.extra_filled = True
        return peek_element


    def has_next(self):
        if self.extra_filled:
            return True
        try:
            next_element = next(self.iterator)
            self.extra = next_element
            self.extra_filled = True
            return True
        except StopIteration:
            return False


def main():

    numbers = [10, 20, 30, 40]
    peekable_iterator = PeekableIterator(numbers)

    print(peekable_iterator.peek())
    print(next(peekable_iterator))
    print(peekable_iterator.peek())
    print(peekable_iterator.has_next())
    print(next(peekable_iterator))
    print(next(peekable_iterator))
    print(peekable_iterator.has_next())
    print(next(peekable_iterator)) 
    print(peekable_iterator.has_next())

if __name__ == "__main__":
    main()

