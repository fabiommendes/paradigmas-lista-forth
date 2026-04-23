def init(data: list[int]) -> str:
    return "\n".join(f"{elem} push" for elem in data)


def test_test_get(io):
    assert io("exercicios-array.fs", [init([1, 2, 3]), "0 get 1 get 2 get .s"]).stack == [1, 2, 3]
    assert io("exercicios-array.fs", [init([1, 2, 3, 4]), "3 get ."]).output == "4"


def test_set(io):
    assert io("exercicios-array.fs", [init([1, 2, 3]), "42 0 set 0 get ."]).output == "42"
    assert io("exercicios-array.fs", [init([1, 2, 3]), "42 1 set 0 get . 1 get ."]).output == "1 42"


def test_print(io):
    assert io("exercicios-array.fs", [init([1, 2, 3]), "print-array"]).output == "1 2 3"
    assert io("exercicios-array.fs", [init([4, 3, 2, 1]), "print-array"]).output == "4 3 2 1"


def test_array_sum(io):
    assert io("exercicios-array.fs", [init([1, 2, 3, 4]), "array-sum .s"]).stack == [10]
    assert io("exercicios-array.fs", [init([0, 1, 2, 3, 4, 5]), "array-sum .s"]).stack == [15]


def test_array_max(io):
    assert io("exercicios-array.fs", [init([1, 2, 3, 4]), "array-max .s"]).stack == [4]
    assert io("exercicios-array.fs", [init([0, 10, 2, 3, 4, 5]), "array-max .s"]).stack == [10]


def test_array_min(io):
    assert io("exercicios-array.fs", [init([1, 2, -3, 4]), "array-min .s"]).stack == [-3]
    assert io("exercicios-array.fs", [init([0, 10, -2, 3, 4, 5]), "array-min .s"]).stack == [-2]

def test_array_average(io):
    assert float(io("exercicios-array.fs", [init([1, 2, 3]), "array-average F."]).output) == 2.0
    assert float(io("exercicios-array.fs", [init([0, 1, 2, 3, 4]), "array-average F."]).output) == 2.0
    assert float(io("exercicios-array.fs", [init([4, 5]), "array-average F."]).output) == 4.5
    
# def test_read_array(io):
#     assert io("exercicios-array.fs",
#                ["read-array print-array"],
#                stdin="1 2 3 0\n").output.replace(">", "").split() == ["1", "2", "3"]
#    
#     assert io("exercicios-array.fs",
#                ["read-array print-array"],
#                stdin="-1 10 42 1 0\n").output.replace(">", "").split() == ["-1", "10", "42", "1"]