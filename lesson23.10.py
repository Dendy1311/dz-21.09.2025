class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __iter__(self):
        self.outer_index = 0
        self.inner_index = 0
        return self

    def __next__(self):
        while self.outer_index < len(self.list_of_lists):
            current_list = self.list_of_lists[self.outer_index]
            if self.inner_index < len(current_list):
                item = current_list[self.inner_index]
                self.inner_index += 1
                return item
            self.outer_index += 1
            self.inner_index = 0
        raise StopIteration



# Задание 2

import types

def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for item in sublist:
            yield item


# Задание 3
class FlatIterator:
    def __init__(self, list_of_lists):
        self.stack = [iter(list_of_lists)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            try:
                element = next(self.stack[-1])
                if isinstance(element, list):
                    self.stack.append(iter(element))
                else:
                    return element
            except StopIteration:
                self.stack.pop()
        raise StopIteration


# Задание 4
import types

def flat_generator(list_of_list):
    for element in list_of_list:
        if isinstance(element, list):
            yield from flat_generator(element)
        else:
            yield element
