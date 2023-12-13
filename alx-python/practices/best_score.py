def best_score(a_dictionary):
    max_score = 0
    max_key = None

    if a_dictionary == None or len(a_dictionary) == 0: 
        return max_key

    for k in a_dictionary:
        if a_dictionary[k] > max_score:
            max_score = a_dictionary[k]
            max_key = k

    return max_key



a_dictionary = {'John': 20, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))


