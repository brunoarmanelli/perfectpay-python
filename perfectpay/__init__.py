import requests

class PerfectPay:
	def __init__(self, token):
		self.token = token
		
	def get_sales(self, transaction_token=None, sale_status=None, 
			start_date_sale=None, end_date_sale=None, start_date_approved=None, end_date_approved=None,  
			page=None):

		method_url = 'https://app.perfectpay.com.br/api/v1/sales/get'
		headers = {
			'Authorization': 'Bearer ' + self.token,
			'Content-Type': 'application/json',
			'User-Agent': 'WhoBotsRuntime/1.0'
		}
		payload = {}
		
		if transaction_token:
			payload['transaction_token'] = transaction_token
		if sale_status:
			payload['sale_status'] = sale_status
		if start_date_sale:
			payload['start_date_sale'] = start_date_sale
		if end_date_sale:
			payload['end_date_sale'] = end_date_sale
		if start_date_approved:
			payload['start_date_approved'] = start_date_approved
		if end_date_approved:
			payload['end_date_approved'] = end_date_approved
		if page:
			payload['page'] = page
		
		try:
			r = requests.post(url = method_url, headers = headers, params = payload)
			data = r.json()
			return data
		except: 
			return None

	def get_subscriptions(self, customer_email=None, subscription_status_enum=None, 
		recurrent_type_enum=None, page=None):

		method_url = 'https://app.perfectpay.com.br/api/v1/subscriptions/get'
		headers = {'Authorization': 'Bearer ' + self.token}
		payload = {}
		
		if customer_email:
			payload['customer_email'] = customer_email
		if subscription_status_enum:
			payload['subscription_status_enum'] = subscription_status_enum
		if recurrent_type_enum:
			payload['recurrent_type_enum'] = recurrent_type_enum
		if page:
			payload['page'] = page
		
		try:
			r = requests.post(url = method_url, headers = headers, params = payload)
			data = r.json()
			return data
		except: 
			return None