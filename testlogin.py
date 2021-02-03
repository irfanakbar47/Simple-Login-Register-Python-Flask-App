from app import app
import unittest





class FlaskTest(unittest.TestCase):




	def test_index1(self):
                tester1 = app.test_client(self)
                response = tester1.get('/login', content_type='html/text')
                self.assertEqual(response.status_code, 200)

	#def test_login():
	#	response = make_response()
	##	login_user(session.query(User).get(1234))
	#	 return response


	#def test_valid_user_login(self):
	#	tester3 = app.test_client(self)
	#	response = tester3.post('/login', 'haan', 'haan')
    #self.assertEqual(response.status_code, 200)
    #self.assertIn(response.data)






#def test_index2(self):
	#	tester2 = app.test_client(self)
	#	response = tester2.get('/login', content_type='html/text')
	#	self.assertEqual(response.status_code, 200)









	#def test_index_data(self):
		#tester2 = app.test_client(self)
		#response = ('/login', data=dict(username=akbar, password=abc123), follow_redirects=True)
		#self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
	unittest.main()
