## CryptoAuthToken  
  
* `A way for authenticating using token with cryptographic encryption system.`  
  
<br>  
  
## Installation  
  
* Install Package Using `pip`  
  ```shell script  
   python3 pip install CryptoAuthToken  
   ```  
    
<br>  
  
### How to use:  

* `Note: ` After installing First time if you try to use or import this, it will print out `Initializing CryptoTokenAuth for the first time.We generate random cerdentials to keep this secure.` and exit.
this is the way it works it will only happen for the first time.it creates random cerdentials so you'r Token salt is totally random from others.

* Creating a Token  
    ```python  
    from CryptoAuthToken import CryptoToken  
    CryptoToken = CryptoToken(key='Mysecretkey')  
      
    token = CryptoToken.create()  
    print(token)  
      
    >>gAAAAABg0fTUjXv1D62TrwaQ==.....  
    ```  
  
* Validating Token.
`If the token was created with the same key then it's a valid token.Returns: Boolean`
    ```python  
    from CryptoAuthToken import CryptoToken  
    CryptoToken = CryptoToken(key='Mysecretkey')  
      
    token = 'gAAAAABg0fTUjXv1D62TrwaQ==...'
    is_valid = CryptoToken.authenticate(token=token)
    
    print(is_valid)
	
	>> True
    ```