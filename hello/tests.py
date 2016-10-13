from django.test import Client, TestCase

# Create your tests here.


class HelloWorldTest(TestCase):
    
    def test_reachable(self):
        
        # arrange
        client = Client()
        
        # act
        response = client.get('/hello_world')
        
        # assert
        self.assertEqual(200, response.status_code)
        
    def test_hello_world(self):
        
        # arrange
        client = Client()
        
        # act
        response = client.get('/hello_world')
        
        # assert
        self.assertIn('Hello world !', response.content)
