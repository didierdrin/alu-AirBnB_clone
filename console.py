from models.engine import storage 
import cmd  

class HBNBCommand(cmd.Cmd):   
    """Cmd interpreter class"""  
    prompt = '(hbnb)' 

    def do_create(self, args):
        """Createe a new instance of BaseModel/User, save it to file.json & prints the id"""
        if not args:    
            print("--- MISSING: Class name ---")
            return  
        try:    
            new_instance = eval(args)() 
            new_instance.save() 
            print(new_instance.id) 
        except NameError:  
            print("--- Class doesn't exist ---") 
    
    def do_show(self, args):
        """Display the string representation of an instance based on the name & the id"""
        args = args.split()  
        if len(args) < 1:    
            print("--- MISSING: Class name ---") 
            return  
        if len(args) < 2: 
            print("--- MISSING: Instance id") 
            return
        class_name, instance_id = args 
        if class_name not in storage.classes(): 
            print("--- Class doesn't exist ---") 
            return 
        key = f"{class_name}.{instance_id}"
        if key not in storage.all(): 
            print("--- No instance found ---")
            return
        print(storage.all()[key]) 

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = args.split()
        if len(args) < 1: 
            print("--- MISSING: Class name ---")
            return 
        if len(args) < 2: 
            print("--- MISSING: Instance id")
        class_name, instance_id = args  
        if  class_name not in storage.classes():
            print("--- Class doesn't exit ---")
            return  
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("--- No instance found ---") 
            return 
        del storage.all()[key]
        storage.save() 
    
    def do_all(self, args): 
        """Displays all string representation based on the id"""
        if args: 
            if args not in storage.classes():
                print("--- Class doesn't exit ---") 
                return
            print([str(objex) for objex in storage.all().values() if objex.__class__.__name__ == args ])
        else:
            print([str(objex) for objex in storage.all().values() ]) 

    def do_update(self, args):
        """Update an instance based on the class name & id by adding or updating attribute"""
        args = args.split() 
        if len(args) < 1:
            print("--- MISSING: Class name ---") 
            return 
        if len(args) < 2: 
            print("--- MISSING: Instance id") 
            return
        if len(args) < 3: 
            print("--- MISSING: Attribute name ---") 
            return 
        if len(args) < 4: 
            print("--- MISSING: Value") 
            return 
        class_name, instance_id, attr_name, attr_value = args 
        if class_name not in storage.classes():
            print("--- Class doesn't exist ---") 
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("--- No instance found ---")
        
        objx = storage.all()[key] 
        setattr(objx, attr_name, attr_value) 
        objx.save() 

    def do_quit(self, args):
        """Command to exit the program -> Quit"""
        return True 
    
    def do_help(self, args):
        """Prints the help message"""
        super().do_help(args) 

if __name__ == "__main__":
    HBNBCommand().cmdloop()
