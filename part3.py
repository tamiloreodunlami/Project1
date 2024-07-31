class NamespaceManager:
    def __init__(self):
        self.namespace = {}

    def set_variable(self, name, value):
        self.namespace[name] = value

    def get_variable(self, name):
        return self.namespace.get(name)

    def delete_variable(self, name):
        if name not in self.namespace:
            raise KeyError(f"Variable '{name}' does not exist.")
        del self.namespace[name]

    def list_variables(self):
        return list(self.namespace.keys())

    def execute_function(self, code):
        exec(code, {}, self.namespace)
        result = self.namespace['result']
        del self.namespace['result']
        return result


def main():

    manager = NamespaceManager()
    manager.set_variable('a', 30)
    manager.set_variable('b', 40)

    print(manager.get_variable('a'))
    print(manager.get_variable('b'))
    print(manager.list_variables())

    print( manager.execute_function('result = a + b'))

if __name__ == "__main__":
    main()

