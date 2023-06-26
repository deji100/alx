#!/usr/bin/python3
"""Defines a base class"""
import json
import csv


class Base:
    """A base class"""

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A static method that receives a list of
        dictionaries and returns a str rep of it"""

        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of objects in a file"""

        if len(list_objs) == 0 or list_objs is None:
            with open(f"{cls.__name__}.json", 'w') as f:
                f.write(json.dumps([]))
        else:
            with open(f"{cls.__name__}.json", "w") as fl:
                new_list = []
                for x in list_objs:
                    new_list.append(x.to_dictionary())
                fl.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of objs from a json string"""

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an new instance of base subclass"""

        if cls.__name__ == "Rectangle":
            r1 = cls(12, 8, 2, 4, 5)
        else:
            r1 = cls(12, 8, 2, 4)

        r1.update(**dictionary)

        return r1

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        file = f"{cls.__name__}.json"
        new_list = []

        if not file:
            return []
        with open(file) as f:
            list_objs = cls.from_json_string(f.read())
            for x in list_objs:
                new_list.append(cls.create(**x))

        return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves list objs in a csv file"""

        if len(list_objs) == 0 or list_objs is None:
            with open(f"{cls.__name__}.csv", 'w') as f:
                f.write(json.dumps([]))
        else:
            with open(f"{cls.__name__}.csv", "w") as fl:
                if cls.__name__ == "Rectangle":
                    csv_writer = csv.DictWriter(fl,
                                                fieldnames=["width",
                                                            "height",
                                                            "x", "y",
                                                            "id"])
                else:
                    csv_writer = csv.DictWriter(fl,
                                                fieldnames=["size",
                                                            "x", "y",
                                                            "id"])

                for x in list_objs:
                    csv_writer.writerow(x.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns list of objs from csv file"""

        file = f"{cls.__name__}.csv"
        new_list = []

        with open(file) as f:
            if cls.__name__ == "Rectangle":
                list_dicts = csv.DictReader(f,
                                            fieldnames=["width",
                                                        "height",
                                                        "x", "y",
                                                        "id"])
                for x in list_dicts:
                    new_list.append(
                        cls.create(**{
                                    'id': int(x['id']),
                                    'width': int(x['width']),
                                    'height': int(x['height']),
                                    'x': int(x['x']),
                                    'y': int(x['y'])
                                     }))
            else:
                list_dicts = csv.DictReader(f,
                                            fieldnames=["size", "x",
                                                        "y", "id"])
                for x in list_dicts:
                    new_list.append(
                        cls.create(**{
                                    'id': int(x['id']),
                                    'size': int(x['size']),
                                    'x': int(x['x']),
                                    'y': int(x['y'])
                                     }))
        return new_list

    def draw(list_rectangles, list_squares):
        pass
