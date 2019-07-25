class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(self.get_size() -1)

  def delete(self):
    # base case, no elements
    if self.get_size() < 1:
      return None
    #second base case, only one
    if self.get_size() == 1:
      return self.storage.pop(0)
    else: 
      deleted_node = self.storage[0]
      self.storage[0] = self.storage.pop(self.get_size() -1)
      self._sift_down(0)
      return deleted_node

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    index = 0
    # base case
    if self.get_size() is 0:
      return None
    else:
      #checking to see if child node is bigger than parent node
      while(self.storage[index] > self.storage[(index - 1)//2] and index > 0):
        self.storage[index], self.storage[(index - 1)//2] = self.storage[(index - 1)//2], self.storage[index]
        index = self.storage[(index - 1)//2]

  def _sift_down(self, index):
    left = 2 * index + 1
    right = 2 * index + 2

    if self.get_size() == 0:
      return None
    else:
      if left < self.get_size():
        largest_node = left
        if right < self.get_size():
          if self.storage[right] > self.storage[left]:
            self.storage[index], self.storage[left] =  self.storage[left],self.storage[index]
            self._sift_down(left)