"""
Hash Table Ransom Note

Jay Ravaliya
"""

def ransom_note(magazine, ransom):

	m_hash = {}

	for word in magazine:
		if word not in m_hash:
			m_hash[word] = 0
		m_hash[word] += 1

	for word in ransom:
		if m_hash.get(word) == None or m_hash[word] == 0:
			return False
		else:
			m_hash[word] -= 1

	return True
    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    

