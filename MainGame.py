from DivisiónGame import div
from ModuloGame import mod
from MultiplicaciónGame import mul
from PotenciaGame import pot
from RestaGame import res
from SumaGame import add


def game():    
  score = 0    
  while True:        
      print('======== Menu ========'              
            '\n1. Add' 
            '\n2. Res'
            '\n3. Mul'
            '\n4. Div'
            '\n5. Pot'
            '\n6. Mod'
            '\n0. Exit')        
      option = int(input('\nChoice an option: '))         
      if option == 0:            
        break         
      num_1 = int(input('Enter first number: '))        
      num_2 = int(input('Enter second number: '))        
      answer = int(input('Enter you answer: '))         
      
      if option == 1:            
        result = add(num_1, num_2)            
        if result == answer:                
          score += 1                
          print('Correct!!')            
        else:                
          print('Incorrect')     
          print(f'======== Game Over ========'          
                f'\nYou score is {score}'          
                '\nKeep going!')  
      elif option == 2:            
          result = res(num_1, num_2)            
          if result == answer:                
            score += 1                
            print('Correct!!')            
          else:                
            print('Incorrect')     
            print(f'======== Game Over ========'          
                  f'\nYou score is {score}'          
                  '\nKeep going!')  
      elif option == 3:            
          result = mul(num_1, num_2)            
          if result == answer:                
            score += 2                
            print('Correct!!')            
          else:                
            print('Incorrect')     
            print(f'======== Game Over ========'          
                  f'\nYou score is {score}'          
                  '\nKeep going!')  
      elif option == 4:            
          result = div(num_1, num_2)            
          if result == answer:                
            score += 2                
            print('Correct!!')            
          else:                
            print('Incorrect')     
            print(f'======== Game Over ========'          
                  f'\nYou score is {score}'          
                  '\nKeep going!')  
      elif option == 5:            
          result = pot(num_1, num_2)            
          if result == answer:                
            score += 4                
            print('Correct!!')            
          else:                
            print('Incorrect')     
            print(f'======== Game Over ========'          
                  f'\nYou score is {score}'          
                  '\nKeep going!')  
      elif option == 6:            
          result = mod(num_1, num_2)            
          if result == answer:                
            score += 4                
            print('Correct!!')            
          else:                
            print('Incorrect')     
            print(f'======== Game Over ========'          
                  f'\nYou score is {score}'          
                  '\nKeep going!')  
game() 