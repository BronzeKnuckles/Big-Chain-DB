

class back:

	
	def docreate(d1,d2):
		from bigchaindb_driver import BigchainDB
		from bigchaindb_driver.crypto import generate_keypair
		
		print(d1,d2)
		bdb = BigchainDB('https://test.ipdb.io/')
		
		alice = generate_keypair()

		tx = bdb.transactions.prepare(
		operation = 'CREATE',
		signers = alice.public_key,
		asset = {'data':{
			'car':{
			'vehicle_number':d1,
			'manufacturer':d2,
			},
		},})

		signed_tx = bdb.transactions.fulfill(tx,private_keys= alice.private_key)
		bdb.transactions.send_commit(signed_tx)

		return signed_tx

	def checker(id):
		from bigchaindb_driver import BigchainDB
		bdb = BigchainDB('https://test.ipdb.io/')

		block_height = bdb.blocks.get(txid = id)
		if bdb.blocks.retrieve(str(block_height)):
			return "sucess"
		else:
			return "failed or inqueue"
		
	

	def asset_transfer():
		pass




	

