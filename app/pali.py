# Input : malayalam
# Output : Yes

# Input : geeks
# Output : No


s = "malayalam"
rs = s[::-1]
print(rs)

if s==rs:
	print("string is pali")
else:
	print("sorry")