#!/usr/bin/python3
"""
A storage module that handles all aspects of adding and removing content"""

class FileStorage:
    """A class that is responsible forstoring data.

    Atts:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary of instantiated objects in __objects.

        If a cls is specified, returns a dictionary of objects of that type
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            class_dict = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    cls_dict[key] = vvalue
            return class_dict
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id."""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_dict = {objt: self.__objects[objt].to_dict() for objt in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for objt in json.load(f).values():
                    name = objt["__class__"]
                    del objt["__class__"]
                    self.new(eval(name)(**objt))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete a given object from __objects, if it exists."""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """Call the reload method."""
        self.reload()
