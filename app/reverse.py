# using recursion # function call itself
def reverse(s): 
    if len(s) == 0: 
        return s 
    else:
    	# p = s[1:]
    	# print(p)
    	print(s[0])
    	return reverse(s[1:]) + s[0]
    	       # reverse('khil') + 'a'
    	       # reverse('hil') + 'k' + 'a'
    	       # reverse('il') + 'h'+ 'k' + 'a'
    	       # reverse('l') + 'i'+ 'h'+ 'k' + 'a'
    	       # reverse('') + 'l'+'i'+ 'h'+ 'k' + 'a'
    	       # 'lihka'

# # using extended slice syntax 
# def reverse(string): 
#     string = string[::-1] 
#     return string

# # using reversed()
# def reverse(string): 
#     string = "".join(reversed(string)) 
#     return string 


reverse("akhil")
