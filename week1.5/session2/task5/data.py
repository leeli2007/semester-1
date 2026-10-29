# Week 1.5, Session 2: Task 5

class Dataset:
    """
    A numeric dataset, loaded from a file.
    """

    def __init__(self, filename=None):
        """
        Creates a Dataset containing data from the specified file.

        If no file is specified, an empty Dataset is created.
        """
        self.data = []
        if filename:
            self.load_data(filename)

    def load_data(self, filename):
        """
        Loads data from the specified file into this Dataset.

        Any existing data will be deleted.
        """
        self.data = []
        with open(filename, 'r') as inFile:
            for line in inFile:
                value = float(line.strip())
                self.data.append(value)

    def __len__(self):
        """
        Returns the size of this Dataset.
        """
        return len(self.data)

    def __getitem__(self, index):
        """
        Returns the value at the specified position in this Dataset.
        """
        return self.data[index]
    
    def mean(self):
        """
        Returns the arithmetic mean of the values in this Dataset.
        """
        return sum(self.data) / len(self.data)

    def median(self):
        """
        Returns the median of the values in this Dataset.
        """
        sorted_data = sorted(self.data)
        length = len(sorted_data)
        mid = length // 2
        if length % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]