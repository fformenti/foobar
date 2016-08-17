def answer(digest):

	def make_hash(prev_msg):
		my_dict = {}
		for ii in range(256):
			code = ((129 * ii) ^ prev_msg) % 256
			my_dict[code] = ii
		return my_dict

	msg_dict = {}
	message = [0]*16
	for counter in enumerate(message):

		if counter > 0:
			prev_msg = message[counter - 1]
		else:
			prev_msg = 0
		
		if not prev_msg in msg_dict:
			msg_dict[prev_msg] = make_hash(prev_msg)

		decode = msg_dict[prev_msg]
		message[counter] = decode[digest[counter]]

	return message






