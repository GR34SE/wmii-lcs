# coding=utf-8

# runtime and memory complexity is O(first_string * second_string)
def get_longest_common_subsequence(first_string, second_string):
    longest_common_subsequence_length = 0

    first_string_length = len(first_string)
    second_string_length = len(second_string)

    if first_string_length == 0 or second_string_length == 0:
        return 0, ""

    results_matrix = [[0] * (second_string_length + 1) for i in range(first_string_length + 1)]
    last_found_index_in_first_string = 0

    # iterating over every letter from first_string
    for i in range(1, first_string_length + 1):
        # iterating over every letter of second_string
        for j in range(1, second_string_length + 1):

            # checking if both letters are the same, if so then updating the results_matrix entry
            if first_string[i - 1] == second_string[j - 1]:
                results_matrix[i][j] = results_matrix[i - 1][j - 1] + 1

            # check if "better" result has been found, if so then update new longest subsequence and ending index
            if results_matrix[i][j] > longest_common_subsequence_length:
                longest_common_subsequence_length = results_matrix[i][j]
                last_found_index_in_first_string = i

    # (length, longest_subsequence)
    return longest_common_subsequence_length, first_string[last_found_index_in_first_string - longest_common_subsequence_length: last_found_index_in_first_string]


if __name__ == '__main__':
    # empty cases
    print get_longest_common_subsequence("", "abc")  # - (0)
    print get_longest_common_subsequence("abc", "")  # - (0)
    print get_longest_common_subsequence("abcdefghijk", "3453453453")  # - (0)

    # optimistic cases
    print get_longest_common_subsequence("abcdefghijkplmnjki", "def_hijk")  # def (3)
    print get_longest_common_subsequence("___12345___", "345")  # 345 (3)
    print get_longest_common_subsequence("ab1122", "xxx_ab1_xxx")  # ab1 (3)
