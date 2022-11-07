class Mug():
    def __init__(self, color,  name = 'Default', breakable = True):
        self.name = name
        self.color = color
        self.volume = ''
        self.breakable = breakable
        self.contents = ''
        self.content_volume = ''
        
    def drink(self):
        pass


    def pour_into(self):
        pass


    def smash(self):
        if self.breakable == True:
            print(f'There are now many {self.color} shards all over the floor')

        else: 
            print(f'The Mug called {self.name} is now on the floor')

        

    def print_name(self):
        print(self.name)


pearces_mug = Mug('White','THE MUG')
jareds_mug = Mug('Gray','Blender Bottle', breakable = False)

pearces_mug.print_name()
jareds_mug.print_name()

print("type", type(jareds_mug))
print("id", id(jareds_mug))


pearces_mug.smash()
jareds_mug.smash()


    
