def first_fit(item_size, bin_size):

    # initialise a list of bins
    bin_list = [0]

    # take our ith item
    for item in item_list:
        if item_list[0] <= bin_size - bin_list[0]:
            bin_list[0] += item_list[0]

        elif 

        else:
            bin_list.append(item)

        return bin_list
# Data we have:

# size of each item
item_list = [2, 1, 3, 2, 1, 2, 3, 1]

# size of bin
bin_size = 4

# Output:
# some list of bins with what each bin contains
# Solution to the question "how many bins are needed"
# can be obtained from len(bin_list)

print(first_fit(item_list, bin_size) == [4, 4, 4, 3])



