import random

def bubble_sort(in_list):
  for stage_num in range(len(in_list)):
    print(f"Stage {stage_num + 1}")
    for i in range(len(in_list) - 1):
      if in_list[i] > in_list[i + 1]:
        print(f"Moving index {i} to index {i+1}")
        in_list[i], in_list[i + 1] = in_list[i + 1], in_list[i]

sample_list = list(range(10))
sample_list = list(range(100, 110)) 
random.shuffle(sample_list)



print(sample_list)
bubble_sort(sample_list)