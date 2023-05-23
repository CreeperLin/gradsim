import kaolin


class TriangleMesh:

    @classmethod
    def from_obj(cls, path):
        return kaolin.io.obj.import_mesh(str(path))
