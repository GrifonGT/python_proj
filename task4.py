def func(x):
    return 1 / x


for i in range(-10, 10):
    x = i / 10
    try:
        print(f"{x} : {func(x)}")
    except ZeroDivisionError:
        print(f"{x} : NaN")

print("------------------------------------")

file = open("sample", "r")
source = file.read().split(" ")
print("Numbers:")

for num in source:
    try:
        print(f"{int(num)}")
    except ValueError:
        print(f"{num} isn't number")


print("--------------------------------------")

files = ["sample1", "sample2", "sample3", "sample4", "sample5"]

for file_name in files:
    try:
        file = open(f"sample_files/{file_name}", "r")
        source = file.read()
        print(f"file {file_name} source: {source}")
    except FileNotFoundError:
        print(f"file {file_name} not found")