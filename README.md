
# Unoffical Perfect Pay Python Module

Perfect Pay requests made easy.

### Usage
  
````python
import perfectpay

perfectpay = perfectpay.PerfectPay(token='YOUR-TOKEN-HERE')
````

and then

````python
response = perfectpay.get_sales()
print(response)
````
