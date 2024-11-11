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
        result1 = string_info("Привет Urban")

        # def is_contains (string,list):
        #     count_calls ()
        #     d = string.lower ()
        #     return d in (item.lower () for item in list)
        result1 = string_info ("Привет Urban")
        #     result2 = is_contains ("Mir", ["Привет","urban", "Знание"])
        # print (result1)
        # print (result2)
    print (calls)

