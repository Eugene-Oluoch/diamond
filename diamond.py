class Diamond:
    def engage_user(self):
        number = int(input("Enter an odd number: "))
        self.diamond(number)
        
    def diamond(self,number):
        if self.is_odd(number):
            loop_times = self.get_loop_time(number)
            spaces_to_add = loop_times
            diamond_to_add = 1
            array = []
            for _ in range(loop_times +1):
                to_append = self.generate_position_shape(spaces_to_add,diamond_to_add)
                spaces_to_add-=1
                diamond_to_add+=2
                if _ < loop_times:
                    array.append(to_append)
                print(to_append)
                if _ == loop_times:
                    self.print_last_portion(array)
        else:
            print("Give a valid odd number")
            self.engage_user()

    def generate_position_shape(self,spaces_to_add,diamond_to_add):
        spaces = " " * spaces_to_add
        diamond = "*" * diamond_to_add
        return spaces + diamond

    def print_last_portion(self,array):
        reversed_array = array[::-1]
        for num in reversed_array:
            print(num)
            
    def get_loop_time(self,number):
        return number // 2
            
    def is_odd(self,number):
        return number % 2 != 0        


    
dmd = Diamond()
dmd.engage_user()