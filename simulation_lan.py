
class Router:
	def __init__(self):
		self.server_lst = {}
		self.ip_occupy = []
	
	def link(self, server):
		i = 1
		while not server.ip:
			if i not in self.ip_occupy:
				server.ip = i
				self.ip_occupy.append(i)
			i += 1
		
		self.server_lst[id(server)] = server
	
	def unlink(self, server):
		self.server_lst.pop(id(server))


class Server:
	def __init__(self):
		self.ip = 0


r = Router()
s1 = Server()
s2 = Server()
r.link(s1)
r.link(s2)
print(s1.ip)
print(s2.ip)