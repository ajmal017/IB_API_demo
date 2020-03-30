from ibapi.client import EClient
from ibapi.common import TickerId
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract, ContractDetails


class DemoApp(EWrapper, EClient):
	def __init__(self):
		EClient.__init__(self, self)
	
	def error(self, reqId, errorCode, errorString):
		print("Error ", reqId, " ", errorCode, " ", errorString)
	
	def contractDetails(self, reqId, contractDetails):
		print("contractDetails: ", reqId, " ", contractDetails)


def main():
	app = DemoApp()
	
	app.connect("127.0.0.1", 7496, 0)
	
	contract = Contract()
	contract.symbol = "AAPL"
	contract.secType = "STK"
	contract.exchange = "SMART"
	contract.currency = "USD"
	contract.primaryExchange = "NASDAQ"
	
	app.reqContractDetails(1, contract)
	
	app.run()


if __name__ == '__main__':
	main()