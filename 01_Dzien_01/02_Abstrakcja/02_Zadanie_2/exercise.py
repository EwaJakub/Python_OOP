def middle_elements(sequences):
    new_el_list = []
    for seq in sequences:
        if len(seq) % 2 == 0 and len(seq) != 0:
            new_el_list.append(seq[int(len(seq)/2)])
        elif len(seq) % 2 != 0:
            new_el_list.append(seq[len(seq)//2])
        elif len(seq) == 0:
            pass
    return new_el_list


class SequenceOfNumbers:
    def __init__(self, start: int, stop: int, step: int):
        self.start = start
        self.stop = stop
        self.step = step
        self.sequence = list(range(start, stop, step))

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, index):
        if index >= len(self.sequence):
            raise IndexError('Always look beyond the horizon, but never beyond the end of sequence!')
        elif index < 0:
            raise IndexError('Negative indexes are not supported, sorry!')
        return self.sequence[index]


print(middle_elements([[6, 7, 8, 9, 10], ["Kto", "to", "taki?"], [], ["sześć", "siedem", "osiem", "dziewięć"],
                      SequenceOfNumbers(14, 46, 4)]))
