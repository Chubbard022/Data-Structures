class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(self.get_size() -1)

  def delete(self):
    # base case, no elements
    if self.get_size() < 1:     # empty list, bail
      return None
    if self.get_size() == 1:    # one-item list
      return self.storage.pop(0)
    ret = self.storage[0]
    self.storage[0] = self.storage.pop(self.get_size() - 1)
    self._sift_down(0)
    return ret

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if index == 0:
      return
    while (self.storage[index] > self.storage[(index-1) // 2] and index > 0):
      self.storage[index], self.storage[(index-1) // 2] = self.storage[(index-1) // 2], self.storage[index]
      index = (index-1) // 2

  def _sift_down(self, index):
    left = 2*index+1
    right = 2*index+2

    if left < self.get_size():
      if right < self.get_size():
          if self.storage[right] > self.storage[left]:
              left = right
          if self.storage[index] < self.storage[left]:
              self.storage[index], self.storage[left] = self.storage[left], self.storage[index]
              self._sift_down(left)