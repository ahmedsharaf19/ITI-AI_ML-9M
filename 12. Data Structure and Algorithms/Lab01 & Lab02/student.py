class Student:
    def __init__(self, id: int, name: str, grades: list[float]):
        self.id = id
        self.name = name
        self.set_grades(grades)

    def get_id(self) -> int:
        """
        get_id function to return the student's ID

        Returns:
            int: The ID of the student
        """
        return self.id
    
    def get_name(self) -> str:
        """
        get_name function to return the student's name

        Returns:
            str: The name of the student
        """
        return self.name

    def get_grades(self) -> list[float]:
        """
        get_grades function to return the student's grades

        Returns:   
            list[float]: The grades of the student
        """
        return self.grades
    
    def get_average(self) -> float:
        """
        get_average function to return the average of the student's grades

        Returns:
            float: The average of the student's grades
        """
        return sum(self.grades) / len(self.grades)

    def set_id(self, id : int) -> None:
        """
        set_id function to set the student's ID

        Args:
            id (int): The new ID of the student
        """
        self.id = id

    def set_name(self, name: str) -> None:
        """
        set_name function to set the student's name

        Args:
            name (str): The new name of the student
        """
        self.name = name

    def set_grades(self, grades: list[float]) -> None:
        """
        set_grades function to set the student's grades

        Args:
            grades (list[float]): The new grades of the student
        Raises:
            ValueError: If the grades list does not contain exactly 5 values
        """
        if len(grades) != 5:
            raise ValueError("Grades must contain exactly 5 values")
        for g in grades:
            if not isinstance(g, (float, int)):
                raise ValueError("Grade Must be numeric Value")
        self.grades = grades