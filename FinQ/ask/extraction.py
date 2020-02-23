from rake_nltk import Rake


def key_extract(mytext):
	r = Rake()
	# mytext = '''Electronic commerce, commonly written as e-commerce, is the trading in products or services using computer networks, such as the Internet. Electronic commerce draws on technologies such as mobile commerce, electronic funds transfer, supply chain management, Internet marketing, onlinetransactionprocessing, electronicdatainterchange (EDI), inv entory management systems, and automated data collection systems. Modern electronic commerce typically uses the World Wide Web for at least one part of the transaction's life cycle, although it may also use other technologies such as e-mail'''
	r.extract_keywords_from_text(mytext)
	return r.get_ranked_phrases()