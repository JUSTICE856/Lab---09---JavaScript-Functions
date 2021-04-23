def factorial(n):

    total = 1
    for i in range(0, n, 1):
        total = total * (n - i)
        print("Current i is " + str(i))
        print("The current value of total is " + str(total))

    return total

}

var userstring = input("Number please");
var usernum = Int(userstring);

print(str(factorial(usernum))) 
