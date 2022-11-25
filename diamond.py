from welcome import welcome

class Diamond:
    
    def __init__(self):
        self.top_shapes = []
        self.welcome = welcome()
        
    
    def engage_user(self):
        number = int(input("Enter an odd number: "))
        if not self.is_odd(number):
            print("Give a valid odd number")
            self.engage_user()
        else:
            self.diamond(number)
        
    def diamond(self,number):
        loop_times = self.get_loop_time(number)
        spaces_to_add = loop_times
        diamond_to_add = 1

        for time in range(loop_times +1):
            to_append = self.generate_position_shape(spaces_to_add,diamond_to_add)
            spaces_to_add-=1
            diamond_to_add+=2
            self.loop_time_operations(time,loop_times,to_append)
        self.try_again()
            

    def loop_time_operations(self,time, loop_times, to_append):
            if time < loop_times:
                self.top_shapes.append(to_append)
            print(to_append)
            if time == loop_times:
                self.print_last_portion()
                
    def generate_position_shape(self,spaces_to_add,diamond_to_add):
        spaces = " " * spaces_to_add
        diamond = "*" * diamond_to_add
        return spaces + diamond

    def print_last_portion(self):
        reversed_array = self.top_shapes[::-1]
        for num in reversed_array:
            print(num)
        self.top_shapes = []
            
    def get_loop_time(self,number):
        return number // 2
            
    def is_odd(self,number):
        return number % 2 != 0        

    def try_again(self):
        ask = input("Do you want to give it another shot?[y/n] ").lower()
        if ask == 'y':
            self.engage_user()
        elif ask == 'n':
            print("Bye")
        else:
            self.try_again()
    
if __name__ == "__main__":
    dmd = Diamond()
    dmd.engage_user()