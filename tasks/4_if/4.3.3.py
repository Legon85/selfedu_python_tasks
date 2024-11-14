string = input()
# msg = "палинтдром" if string == string[:] else "не палиндром"
# print(msg)
print(["не ", ""][string == string[:]] + "палиндром")
