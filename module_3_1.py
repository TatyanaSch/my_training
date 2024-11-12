calls = 0
def count_calls ():
    global calls
    calls += 1
def string_info (string):
    count_calls ()
    a = len (string)
    b = string.upper ()
    c = string.lower ()
    return a,b,c

def is_contains (string,list_1):
    count_calls ()
    d = string.lower ()
    return d in (item.lower () for item in list_1)


result1 = string_info("Привет пРЕПОДАватель")
result2 = string_info("До свидания УЧЕник")
result3 = is_contains ("знания", ["Привет","urban", "Знания"])
result4 = is_contains ("Вид", ["Привет","urban", "Знание"])

print (result1)
print (result2)
print (result3)
print (result4)
print (calls)
