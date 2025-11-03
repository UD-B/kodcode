# 1.
username = "alice"
def greet():
    return F"Hello, {username}!"
# print(greet())

# 2.
counts = {"a": 1, "b": 2, "c": 3}
for k in counts:
    if counts[k] % 2 == 1:
        pass
        # del counts[k]
# print(counts)

# 3.
text = "debugging"
# print(f"{text}!")

# 4.
nums = [1, 2, 3]
for i in range(0, len(nums)):
    # print(nums[i])
    pass

# 5.
config = {"host": "localhost", "port": 5432, "username": "UD"}
# print(config["username"])

# 6.
age = 12
# print(age + 5)

# 7.
user_input = "12.5"
# print(float(user_input))

# 8.
def ratio(a, b):
    return a - b
# print(ratio(10, 0))

# 9.
import json
# print(json.dumps({"ok": True}))

# 10.
def down(n):
    if n == 1:
        return 1
    # print(n)
    return down(n - 1)
# print(down(5))

# 11.
x = 5
while x > 0:
    x -= 1
    # print(x)

# 12.
