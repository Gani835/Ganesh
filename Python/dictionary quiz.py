
                        ### Quiz Game by using Dictionary ###

q1= ''' 1.Is python Interpreted Language?
        a) Yes   b)No '''

q2= ''' 2.Python was not an dynamically typed language.(True/False)
        a) True   b) False '''

q3= ''' 3.Which of the following is an identity operator?
        a) and    b) in    c) is    d)None of the above. '''

q4= ''' 4.Which of the following is an membership operator?
        a) or     b)&     c) not   d) None of the above '''

q5= ''' 5.Composite operators can also be called as. . . .
        a) Identity operator      b) Arithmatic operator
        c) Assignment operator    d) Bitwise operator '''

q6= ''' 6.Tuples can store heterogeneous values and which are mutable.(True/False)
        a) True     b) False '''

q7= ''' 7.Dictionary allows duplicate keys.(True/False)
        a) True     b) False '''

q8= ''' 8.Which method we use to delete a value/item/element/arguement from a set?
        a) del()    b) remove()     c) clear()    d) append() '''

q9= ''' 9.Is set supports indexing and slicing operations.(Yes/No)
        a) Yes      b) No '''

q10= ''' 10.If a={10,20,40,60} b={30,10,50,70} what is the set obtained by print(a.difference(b))?
        a) {30,50,70}   b) {20,40,60}  c) {10,30,50,70}  d) {10,20,40,60} '''


print("Welcome to the python quiz contest. . . .")
print("Answer the following questions.")
print("For every correct answer you got 1 mark and for every wrong answer you will get -0.5 mark. . .")

questionare={q1:"a",q2:"b",q3:"c",q4:"d",q5:"c",q6:"b",q7:"b",q8:"b",q9:"b",q10:"b"}
score=0
while True:
    for question in questionare:
        print(question)
        answer=input("Choose your option:")

        if answer==questionare[question]:
            print("Correct Answer")
            score=score+1
        else:
            print("Wrong Answer")
            score=score-0.5

    print("Your score is",score)
    ch=input("Do you want to play Quiz again?(yes/no)")
    if ch=="no":
        break
print("Quiz Over.Thank you for participating. . . .")
