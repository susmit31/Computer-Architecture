class UniBitReg:
    def __init__(self,ini_val):
        self.content = ini_val

    def update(self, write, data):
        self.content = (write and data) or ((not write) and self.content)
        self.content = int(self.content)

    def read(self):
        return self.content


class MultiBitReg:
    def __init__(self, *bits):
        self.regs = []
        if len(bits) == 1:
            bits = list(str(bits[0]))
            bits = [int(b) for b in bits]
        for bit in bits[::-1]:
            self.regs.append(UniBitReg(int(bit)))
        self.nbits = len(bits)

    def read(self):
        for reg in self.regs[::-1]:
            print(reg.read(), end='')
        print()
    
    def update(self, position, write, data):
        self.regs[position].update(write,data)