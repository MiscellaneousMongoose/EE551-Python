"""
Python Functions and Recursions
"""
"""
QUESTION 1: 
========================================================================================================
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
["((()))","(()())","(())()","()(())","()()()"]
Write a function named generateParenthesis that takes an integer as an input and returns a list of strings 
as an output. Note that you can define a function inside a function if necessary.
"""
def generateParenthesis(n):
    def Newstrng(lst, index_len):
        index_len = len(lst)
        newlst = []
        newlst += ["("+lst[x]+")" for x in range(index_len)]
        newlst+=[lst[x]+"()" for x in range(index_len) if not lst[x]+"()" in newlst]    
        newlst+=["()"+lst[x] for x in range(index_len) if not "()" + lst[x] in newlst]
        if index_len == 2:
            newlst = newlst[:3]+[newlst[4]]+[newlst[3]]
            
        return newlst
    #***This one was hard because of the required pattern order of the list was difficult to produce***    
    if n == 0:
        return [""]
    if n == 1:
        l=["()"]
        return l
    else:
        
        return Newstrng(generateParenthesis(n-1), n)
    


"""
QUESTION 2: 
========================================================================================================
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
Example 1:
========================================
Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:
=========================================
Input: "race a car"
Output: false
Write a function named isPalindrome that takes a string as an input and returns a bool as an output.
"""
def isPalindrome(strng):
    strng = strng.lower()
    def all_letter(strng):
        new_strng = ""
        alphebet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        for x in range(len(strng)):
            if strng[x] in alphebet:
                new_strng = new_strng + strng[x]
        return new_strng
    if not strng.isalnum():
        strng = all_letter(strng)
    if len(strng) <= 1:
        return True
    if len(strng) == 2:
        if strng[0] is strng[1]:
            return True
        else:
            return False
    if strng[0] is not strng[len(strng)-1]:
        return False
    return isPalindrome(strng[1:(len(strng)-1)])
