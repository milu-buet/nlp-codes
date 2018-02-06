# Natural Language Processing, Spring'18
# Assignment #1
# Md Lutfar Rahman
# mrahman9@memphis.edu


def word_splitter(text):
	separators = [',','.','-','"','\n']
	for sep in separators:
		text = text.replace(sep,'')
	words = text.split(' ')
	words.remove('')
	return words

def word_count(text):
	words_count_dict = {}
	words = word_splitter(text)

	for word in words:
		if word in words_count_dict:
			words_count_dict[word]+=1
		else:
			words_count_dict[word]=1

	return words_count_dict

def get_topten(words_count_dict):
	return sorted(words_count_dict, key=words_count_dict.__getitem__, reverse=True)[0:10]


def show_result(topten, words_count_dict):
	print("word frequency")
	for word in topten:
		print(word,words_count_dict[word])


if __name__ == "__main__":
	sample_text = '''
	Whales are marine mammals of order Cetacea which are neither dolphins 
	- members, in other words, of the families delphinidae or
	platanistoidae - nor porpoises. They include the blue whale, the
	largest animal ever to have lived. Orcas, colloquially referred to as
	"killer whales", and pilot whales have whale in their name but for the
	purpose of classification they are actually dolphins. For centuries,
	whales have been hunted for meat and as a source of valuable raw
	materials. By the middle of the 20th century, large-scale industrial
	whaling had left many populations severely depleted, rendering certain
	species seriously endangered.
	'''
	words_count_dict = word_count(sample_text)
	topten = get_topten(words_count_dict)
	show_result(topten, words_count_dict)

