class Memory:
    def __init__(self, name):
        self.scope_name = name
        self.memory = {}

    def has_key(self, name):
        return name in self.memory

    def get(self, name):
        return self.memory.get(name)

    def put(self, name, value):
        self.memory[name] = value


class MemoryStack:
    def __init__(self, memory=None):
        if memory is None:
            memory = Memory('global')
        self.stack = [memory]

    def get(self, name):
        for mem in reversed(self.stack):
            if mem.has_key(name):
                return mem.get(name)
        return None

    def insert(self, name, value):
        self.stack[-1].put(name, value)

    def set(self, name, value):
        self.stack[-1].put(name, value)

    def push(self, memory_name: str):
        self.stack.append(Memory(memory_name))

    def pop(self):
        popped_memory = self.stack.pop()
        for key, value in popped_memory.memory.items():
            for mem in reversed(self.stack):
                if mem.has_key(key):
                    mem.put(key, value)
                    break
                