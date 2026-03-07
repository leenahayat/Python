print("Welcome to kon Banega crorepati season one , total reward is 10,000 and 1000 will be added for each correct answers ")
question = ["Who is the best programmer :- a Harry   b Striver   c Love Babbar  d All"
            ,"What does SQL stand for ? :- a) Super Quick Language b) Software Query Logic c) Structured Query Logic d) Structured Query Language" 
            , "What does the Boolean datatype represent? :- a) Numbers b) True/False c) Decimal d) Fraction"
            ,"Which of these is not a core data type? :- a) Class b) Lists c) Dictionary d) Tuples"
            ,"What data type is the object below ? L = [1, 23, 1] :- a) List b) Dictionary c) Tuple d) Array"
            ]

ans = ["d","d","b","a","a"]
reward = 0
i = 0
j = 0

while i != 5:
    print(question[i])
    x = input("enter your answer as a or b or c or d :- ")
    if ans[j] == x:
        print("correct answer")
        reward += 1000
        
    else:
        print("INCORRECT ANSWER YOU REWARD IS- ",reward)
        break
    i += 1 
    j +=1

if(reward==5000):
    print("AP JEET GAYE 7 CRORE , JUST KIDDING YOUR REWARD IS 5,000")