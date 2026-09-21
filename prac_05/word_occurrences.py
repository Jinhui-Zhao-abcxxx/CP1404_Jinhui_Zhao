"""
Word Occurrences
Estimate: 20 minutes
Start : 9:37
End:10:07
Actual:30 minutes
"""

from operator import itemgetter

words_to_times = {}
words_length = []


text = input("text:")
for word in text.split():
    if word not in words_to_times:
        times_used = 1
        words_to_times[word] = times_used
    else:
        words_to_times[word] += 1

for word in words_to_times:
    words_length.append(len(word))
max_length = max(words_length)



picks = sorted(words_to_times.items(), key=itemgetter(0))
for pick in picks:
    print(f"{pick[0]:{max_length}} : {pick[1]}")