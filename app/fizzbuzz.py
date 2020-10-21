#Python program to print Fizz Buzz 
#loop for 100 times i.e. range 
for i in range(20):  
  
    # number divisible by 3, print 'Fizz'  
    # in place of the number 
    if i % 15 == 0:  
        print("FizzBuzz")                                          
        continue
  
    # number divisible by 5, print 'Buzz' 
    # in place of the number 
    elif i % 3 == 0:      
        print("Fizz")                                          
        continue
  
    # number divisible by 15 (divisible  
    # by both 3 & 5), print 'FizzBuzz' in 
    # place of the number 
    elif i % 5 == 0:          
        print("Buzz")                                      
        continue
  
    # print numbers 
    print(i) 
