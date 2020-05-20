from selenium import webdriver
import time
class Bot():
	def __init__(self):
		self.driver = webdriver.Chrome()
		#print(subGet('entj'))
	def subGet(self,x):
		self.driver.get('https://old.reddit.com/r/' + x)
		time.sleep(1)
		try:
			sub = self.driver.find_element_by_xpath('/html/body/div[3]/div[6]/div/span[2]/span[1]')
			return sub.text
		except:
			return 0
		
bot = Bot()
mbti = ['infp',
'infj',
'enfp',
'enfj',
'intp',
'intj',
'entj',
'estp',
'isfp',
'esfp',
'istp',
'estp',
'istj',
'estj',
'isfj',
'esfj']
subscribers = []
for x in mbti:
	subscribers.append(bot.subGet(x))
print(subscribers)
