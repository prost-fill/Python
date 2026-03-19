class BaseMoney():
    def __init__(self,wholes,cents):
        
        self.wholes = int(wholes)
        self.cents = int(cents) 
 
    def __str__(self):
        return f'{self.wholes}.{self.cents}' 
 
    def __add__(self, other):
        new_wholes = self.wholes + other.wholes
        new_cents = self.cents + other.cents  
        
        if other.cents+self.cents >=100:
            
            new_cents = (other.cents+self.cents)%100
            new_wholes = new_wholes + (other.cents+self.cents)//100
        
        
        
        return BaseMoney(new_wholes, new_cents)
    
    def __sub__(self,other):
        
        new_wholes = self.wholes - other.wholes
        new_cents = self.cents - other.cents  
        if new_cents<0:
            new_cents = abs(self.cents - other.cents)
        return BaseMoney(new_wholes, new_cents)
    
  
    def __mul__(self, other):
        a = int(self.wholes) + (int(self.cents)%100)/100
        b = int(other.wholes) + (int(other.cents)%100)/100   
        c = a * b
        new_wholes = int(c)
        new_cents = (c-int(c))*100
        return BaseMoney(new_wholes, new_cents)      
    
    def __truediv__(self, other):
        a = int(self.wholes) + (int(self.cents)%100)/100
        b = int(other.wholes) + (int(other.cents)%100)/100  
        c = a/b
        new_wholes = int(c)
        new_cents = (c-int(c))*100
        return BaseMoney(new_wholes, new_cents)                 
        
    def __lt__(self, other):
        
        a = int(self.wholes) + (int(self.cents)%100)/100
        b = int(other.wholes) + (int(other.cents)%100)/100 
        
        if a<b:
            return bool(1)
        else:
            return bool(0)
    def __le__(self, other):
        a = int(self.wholes) + (int(self.cents)%100)/100
        b = int(other.wholes) + (int(other.cents)%100)/100 
        
        if a<=b:
            return bool(1)
        else:
            return bool(0)        
        
    def __eq__(self, other):
        a = int(self.wholes) + (int(self.cents)%100)/100
        b = int(other.wholes) + (int(other.cents)%100)/100 
        
        if a == b:
            return bool(1)
        else:
            return bool(0)  
        
    def __ne__(self, other):
        a = int(self.wholes) + (int(self.cents)%100)/100
        b = int(other.wholes) + (int(other.cents)%100)/100 
        
        if a != b:
            return bool(1)
        else:
            return bool(0)          
        
    def __gt__(self, other):
        a = int(self.wholes) + (int(self.cents)%100)/100
        b = int(other.wholes) + (int(other.cents)%100)/100 
        
        if a > b:
            return bool(1)
        else:
            return bool(0)         
        
        def __ge__(self, other):
            a = int(self.wholes) + (int(self.cents)%100)/100
            b = int(other.wholes) + (int(other.cents)%100)/100 
            
            if a >= b:
                return bool(1)
            else:
                return bool(0)              
        
 
bm_1 = BaseMoney(4,4)  
print(bm_1) 
bm_2 = BaseMoney(2,30)  
print(bm_2)
bm_3 = bm_2 + bm_1
print(bm_3)
bm_4 = bm_1 - bm_2
print(bm_4)
bm_5 = bm_1 * bm_2
print(bm_5)
bm_6 = bm_1 / bm_2
print(bm_6)
print (bm_1 != bm_2)