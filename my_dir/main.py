import random

def bubble_sort(in_list):
  num_index = None
  for i in range(len(in_list) - 1):
    if in_list[i] > in_list[i + 1]:
      num_index = i
  print(f"The unsorted number is at index {num_index}")

sample_list = list(range(10))
sample_list.insert(random.randrange(10), 100)

print(sample_list)
bubble_sort(sample_list)