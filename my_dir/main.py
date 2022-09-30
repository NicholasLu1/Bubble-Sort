import random

def bubble_sort(in_list):
  for stage in ["Stage 1", "Stage 2", "Stage 3"]:
    print(stage)
    for i in range(len(in_list) - 1):
      if in_list[i] > in_list[i + 1]:
        print(f"The list is {in_list}")
        print(f"Moving {in_list[i]}") 
        in_list[i], in_list[i + 1] = in_list[i + 1], in_list[i]

sample_list = list(range(10))
sample_list.insert(random.randrange(10), 100)
sample_list.insert(random.randrange(10), 101)
sample_list.insert(random.randrange(10), 102)


print(sample_list)
bubble_sort(sample_list)