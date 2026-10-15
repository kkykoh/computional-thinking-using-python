
def my_own_function(*args, **kwargs):
    print("Hello!")
    print("I see that you have entered the following", args, kwargs)
    return 123


class Paper:
    def __init__(self):
        self.contents = "" # start with empty str

    def write(self, entry: str):
        self.contents += entry  # concat entry to the contents str

    def __str__(self):
        return self.contents    # return the string