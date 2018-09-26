import random

# open file as list
prompts_list = [line.rstrip('\n') for line in open('lists/writing_prompts')]

# randomly pick a writing prompt
random.shuffle(prompts_list)
choice = prompts_list[0]
print(choice)

# delete choice from prompts_list
updated_list = prompts_list[1:]

# remove choice from prompts_list
with open('lists/writing_prompts', mode='w') as outfile:
    for line in updated_list:
            outfile.write("%s\n" % line)

# put choice on used_prompts list
with open('lists/used_prompts', mode='a') as outfile:
    outfile.write("%s\n" % choice)


# print the amount of still available prompts
print(f'Available prompts: {len(updated_list)}')