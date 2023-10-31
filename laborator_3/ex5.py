def ex5(rules, dict):
    counter = 0
    for key, prefix, middle, suffix in rules:
        # verificam daca cheia este in dictionar
        if key not in dict:
            return False
        value = dict[key]
        words = value.split()
        if words[0] == prefix or prefix == "":
            counter = counter + 1
            words.remove(words[0])
        if words[-1] == suffix or suffix == "":
            counter = counter + 1
            words.remove(words[-1])
        if middle in words:
            counter = counter + 1
        if counter == 3:
            return True
    return False


rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dictionary = {"key1": "come inside it's too cold out"}
print(ex5(rules, dictionary))