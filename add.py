class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        return
    def __init__(self):   #factorial calculation
        factor=1
        c=True
        while c:
            d=int(input("enter no:"))
            if d<10:
                c=False #default:execute once  
            else:    
                print("try less than 10")
                c=True  #restart loop logic
            for i in range(1,d+1):
                  factor=factor*i
        print(factor)
   
    
        
        

obj=calculator()        