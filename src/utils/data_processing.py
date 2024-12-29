import ast

class Dataset:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def sliceEnd(text, strToFind):
        if isinstance(strToFind, list):
            for i in strToFind:
                strIdx = text.lower().find(str(i).lower())
                if strIdx != -1:
                    return text[:strIdx]
                else:
                    return text
        else:
            strIdx = text.lower().find(str(strToFind).lower())
            if strIdx != -1:
                return text[:strIdx]
            else:
                return text

    @staticmethod
    def formatLb(text):
        textList = ast.literal_eval(text)
        uniqItems = []
        for i in textList:
            if i not in uniqItems:
                uniqItems.append(i)
        return uniqItems
    
    def applySliceEnd(self, column, strMarker):
        self.data[column] = self.data[column].apply(lambda x: self.sliceEnd(x, strMarker))
        return self.data

    def applyFormatLb(self, column):
        self.data[column] = self.data[column].apply(self.formatLb)
        return self.data
    
    
