from InputsConfig import InputsConfig as p
from Cserver import Cserver as CS
from LightTransaction import Transaction

def main(): 
	# connect to the nodes
	CS.connect()
	CS.send_nodes_info()
	
	for i in range (p.Runs):
		if p.hasTrans:
			if p.Ttechnique == "Light":
				LightTransaction.create_transactions() # generate pending transactions
			elif p.Ttechnique == "Full":
				Transaction.create_transactions_full() # generate pending transactions
		CS.send_txnpool_gblock()
		CS.consensus()
	

######################################################## Run Main method #####################################################################
if __name__ == '__main__':
	main()
