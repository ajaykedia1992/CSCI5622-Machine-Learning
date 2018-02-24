import re

s = '[<span class="bp_sub_heading">10 episodes</span>]'

cleanr = re.compile('\[?<.*?>]?')
cleantext = re.sub(cleanr, '', s)



print(cleantext)