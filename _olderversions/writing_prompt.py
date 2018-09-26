import pandas as pd
import random

# open list with writing prompts and transforming them to type=list
writing_prompts = pd.read_csv('lists/writing_prompts.csv', sep=",", header=None)
writing_prompts = writing_prompts.drop([0])
writing_prompts = writing_prompts.drop([0], axis=1)
lists = writing_prompts.values
np_list = lists.flatten()
prompts_list = np_list.tolist()
print(writing_prompts)

# open list of used prompts and transforming them to type=list
used_prompts = pd.read_csv('lists/used_prompts.csv', sep=",", header=None)
used_prompts = used_prompts.drop([0])
used_prompts = used_prompts.drop([0], axis=1)
used_lists = used_prompts.values
np_used_list = used_lists.flatten()
used_list = np_used_list.tolist()

# randomly picking a writing prompt
random.shuffle(prompts_list)
choice = prompts_list[0]

# remove picked prompt from list of writing prompts
updated_list = prompts_list[1:]
pd.DataFrame(updated_list).to_csv('lists/writing_prompts.csv')

# add chosen writing prompt to used prompt list
used_list.append(choice)
pd.DataFrame(used_list).to_csv('lists/used_prompts.csv')

print(choice)
print(f'Available prompts: {len(writing_prompts) + 1}')
print(f'Used prompts: {len(used_prompts) + 1}')