call = 0
def count_calls():
    global call
    call = call + 1
    return call


def string_info(string_):
    a = (len(string_), string_.upper(), string_.lower())
    count_calls()
    return(a)

def is_contains(string, list_to_search):
    string = string.lower()
    list_to_search_lower = [s.lower() for s in list_to_search]
    count_calls()
    if string in list_to_search_lower:
        return True
    else:
        return False

string_ = 'Abba'
string_2 = 'Bob'
a = 'Urban'
b = ['ban', 'BaNaN', 'urBAN']
c = 'cycle'
d = ['recycling', 'cyclic']
print(string_info(string_))
print(string_info(string_2))
print(is_contains(a, b))
print(is_contains(c, d))
print(call)