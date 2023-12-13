def print_sorted_dictionary(a_dictionary):
    return dict(sorted(a_dictionary.items()))


a_dictionary = {'language': "C", 'Number': 89,
                'track': "Low level", 'ids': [1, 2, 3]}
print(print_sorted_dictionary(a_dictionary))
