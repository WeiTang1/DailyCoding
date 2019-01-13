# first thought:
#
# use a map of key -> linklist
#
# linklist will be ordered in time and keep the value of the key
#
# get/set will be O(n)
#
# second thougth to improve on performance:
#
# use self balance tree instead of linklist it will achieve O(logn) for set and get
#
# I think we can also use treemap to store to get O(1)