
# Lambda Function:-
                    # It's also called as Anonymous Function.
                    # That means a function without name.
                    # Lambda function,which takes 'n' number
                    # of inputs but only one expression.


# 1) Example:-

square=lambda num:num**2
print(square(10))

        # or #

square=lambda num:num**2
res=square(10)
print(res)

# 2) Example:-

#Map() function # map() function  passes each element in the iterable
                # (list,tuple,set,dict) through a function and returns 
                # the result of all elements having passed through the function.

li=[1,2,3,4,5]

res=map(lambda num:num**2,li)
print(list(res))

        # or #


print(list(map(lambda num:num**2,range(1,11))))


# Filter() function:- # The filter() function to return the boolean values 
                      # (true or false) and then passes each element in the
        # iterable through the function, "filtering" away those that are false.

li=[1,2,3,4,5,6,7,8,9]

res=filter(lambda num:num%2==0,li)
print(res)


        # or #

print(list(filter(lambda num:num%2==0,li)))

                # or #

print(list(filter(lambda num:num%2==0,range(1,11))))
        

# Return() Function:- # reduce() works differently than map() and filter().
                      # It does not return a new list based on the function and
                      # iterable we've passed. Instead, it returns a "single value".


li=[2,4,7,3]
print(reduce(lambda x,y:x+y,li))

        
