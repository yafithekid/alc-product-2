from lc.collections import Material


class MaterialDao:
    def find_by_id(self,_id:str) -> Material:
        raise NotImplementedError

    def insert(self,material:Material) -> str:
        raise NotImplementedError
