from lc.collections import Material


class MaterialService:
    def find_by_id(self,_id:str) -> Material:
        raise NotImplementedError

    def add_material(self,material:Material) -> str:
        raise NotImplementedError