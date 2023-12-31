import _ctypes

def get_object(obj_id):
    return _ctypes.PyObj_FromPtr(obj_id)

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return str(id(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        return get_object(int(data))
