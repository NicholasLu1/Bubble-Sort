import random

def bubble_sort(in_list):
  for stage_num in range(len(in_list) - 1):
    print(f"Stage {stage_num + 1}")
    found_unsorted = False
    for i in range(len(in_list) - 1 - stage_num):
      if in_list[i] > in_list[i + 1]:
        found_unsorted = True
        print(f"Moving index {i} to index {i+1}")
        in_list[i], in_list[i + 1] = in_list[i + 1], in_list[i]
    if not found_unsorted:
      break

sample_list = list(range(10))
sample_list = list(range(100, 110)) 
random.shuffle(sample_list)



print(sample_list)
bubble_sort(sample_list)
print("Sorted: ", sample_list)
