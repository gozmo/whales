import pandas as pd
from collections import Counter

train = pd.read_csv("train.csv")

whale_ids = list(train["whaleID"])
counted_whale_ids = dict(Counter(whale_ids))
values = counted_whale_ids.values()

mean = sum(values) / float(len(values))

values.sort()
idx = len(values) / 2
median = values[idx]

print "mean: %s, median: %s" % (mean, median)
