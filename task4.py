import collections

text = 'cool cola, is really cool drink'

words = text.split()
counter = collections.Counter(words)
most_common, occurrences = counter.most_common() [0]

longest = max(words, key=len)

print(most_common, longest)