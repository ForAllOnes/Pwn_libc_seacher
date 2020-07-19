# Pwn_libc_seacher
This is the tools for pwn ret2libc. just like LibcSearcher. It's my version.
This file is just written for fun.
When I was playing pwn using LibcSearcher, I just don't know how to use it. And there's sometimes when there exists two libc version need to be choosed but just one discovered by LibcSearcher. It's really depressed me and I don't know why.
So this script is using the websites https://publicki.top/libc/ to find the offsets.
With Requests & BeautifulSoup we could easily achieve the goal to find the offsets just like you do manually.

For more detials:

from parser import * \
ret = searcher('puts',0xa30) \
system_offset = ret['system']\
str_bin_sh_offset = ret['str_bin_sh']\
puts_addr = ret['puts']\

Tips
the return value of searcher is a dict like this { 'func_name':offsets }\
func_name is encoded by unicode(which is returned from the website)\
type(offsets) = int\
the dict just containes the functions showed on the webpages. 

enjoy !  (>_<)
