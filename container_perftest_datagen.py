import array
import random

Max_exponent=7 
Haystack_len=10**Max_exponent
Needles_len=10**(Max_exponent-1)
Sample_len=Haystack_len +Needles_len//2 
needles=array.array('d')
sample={1/random.random()for i in range(Sample_len)}
print(f'initial sample: elements {len(sample)}')
#complete sample,in case duplicate random numbers were discarded
while len(sample)< Sample_len:
    sample.add(1/random.random())
print(f'complete sample: elements {len(sample)}')
sample=array.array('d',sample)
random.shuffle(sample)
not_selected=sample[:Needles_len //2]
print(f'not selected: samples {len(not_selected)}')
print(' writing not_seclected.arr')
with open('not selected.arr','wb')as f:
    not_selected.tofile(f)
selected=sample[Sample_len //2:]
print(f'selected: samples {len(selected)}')
print(' writing selected.arr ')
with open('selected.arr','wb')as f:
    selected.tofile(f)

