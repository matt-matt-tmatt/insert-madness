import random
import datetime

class InsertMadness(object):
    """
    Insert madness is a random SQL insert querty generator
    """
    
    def __init__(self, inputDic, input="d", path=""):
        """
        It receives a dictinary with a key named "tableName" and the value is a string with 
        the table to appear in the query.
        The dictionary must have at least one more key. The name of the key will be the name
        of the column and the value a list of the posibles values to appear in the query

        """
        #TODO: input ="f" let you import from json file
        self.backupDict =inputDic
        self.dict  = inputDic
        self.table = inputDic["tableName"]
        self.columns = [k for k in self.dict.keys() if k != "tableName"]
    
    def get_random_value(self, column):
        """ recieves string with the name of a column(key) and returns a random value from that key's values """
        randomValue = self.dict[column][random.randint(0,(len(self.dict[column])-1))]
        if type(randomValue) == str:
            randomValue = f"'{randomValue}'"
        return randomValue

    def status(self):
        """Returns a string value with the current table name, columns and configs"""
        statusCheck = f"The table name is {self.table}\nColumns are: {', '.join(self.columns)}"
        return statusCheck
    

    def export(self, n_inserts= 1, write2file= False, path="insertMadness_export.txt"):
        """
        Returns a list of Insert queries selecting random values from the dictionary provided
        n_inserts: numbers of insert queries to return (default=1)
        """
        return_list =[]
        for times in range(n_inserts):
            query = (
            f"INSERT INTO {self.table} ({', '.join(self.columns)}) VALUES (" +
            f"{self.get_random_value(self.columns[0])}"
            )
            # if columns has more than 1 value, keep concatenating corresponding random values
            #Then close the query with ");"
            if len(self.columns) > 1:
                #itinerate and concatenate starting from the second value of the list
                for i in range(1,len(self.columns)):
                    query = query + f", {self.get_random_value(self.columns[i])}"
            query = query + ");" 
            return_list.append(query)           
        if write2file == False:
            return return_list
        else:
            with open(path, "a") as f_obj:
                f_obj.write("---------------------------------------------------------------------\n")
                f_obj.write(str(datetime.datetime.now()) +":\n")
                f_obj.write("\n".join(list(return_list)))

    
    def glide(self, column, interval=1):
        """Glide takes the lower and higher numerical values of the column and creates new values
        in the dictionary separated by the given interval 
        """
        #TODO: find the higher and lower value of the column's list
        minNumber = min(self.dict[column])
        maxNumber = max(self.dict[column])          
        #TODO: Clear the old list Populate the new list with new values starting from the lowest value
        #  and incrementing with the given interval
        self.dict[column] = [minNumber]
        while maxNumber >= self.dict[column][-1] + interval:
           self.dict[column].append(self.dict[column][-1] + interval)
    
    #TODO: unglide
    
    #TODO: restore (restores the changes made)

    #TODO: unrandomize column (instead of choosing random values it cicles through. asc or desc)
    

         