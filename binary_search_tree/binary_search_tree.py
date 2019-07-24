class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      #check to see if there is a left value
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        # recursively putting value in tree once find empty spot
        self.left.insert(value)
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass