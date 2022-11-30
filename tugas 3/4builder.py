class Product(object):
  def __init__(self, server):
    self.server = server
  
  def connect(self):
    print(f"Connecting to{self.server}")
    
class ServerA(object):
  def connect_to(self):
    return Product(" Server A")
    
class ServerB(object):
  def connect_to(self):
    return Product(" Server B")
    
class Director(object):
  def set_builder(self, builder):
    self.builder = builder
    
  def get_server(self):
    return self.builder.connect_to(self)
    
    
def main():
  director = Director()
  director.set_builder(ServerB)
  product = director.get_server()
  product.connect()

if __name__ == "__main__":
  main()